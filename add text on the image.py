import cv2
image = cv2.imread('image.jpg')
res_img = cv2.resize(image,(400,350))
text = 'katana'
position = (30, 50)
font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 1
color = (255, 0, 0)
thickness = 2
cv2.putText(res_img, text, position, font, font_scale, color, thickness)
cv2.imshow('Image with Text', res_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
