import cv2
import pandas as pd

drawing = False
ix, iy = -1, -1

def draw_rectangle(event, x, y, flags, param):
    global ix, iy, drawing, img, selected_section,mycsv

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            img_copy = img.copy()
            cv2.rectangle(img_copy, (ix, iy), (x, y), (0, 255, 0), 2)
            cv2.imshow('Selection Window', img_copy)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.rectangle(img, (ix, iy), (x, y), (0, 255, 0), 2)
        coordinates=(ix, iy, x - ix, y - iy)
        selected_section.append(coordinates)
        curr=mycsv.columns[len(selected_section)-1]
        write_text_on_image(img, curr,  coordinates)
        cv2.imshow('Selection Window', img)


def take_coordinates(number_of_attributes):
    global mycsv
    requirements={}
    cv2.imshow('Selection Window', img)
    cv2.setMouseCallback('Selection Window', draw_rectangle)

    while True:
        cv2.imshow('Selection Window', img)
        k = cv2.waitKey(1) & 0xFF
        if k == 27:
            break
        if(len(selected_section)==number_of_attributes):
            break
    cv2.destroyAllWindows()

    print(selected_section)
    i=0
    for key in mycsv.columns:
        requirements[key]=selected_section[i]
        i+=1
    return requirements

def write_text_on_image(img, text, coordinates):
    (x, y, w, h)= coordinates
    font_scale = min(w / 200, h / 50)
    thickness = 1
    text_size, _ = cv2.getTextSize(text, cv2.FONT_HERSHEY_SIMPLEX, font_scale, thickness)
    text_position = (x + (w - text_size[0]) // 2, y + (h + text_size[1]) // 2)
    border_color = (0, 0, 0)
    cv2.putText(img, text, text_position, cv2.FONT_ITALIC, font_scale,border_color, thickness, cv2.LINE_AA)

img_path = 'aa.png'
img = cv2.imread(img_path)

window_width = 1000
window_height = 800

original_height, original_width = img.shape[:2]

aspect_ratio = original_width / original_height

if original_width > original_height:
    new_width = window_width
    new_height = int(window_width / aspect_ratio)
else:
    new_height = window_height
    new_width = int(window_height * aspect_ratio) 

if new_width < original_width or new_height < original_height:
    interpolation = cv2.INTER_AREA
else:
    interpolation = cv2.INTER_CUBIC

# Resize the image
img= cv2.resize(img, (new_width, new_height), interpolation=interpolation)
main_copy = img.copy()
if img is None:
    print("Error loading image")
    exit()

selected_section = []
mycsv = pd.read_csv('./student_data.csv')

number_of_attributes=len(mycsv.columns)
requirements =take_coordinates(number_of_attributes)

print("\nSelected sections:")
print(requirements)
cv2.destroyAllWindows()

for index, row in mycsv.iterrows():
    save_copy = main_copy.copy()
    for key, value in requirements.items():
        write_text_on_image(save_copy, row[key], value)
    
    output_filename = f'./temp_certificates/{row["Roll Number"]}.jpg'
    cv2.imwrite(output_filename, save_copy)

print("Certificates created successfully.")
