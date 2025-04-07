import cv2
import pytesseract
import easyocr
import numpy as np
import pytesseract
import easyocr
import os

# Cấu hình Tesseract 
pytesseract.pytesseract.tesseract_cmd = r"D:\\Program Files\\Tesseract-OCR\\tesseract.exe"

# Hỗ trợ cả Tesseract và EasyOCR, tùy chọn qua tham số use_easyocr
def deskew_image_ui(image):
    edges = cv2.Canny(image, 50, 150, apertureSize=3)
    lines = cv2.HoughLines(edges, 1, np.pi / 180, 200)
    
    if lines is not None:
        for rho, theta in lines[0]:
            angle = (theta * 180 / np.pi) - 90
            (h, w) = image.shape[:2]
            center = (w // 2, h // 2)
            M = cv2.getRotationMatrix2D(center, angle, 1.0)
            return cv2.warpAffine(image, M, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)
    return image

# Tăng cường hình ảnh trước khi nhận diện văn bản
def enhance_image_ui(image):
    scale_factor = 2
    height, width = image.shape[:2]
    resized = cv2.resize(image, (width * scale_factor, height * scale_factor), interpolation=cv2.INTER_LINEAR)
    denoised = cv2.fastNlMeansDenoising(resized, h=10)
    deskewed = deskew_image_ui(denoised)
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    enhanced = clahe.apply(deskewed)
    _, thresh = cv2.threshold(enhanced, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    return thresh

def extract_text_ui(image, use_easyocr=False):
    #optimized_image = enhance_image_ui(image)
    optimized_image = image

    if use_easyocr:
        reader = easyocr.Reader(['vi', 'en'], gpu=False)
        result = reader.readtext(optimized_image, detail=0, paragraph=True, min_size=5)
        text = "\n".join(result)
    else:
        custom_config = r'--oem 1 --psm 3 -l vie'
        text = pytesseract.image_to_string(optimized_image, config=custom_config)

    text = text.replace("Tổng cong", "Tổng cộng").replace("Tổng cổng", "Tổng cộng")
    return text.strip()


