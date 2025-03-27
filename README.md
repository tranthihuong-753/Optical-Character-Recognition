📂 OCR/
│── 📂 data/                # Thư mục chứa dữ liệu (hình ảnh, CSV, JSON,...)
│── 📂 results/             # Lưu trữ kết quả đầu ra
│── 📂 src/                 # Chứa mã nguồn chính của dự án
│   │── 📜 train.py         # Huấn luyện mô hình
│   │── 📜 predict.py       # Dự đoán với mô hình
│   │── 📜 preprocess.py    # Tiền xử lý dữ liệu
│   │── 📜 utils.py         # Các hàm hỗ trợ (hàm vẽ biểu đồ, đọc dữ liệu,...)
│── 📜 requirements.txt     # Danh sách thư viện cần cài đặt
│── 📜 main.py              # Chương trình chính chạy AI
│── 📜 README.md            # Mô tả dự án, cách chạy
│── 📜 .gitignore           # Loại trừ các file không cần thiết khi đẩy lên GitHub

│── 📂 models/              # Lưu trữ mô hình đã huấn luyện
│── 📂 notebooks/           # Chứa các file Jupyter Notebook (nếu cần)
│── 📂 logs/                # Lưu trữ log của quá trình chạy mô hình
│── 📂 tests/               # Chứa các tập tin kiểm thử

TIẾN ĐỘ CỦA DỰ ÁN 
1. Tiền xử lý ảnh (trong preprocess.py):
Chuyển ảnh sang grayscale
Tăng chất lượng ảnh (resize, denoise)
Sửa nghiêng ảnh tự động
Tăng độ tương phản

2. Nhận dạng văn bản (trong predict.py):
Sử dụng 2 engine OCR: Tesseract và EasyOCR
Có thể chuyển đổi giữa 2 engine thông qua tham số
Tối ưu hóa cấu hình cho từng engine
Hỗ trợ cả tiếng Việt và tiếng Anh

3. Xử lý và lưu trữ kết quả:
Trích xuất thông tin từ text được nhận dạng
Lưu kết quả dưới dạng JSON và CSV

CÓ THỂ NÂNG CẤP 
1. Học có giám sát (Supervised Learning):
Sử dụng KNN hoặc SVM để phân loại các mẫu hóa đơn khác nhau
Decision Trees để phân loại các vùng text trên hóa đơn (tiêu đề, nội dung, tổng tiền)
Logistic Regression để phân loại xem một vùng text có phải là số tiền hay không

2. Học không giám sát (Unsupervised Learning):
K-means clustering để nhóm các hóa đơn có format tương tự
PCA để giảm chiều dữ liệu ảnh trước khi đưa vào OCR
Anomaly Detection để phát hiện hóa đơn bất thường hoặc giả mạo

3. Học tăng cường (Reinforcement Learning):
Xây dựng agent để tối ưu hóa các tham số xử lý ảnh (độ sáng, độ tương phản)
Tối ưu hóa việc lựa chọn vùng text quan trọng trên hóa đơn
