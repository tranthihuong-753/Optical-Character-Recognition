OCR Project
📂 Cấu trúc thư mục
css
Copy
Edit
OCR/
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
🚀 Tiến độ của dự án
1. Tiền xử lý ảnh (Trong preprocess.py)
Chuyển ảnh sang dạng grayscale

Tăng chất lượng ảnh: resize, denoise

Sửa nghiêng ảnh tự động

Tăng độ tương phản của ảnh

2. Nhận dạng văn bản (Trong predict.py)
Sử dụng 2 engine OCR: Tesseract và EasyOCR

Có thể chuyển đổi giữa 2 engine thông qua tham số

Tối ưu hóa cấu hình cho từng engine

Hỗ trợ tiếng Việt và tiếng Anh

3. Xử lý và lưu trữ kết quả
Trích xuất thông tin từ văn bản đã nhận dạng

Lưu kết quả dưới dạng JSON và CSV

💡 Các tính năng có thể nâng cấp
1. Học có giám sát (Supervised Learning)
KNN hoặc SVM để phân loại các mẫu hóa đơn khác nhau

Decision Trees để phân loại các vùng văn bản trên hóa đơn (tiêu đề, nội dung, tổng tiền)

Logistic Regression để phân loại xem một vùng văn bản có phải là số tiền hay không

2. Học không giám sát (Unsupervised Learning)
K-means clustering để nhóm các hóa đơn có định dạng tương tự

PCA để giảm chiều dữ liệu ảnh trước khi đưa vào OCR

Anomaly Detection để phát hiện hóa đơn bất thường hoặc giả mạo

3. Học tăng cường (Reinforcement Learning)
Xây dựng agent để tối ưu hóa các tham số xử lý ảnh (độ sáng, độ tương phản)

Tối ưu hóa việc lựa chọn các vùng văn bản quan trọng trên hóa đơn

📋 Cài đặt
Cài đặt các thư viện cần thiết: Chạy lệnh sau trong terminal:

bash
Copy
Edit
pip install -r requirements.txt
Chạy chương trình chính: Để chạy dự án, sử dụng lệnh:

bash
Copy
Edit
python main.py
📚 Mô tả dự án
Dự án này tập trung vào việc sử dụng các kỹ thuật OCR để nhận dạng văn bản từ hóa đơn, đặc biệt là hóa đơn tiếng Việt và tiếng Anh. Mục tiêu là phát triển một hệ thống có khả năng nhận diện thông tin từ hóa đơn một cách tự động và lưu trữ kết quả theo dạng có thể phân tích được. Dự án này sử dụng các kỹ thuật tiền xử lý ảnh, học máy và học sâu để tối ưu hóa quá trình nhận dạng.

📝 Liên hệ
Nếu bạn có bất kỳ câu hỏi nào hoặc cần hỗ trợ thêm, đừng ngần ngại liên hệ với tôi qua email: dhuongdhlt1@gmail.com

