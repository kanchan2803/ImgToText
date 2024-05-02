import pytesseract
import cv2

#add your tesseract path here 
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

myconfig = r"--psm 11 --oem 3"

def extract_text(image_path):

  #Loading image in CV2 format
  img = cv2.imread(image_path)

  #Image preprocessing
  gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  cv2.imwrite("temp/gray.png", gray)
  blur = cv2.GaussianBlur(gray, (7,7), 0)
  cv2.imwrite("temp/blur.png", blur)

  thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
  kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,13))
  dilate = cv2.dilate(thresh, kernel, iterations=1)

  #Finding Contours for creating boundaries
  cnts = cv2.findContours(dilate, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
  cnts = cnts[0] if len(cnts) == 2 else cnts[1]
  cnts = sorted(cnts, key=lambda x: cv2.boundingRect(x)[0])

  for c in cnts:
    x, y, w, h = cv2.boundingRect(c)
    if h > 50 and w > 10:
      cv2.rectangle(img, (x,y), (x+w, y+h), (36,200,12), 2)

  cv2.imwrite("temp/boxes.png", img)

  # Text extraction
  text = pytesseract.image_to_string(gray,config=myconfig)

  print("Extracted Text:\n", text)
  return img, text
