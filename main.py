import os
from src.preprocess import preprocess_image
from src.predict import extract_text
from src.utils import extract_info, save_to_json, save_to_csv
import gradio as gr

def main():
    # Đường dẫn ảnh gốc
    input_image = "./data/invoices/img1.png"
    
    # Bước 2: Tiền xử lý
    processed_image = preprocess_image(input_image)
    print(f"✅ Tiền xử lý: {processed_image}")

    # Bước 3: Trích xuất văn bản
    text = extract_text(processed_image, use_easyocr=False)
    print("✅ Trích xuất văn bản:\n", text)

    # Bước 4: Trích xuất thông tin
    data = extract_info(text)
    print("✅ Trích xuất thông tin:\n", data)

    # Bước 5: Lưu trữ
    json_path = save_to_json(data)
    csv_path = save_to_csv(data)
    print(f"✅ Đã lưu JSON tại: {json_path}")
    print(f"✅ Đã lưu CSV tại: {csv_path}")

if __name__ == "__main__":
    main()
