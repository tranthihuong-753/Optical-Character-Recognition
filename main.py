import os
from src.preprocess import preprocess_image_ui
from src.predict import extract_text_ui
from src.utils import extract_info_ui
import gradio as gr
import cv2
import numpy as np

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