import cv2

drawing = False  
ix, iy = -1, -1  


def draw_rectangle(event, x, y, flags, param):
    global ix, iy, drawing, img, selected_section

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            img_copy = img.copy()
            cv2.rectangle(img_copy, (ix, iy), (x, y), (0, 255, 0), 2)
            cv2.imshow('image', img_copy)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.rectangle(img, (ix, iy), (x, y), (0, 255, 0), 2)
        cv2.imshow('image', img)
        selected_section.append((ix, iy, x - ix, y - iy))

def take_coordinates(s):
    global selected_section
    selected_section = []

    cv2.imshow('image', img)
    cv2.setMouseCallback('image', draw_rectangle)

    while True:
        cv2.imshow('image', img)
        k = cv2.waitKey(1) & 0xFF
        if k == 27:  # 'ESC' to close the window
            break

    cv2.destroyAllWindows()

    print(f"Selected sections for {s}:", selected_section)
    return selected_section

def write_text_on_image(img, text, coordinates):
    for (x, y, w, h) in coordinates:
        center_x = x + w // 2
        center_y = y + h // 2
        text_size, _ = cv2.getTextSize(text, cv2.FONT_HERSHEY_SIMPLEX, 0.9, 2)
        text_position = (center_x - text_size[0] // 2, center_y + text_size[1] // 2)
        cv2.putText(img, text, text_position, cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)




img = cv2.imread('a.png')
save_copy = img.copy()  
if img is None:
    print("Error loading image")
    exit()

selected_section = []
requirements = {}

while True:
    s = input("Enter the addon name (or 'NOPE' to finish): ")
    if s == "NOPE":
        break
    sections = take_coordinates(s)
    requirements[s] = sections

print("\nSelected sections:")
print(requirements)

for key, value in requirements.items():
    text = input(f"Enter text for {key}: ")
    write_text_on_image(save_copy, text, value)


cv2.imshow('Certificate', save_copy)
cv2.waitKey(0)
cv2.destroyAllWindows()

output_filename = 'certificate1.jpg'
cv2.imwrite(output_filename, save_copy)
