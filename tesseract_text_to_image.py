import pytesseract
from PIL import Image

file_name = "numbers"

img = Image.open(f'C:\\Users\\vlaso\\OneDrive\\images_for_tesseract\\{file_name}.png')
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'  # path to installed tesseract for Windows
text = pytesseract.image_to_string(img)
print(text)
