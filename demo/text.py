import cv2
import numpy as np

image = np.zeros((600, 800, 3), dtype=np.uint8)

text = "Hello, OpenCV!"

font = cv2.FONT_HERSHEY_SIMPLEX

font_scale = 2
font_thickness = 3
font_color = (255, 255, 255) 

(text_width, text_height), baseline = cv2.getTextSize(text, font, font_scale, font_thickness)

text_x = (image.shape[1] - text_width) // 2
text_y = (image.shape[0] + text_height) // 2

background_color = (0, 0, 0)  
cv2.rectangle(image, (text_x, text_y - text_height - baseline), (text_x + text_width, text_y + baseline), background_color, -1)

border_color = (0, 0, 0)  
cv2.putText(image, text, (text_x, text_y), font, font_scale, border_color, font_thickness + 2, cv2.LINE_AA)

cv2.putText(image, text, (text_x, text_y), font, font_scale, font_color, font_thickness, cv2.LINE_AA)

cv2.imshow('Image with Text', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
