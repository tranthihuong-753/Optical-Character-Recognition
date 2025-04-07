<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>OCR Project</title>
</head>
<body>
    <h1>OCR Project</h1>

    <h2>📂 Cấu trúc thư mục</h2>
    <pre>
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
    </pre>

    <h2>🚀 Tiến độ của dự án</h2>

    <h3>1. Tiền xử lý ảnh (Trong <code>preprocess.py</code>)</h3>
    <ul>
        <li>Chuyển ảnh sang dạng <strong>grayscale</strong></li>
        <li>Tăng chất lượng ảnh: <strong>resize</strong>, <strong>denoise</strong></li>
        <li><strong>Sửa nghiêng ảnh</strong> tự động</li>
        <li>Tăng độ <strong>tương phản</strong> của ảnh</li>
    </ul>

    <h3>2. Nhận dạng văn bản (Trong <code>predict.py</code>)</h3>
    <ul>
        <li>Sử dụng <strong>2 engine OCR</strong>: <strong>Tesseract</strong> và <strong>EasyOCR</strong></li>
        <li>Có thể chuyển đổi giữa 2 engine thông qua tham số</li>
        <li>Tối ưu hóa cấu hình cho từng engine</li>
        <li><strong>Hỗ trợ tiếng Việt</strong> và tiếng Anh</li>
    </ul>

    <h3>3. Xử lý và lưu trữ kết quả</h3>
    <ul>
        <li>Trích xuất thông tin từ văn bản đã nhận dạng</li>
        <li>Lưu kết quả dưới dạng <strong>JSON</strong> và <strong>CSV</strong></li>
    </ul>

    <h2>💡 Các tính năng có thể nâng cấp</h2>

    <h3>1. Học có giám sát (Supervised Learning)</h3>
    <ul>
        <li><strong>KNN</strong> hoặc <strong>SVM</strong> để phân loại các mẫu hóa đơn khác nhau</li>
        <li><strong>Decision Trees</strong> để phân loại các vùng văn bản trên hóa đơn (tiêu đề, nội dung, tổng tiền)</li>
        <li><strong>Logistic Regression</strong> để phân loại xem một vùng văn bản có phải là số tiền hay không</li>
    </ul>

    <h3>2. Học không giám sát (Unsupervised Learning)</h3>
    <ul>
        <li><strong>K-means clustering</strong> để nhóm các hóa đơn có định dạng tương tự</li>
        <li><strong>PCA</strong> để giảm chiều dữ liệu ảnh trước khi đưa vào OCR</li>
        <li><strong>Anomaly Detection</strong> để phát hiện hóa đơn bất thường hoặc giả mạo</li>
    </ul>

    <h3>3. Học tăng cường (Reinforcement Learning)</h3>
    <ul>
        <li>Xây dựng <strong>agent</strong> để tối ưu hóa các tham số xử lý ảnh (độ sáng, độ tương phản)</li>
        <li>Tối ưu hóa việc lựa chọn các vùng văn bản quan trọng trên hóa đơn</li>
    </ul>

    <h2>📋 Cài đặt</h2>

    <h3>1. Cài đặt các thư viện cần thiết:</h3>
    <p>Chạy lệnh sau trong terminal:</p>
    <pre><code>pip install -r requirements.txt</code></pre>

    <h3>2. Chạy chương trình chính:</h3>
    <p>Để chạy dự án, sử dụng lệnh:</p>
    <pre><code>python main.py</code></pre>

    <h2>📚 Mô tả dự án</h2>
    <p>Dự án này tập trung vào việc sử dụng các kỹ thuật OCR để nhận dạng văn bản từ hóa đơn, đặc biệt là hóa đơn tiếng Việt và tiếng Anh. Mục tiêu là phát triển một hệ thống có khả năng nhận diện thông tin từ hóa đơn một cách tự động và lưu trữ kết quả theo dạng có thể phân tích được. Dự án này sử dụng các kỹ thuật tiền xử lý ảnh, học máy và học sâu để tối ưu hóa quá trình nhận dạng.</p>

    <h2>📝 Liên hệ</h2>
    <p>Nếu bạn có bất kỳ câu hỏi nào hoặc cần hỗ trợ thêm, đừng ngần ngại liên hệ với tôi qua email: <strong>your_email@example.com</strong></p>
</body>
</html>
