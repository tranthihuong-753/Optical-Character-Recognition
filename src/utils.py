import re
import json
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

# Hàm Fuzzy Matching để sửa lỗi nhận dạng
def fuzzy_correct(text, correction_dict):
    corrected_text = text
    for wrong_char, correct_char in correction_dict.items():
        print(f"Comparing {wrong_char} with {correct_char} = {fuzz.partial_ratio(wrong_char, corrected_text)}")  # In để theo dõi so sánh
        # Sử dụng fuzzy matching để thay thế ký tự sai
        if fuzz.partial_ratio(wrong_char, corrected_text) > 50:  # Tỉ lệ độ tương đồng > 50%
            corrected_text = corrected_text.replace(wrong_char, correct_char)
    return corrected_text

# Fuzzy logic cho total 
corrections_total = {
    "I": "1",
    "L": "1",
    "S": "5",
    "Z": "2",
    "5": "$",
    "B": "8",
    "G": "6",
    "Q": "0",
}
def correct_total(total_str):
    if not total_str:
        return "0"
    
    # Áp dụng Fuzzy Logic để thay thế ký tự sai
    total_str = fuzzy_correct(total_str, corrections_total)
    
    # Kiểm tra định dạng đúng sau khi sửa (cập nhật biểu thức chính quy để phù hợp hơn)
    if re.match(r"^\d{1,3}(?:[.,]\d{3})*(?:\.\d{1,2})?$", total_str):
        return total_str
    else:
        return "0"

# Hàm Fuzzy Matching để nhận diện phương thức thanh toán
def detect_payment_method(text):
    payment_methods = {
        "Tiền mặt": ["tiền mặt", "cash"],
        "Thẻ": ["thẻ", "card", "credit card", "debit card"],
        "Ví điện tử": ["ví điện tử", "ví", "e-wallet", "mobile wallet"]
    }

    # Kiểm tra từng phương thức thanh toán với Fuzzy Matching
    for method, keywords in payment_methods.items():
        for keyword in keywords:
            if fuzz.partial_ratio(keyword, text.lower()) > 80:  # Tỉ lệ độ tương đồng > 80%
                return method

    return "Không xác định"  # Trường hợp không tìm thấy phương thức nào

def extract_info_ui(text):
    data = {"store_name": "", "date": "", "items": [], "total": "", "payment_method": ""}
    
    lines = text.split("\n")
    if lines:
        data["store_name"] = lines[0].strip()

    date_match = re.search(r"\d{2}[/|-]\d{2}[/|-]\d{4}", text)
    if date_match:
        data["date"] = date_match.group()

    total_match = re.search(r"Tiền mặt:?\s*(\d{1,3}(?:[.,]\d{3})*)", text)
    if total_match:
        # Sử dụng hàm sửa lỗi Fuzzy để đảm bảo tổng cộng chính xác
        data["total"] = correct_total(total_match.group(1))

    for line in lines:
        if line.strip() and not any(keyword in line.lower() for keyword in ["tổng", "ngày", "thanh toán"]):
            data["items"].append(line.strip())

    # Sử dụng hàm detect_payment_method để xác định phương thức thanh toán
    data["payment_method"] = detect_payment_method(text)

    return json.dumps(data, indent=4, ensure_ascii=False)
