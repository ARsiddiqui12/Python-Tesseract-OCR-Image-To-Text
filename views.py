from django.shortcuts import render
from django.http import HttpResponse
from PIL import Image
import pytesseract
from projimgtotxt import settings
import os

# Create your views here.
def ImageToText(imageName):
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    image_path = os.path.join(settings.IMAGES_DIR, imageName)
    image = Image.open(image_path)
    extracted_text = pytesseract.image_to_string(image)
    return extracted_text


def SaveImageText(text,fileName):
    fileName, file_extension = os.path.splitext(fileName)
    textName = os.path.join(settings.TEXT_DIR,str(fileName+".txt"))
    with open(textName, 'w') as file:
         file.write(str(text)) 
    

def ImgtoTxt(request):
    for fileName in os.listdir(settings.IMAGES_DIR):
        imageText = ImageToText(fileName)
        SaveImageText(imageText,fileName)

    return HttpResponse(imageText, content_type='text/plain')
    

