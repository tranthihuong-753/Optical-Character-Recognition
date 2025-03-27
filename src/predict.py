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

""" ef enhance_image(image):
    # Tăng chất lượng ảnh trước khi OCR
    # Điều chỉnh kích thước (tăng gấp đôi nếu ảnh nhỏ)
    scale_factor = 2
    height, width = image.shape[:2]
    resized = cv2.resize(image, (width * scale_factor, height * scale_factor), interpolation=cv2.INTER_LINEAR)

    # Tăng độ tương phản
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    enhanced = clahe.apply(resized)
    
    return enhanced

def extract_text(image_path, use_easyocr=False):
    # Đọc ảnh
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)  # Đọc trực tiếp thành grayscale
    if image is None:
        raise ValueError(f"Không thể đọc ảnh: {image_path}")

    # Tăng chất lượng ảnh
    optimized_image = enhance_image(image)

    if use_easyocr:
        # Dùng EasyOCR
        reader = easyocr.Reader(['vi', 'en'], gpu=False)  # Tắt GPU nếu không cần
        result = reader.readtext(optimized_image, detail=0, paragraph=True, min_size=10)
        text = "\n".join(result)
    else:
        # Dùng Tesseract với cấu hình tối ưu
        custom_config = r'--oem 1 --psm 6 -l vie'  # OEM 1: LSTM, PSM 6: Khối văn bản
        text = pytesseract.image_to_string(optimized_image, config=custom_config)

    return text.strip()

if __name__ == "__main__":
    image_path = "data/processed/img1.png"
    # Thử với Tesseract
    text_tesseract = extract_text(image_path, use_easyocr=False)
    print("Tesseract Output:\n", text_tesseract)
    
    # Thử với EasyOCR
    text_easyocr = extract_text(image_path, use_easyocr=True)
    print("\nEasyOCR Output:\n", text_easyocr)

 """
""" 
import cv2
import numpy as np
import pytesseract
import easyocr
import os

def deskew_image(image):
    # Sửa nghiêng ảnh nếu có
    # Tìm góc nghiêng bằng Hough Transform
    edges = cv2.Canny(image, 50, 150, apertureSize=3)
    lines = cv2.HoughLines(edges, 1, np.pi / 180, 200)
    
    if lines is not None:
        angle = 0
        for rho, theta in lines[0]:
            angle = (theta * 180 / np.pi) - 90
            break
        (h, w) = image.shape[:2]
        center = (w // 2, h // 2)
        M = cv2.getRotationMatrix2D(center, angle, 1.0)
        rotated = cv2.warpAffine(image, M, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)
        return rotated
    return image

def enhance_image(image):
    # Tăng chất lượng ảnh trước khi OCR
    # Điều chỉnh kích thước
    scale_factor = 2
    height, width = image.shape[:2]
    resized = cv2.resize(image, (width * scale_factor, height * scale_factor), interpolation=cv2.INTER_LINEAR)

    # Lọc nhiễu
    denoised = cv2.fastNlMeansDenoising(resized, h=10)

    # Sửa nghiêng
    deskewed = deskew_image(denoised)

    # Tăng độ tương phản
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    enhanced = clahe.apply(deskewed)

    # Ngưỡng hóa để làm rõ chữ
    _, thresh = cv2.threshold(enhanced, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    
    return thresh

def extract_text(image_path, use_easyocr=False):
    # Đọc ảnh trực tiếp thành grayscale
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if image is None:
        raise ValueError(f"Không thể đọc ảnh: {image_path}")

    # Tăng chất lượng ảnh
    optimized_image = enhance_image(image)

    # Lưu ảnh tạm để kiểm tra (optional)
    cv2.imwrite("data/processed/optimized_temp.png", optimized_image)

    if use_easyocr:
        # Dùng EasyOCR
        reader = easyocr.Reader(['vi', 'en'], gpu=False)
        result = reader.readtext(optimized_image, detail=0, paragraph=True, min_size=5)  # Giảm min_size
        text = "\n".join(result)
    else:
        # Dùng Tesseract với cấu hình tối ưu
        custom_config = r'--oem 1 --psm 3 -l vie'  # PSM 3: Full auto, tốt cho hóa đơn
        text = pytesseract.image_to_string(optimized_image, config=custom_config)

    # Hậu xử lý đơn giản
    text = text.replace("Tổng cong", "Tổng cộng").replace("Tổng cổng", "Tổng cộng")
    return text.strip()

if __name__ == "__main__":
    image_path = "data/processed/img1.png"   
    text_tesseract = extract_text(image_path, use_easyocr=False) """

# Sửa nghiêng ảnh nếu có
def deskew_image(image):
    # Tìm góc nghiêng bằng Hough Transform
    edges = cv2.Canny(image, 50, 150, apertureSize=3)
    lines = cv2.HoughLines(edges, 1, np.pi / 180, 200)
    
    if lines is not None:
        angle = 0
        for rho, theta in lines[0]:
            angle = (theta * 180 / np.pi) - 90
            break
        (h, w) = image.shape[:2]
        center = (w // 2, h // 2)
        M = cv2.getRotationMatrix2D(center, angle, 1.0)
        rotated = cv2.warpAffine(image, M, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)
        return rotated
    return image

# Tăng chất lượng ảnh trước khi OCR
def enhance_image(image):
    # Điều chỉnh kích thước
    scale_factor = 2
    height, width = image.shape[:2]
    resized = cv2.resize(image, (width * scale_factor, height * scale_factor), interpolation=cv2.INTER_LINEAR)

    # Lọc nhiễu
    denoised = cv2.fastNlMeansDenoising(resized, h=10)

    # Sửa nghiêng
    deskewed = deskew_image(denoised)

    # Tăng độ tương phản
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    enhanced = clahe.apply(deskewed)

    # Ngưỡng hóa để làm rõ chữ
    _, thresh = cv2.threshold(enhanced, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    
    return thresh

def extract_text(image, use_easyocr=False):
    # Tăng chất lượng ảnh
    optimized_image = enhance_image(image)

    # Lưu ảnh tạm để kiểm tra (optional)
    cv2.imwrite("data/processed/optimized_temp.png", optimized_image)

    if use_easyocr:
        # Dùng EasyOCR
        reader = easyocr.Reader(['vi', 'en'], gpu=False)
        result = reader.readtext(optimized_image, detail=0, paragraph=True, min_size=5)  # Giảm min_size
        text = "\n".join(result)
    else:
        # Dùng Tesseract với cấu hình tối ưu
        custom_config = r'--oem 1 --psm 3 -l vie'  # PSM 3: Full auto, tốt cho hóa đơn
        text = pytesseract.image_to_string(optimized_image, config=custom_config)

    # Hậu xử lý đơn giản
    text = text.replace("Tổng cong", "Tổng cộng").replace("Tổng cổng", "Tổng cộng")
    return text.strip()

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

def enhance_image_ui(image):
    scale_factor = 2
    height, width = image.shape[:2]
    resized = cv2.resize(image, (width * scale_factor, height * scale_factor), interpolation=cv2.INTER_LINEAR)
    denoised = cv2.fastNlMeansDenoising(resized, h=10)
    deskewed = deskew_image(denoised)
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    enhanced = clahe.apply(deskewed)
    _, thresh = cv2.threshold(enhanced, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    return thresh

def extract_text_ui(image, use_easyocr=False):
    optimized_image = enhance_image(image)

    if use_easyocr:
        reader = easyocr.Reader(['vi', 'en'], gpu=False)
        result = reader.readtext(optimized_image, detail=0, paragraph=True, min_size=5)
        text = "\n".join(result)
    else:
        custom_config = r'--oem 1 --psm 3 -l vie'
        text = pytesseract.image_to_string(optimized_image, config=custom_config)

    text = text.replace("Tổng cong", "Tổng cộng").replace("Tổng cổng", "Tổng cộng")
    return text.strip()


