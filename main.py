import os
from src.preprocess import preprocess_image, preprocess_image_ui
from src.predict import extract_text, extract_text_ui
from src.utils import extract_info, save_to_json, save_to_csv, extract_info_ui
import gradio as gr
import cv2
import numpy as np
import easyocr
import pytesseract
import json
import re

""" def main():
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
    main() """

def process_receipt_ui(image):
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    processed = preprocess_image_ui(image)
    text = extract_text_ui(processed)
    extracted_info = extract_info_ui(text)
    return processed, extracted_info

# Tạo giao diện Gradio
iface = gr.Interface(
    fn=process_receipt_ui,
    inputs=gr.Image(type="numpy"),
    outputs=[gr.Image(type="numpy"), gr.JSON()],
    title="Hệ thống nhận diện hóa đơn",
    description="Tải lên ảnh hóa đơn để trích xuất thông tin",
)

iface.launch()