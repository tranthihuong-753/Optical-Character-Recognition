import re
import json
from fuzzywuzzy import fuzz

# Sửa lỗi OCR bằng Fuzzy Logic cơ bản.
def correct_total(total_str):
    if not total_str:
        return "0"
    corrected = total_str.replace("O", "0").replace("I", "1")
    return corrected if re.match(r"\d{1,3}(?:[.,]\d{3})*", corrected) else "0"

# Trích xuất thông tin thành dictionary.
def extract_info(text):
    data = {
        "store_name": "",
        "date": "",
        "items": [],
        "total": "",
        "payment_method": ""
    }

    lines = text.split("\n")
    if lines:
        data["store_name"] = lines[0].strip()

    date_match = re.search(r"\d{2}/\d{2}/\d{4}", text)
    if date_match:
        data["date"] = date_match.group()

    total_match = re.search(r"Tổng cộng:?\s*(\d{1,3}(?:[.,]\d{3})*)", text)
    if total_match:
        data["total"] = correct_total(total_match.group(1))

    for line in lines:
        if line.strip() and not any(keyword in line.lower() for keyword in ["tổng", "ngày", "thanh toán"]):
            data["items"].append(line.strip())

    if "tiền mặt" in text.lower():
        data["payment_method"] = "Tiền mặt"
    elif "thẻ" in text.lower():
        data["payment_method"] = "Thẻ"
    elif "ví" in text.lower():
        data["payment_method"] = "Ví điện tử"

    return data

# Lưu dữ liệu vào file JSON.
def save_to_json(data, output_path="results/data.json"):
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    return output_path
import pandas as pd

def save_to_csv(data, output_path="results/receipt_data.csv"):
    df = pd.DataFrame({
        "Store Name": [data["store_name"]],
        "Date": [data["date"]],
        "Items": [", ".join(data["items"])],
        "Total": [data["total"]],
        "Payment Method": [data["payment_method"]]
    })
    df.to_csv(output_path, index=False, encoding="utf-8-sig")
    return output_path

def extract_info_ui(text):
    data = {"store_name": "", "date": "", "items": [], "total": "", "payment_method": ""}
    
    lines = text.split("\n")
    if lines:
        data["store_name"] = lines[0].strip()

    date_match = re.search(r"\d{2}/\d{2}/\d{4}", text)
    if date_match:
        data["date"] = date_match.group()

    total_match = re.search(r"Tổng cộng:?\s*(\d{1,3}(?:[.,]\d{3})*)", text)
    if total_match:
        data["total"] = total_match.group(1)

    for line in lines:
        if line.strip() and not any(keyword in line.lower() for keyword in ["tổng", "ngày", "thanh toán"]):
            data["items"].append(line.strip())

    if "tiền mặt" in text.lower():
        data["payment_method"] = "Tiền mặt"
    elif "thẻ" in text.lower():
        data["payment_method"] = "Thẻ"
    elif "ví" in text.lower():
        data["payment_method"] = "Ví điện tử"

    return json.dumps(data, indent=4, ensure_ascii=False)

