import pytesseract as tess
tess.pytesseract.tesseract_cmd=r'D:\TESSERACT\tesseract.exe'; #path to tesseract exe
from PIL import Image

img=Image.open('corona.jpg'); #image open
text=tess.image_to_string(img); #convert image to string
print(text)


