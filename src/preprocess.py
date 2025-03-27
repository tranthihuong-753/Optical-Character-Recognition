import cv2
import numpy as np
import os

# Nhận đường dẫn ảnh, xử lý và lưu vào data/processed/
def preprocess_image(image_path, output_dir="data/processed", min_area=100, debug=False):
    # Đọc ảnh
    image = cv2.imread(image_path)
    if image is None:
        raise ValueError(f"Không thể đọc ảnh: {image_path}")

    # Chuyển sang grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Dùng adaptive threshold thay vì OTSU để giữ chi tiết viết tay
    thresh = cv2.adaptiveThreshold(
        gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
        cv2.THRESH_BINARY_INV, 11, 2
    )

    # Tạo thư mục đầu ra
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, os.path.basename(image_path))
    
    # Lưu ảnh đã xử lý
    cv2.imwrite(output_path, thresh)

    # Debug: Hiển thị 
    if debug:
        cv2.imshow("Threshold", thresh)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    return output_path

if __name__ == "__main__":
    input_path = "data/invoices/img1.png"
    processed_path = preprocess_image(input_path, debug=True)
    print(f"Ảnh đã xử lý lưu tại: {processed_path}")

def preprocess_image_ui(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2)
    return thresh
