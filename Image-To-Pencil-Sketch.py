import cv2
import random

def convert_to_pecilsketch(img):
    grey_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    invert_img = cv2.bitwise_not(grey_img)
    blur_img = cv2.GaussianBlur(invert_img, (21, 21),0)
    invert_blur_img = cv2.bitwise_not(blur_img)
    pecil_sketch = cv2.divide(grey_img, invert_blur_img, scale = 256.0)
    return pecil_sketch



print('ITPS ')

img_loc = input('ENTER THE LOCATION OF THE IMG IN YOUR SYSTEM THAT YOU WANT TO CONVERT TO PENCIL SKETCH ART ')


img = cv2.imread(img_loc)

file_name = str(random.randint(1,1000))+str(random.randint(1,1000))+'ITPS.png'

sketch = convert_to_pecilsketch(img)
#"C:\Users\User\Downloads\clipart1007838.png"
cv2.imwrite(file_name, sketch)
cv2.imshow(file_name, sketch)
cv2.waitKey(0)
cv2.destroyAllWindows()