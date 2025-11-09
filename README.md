# 🎨 Image Color Analyzer

Modern ve kullanıcı dostu bir web uygulaması ile görüntülerinizdeki renkleri analiz edin. Yüklediğiniz resimlerdeki dominant renkleri tespit eder, hex kodlarını gösterir ve tek tıkla kopyalama özelliği sunar.

## ✨ Özellikler

- 🖼️ **Resim Yükleme**: JPG, PNG ve diğer görüntü formatlarını destekler
- 🎯 **Renk Analizi**: K-Means clustering algoritması ile dominant renkleri tespit eder
- 📊 **Renk İstatistikleri**: Her rengin kullanım yüzdesini gösterir
- 🎨 **Hex Kodları**: Tüm renklerin hex kodlarını görüntüler
- 📋 **Kopyalama**: Tek tıkla hex kodunu panoya kopyalar
- 📱 **Responsive Tasarım**: Mobil ve masaüstü cihazlarda mükemmel görünüm
- 🌙 **Modern UI**: Karanlık tema ve glassmorphism efektleri

## 🚀 Hızlı Başlangıç

### Gereksinimler

- Python 3.8+
- pip (Python paket yöneticisi)

### Kurulum

1. **Repository'yi klonlayın:**
```bash
git clone <repository-url>
cd "Portfolyo 11"
```

2. **Sanal ortam oluşturun (önerilir):**
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

3. **Bağımlılıkları yükleyin:**
```bash
pip install -r requirements.txt
```

4. **Environment variables ayarlayın:**
```bash
# .env dosyası oluşturun
cp env.example .env

# .env dosyasını düzenleyin ve SECRET_KEY değerini ayarlayın
# Production için güvenli bir secret key oluşturun:
# python -c "import secrets; print(secrets.token_hex(32))"
```

5. **Gerekli klasörleri oluşturun:**
```bash
mkdir -p static/uploads
```

6. **Uygulamayı çalıştırın:**
```bash
python main.py
```

7. **Tarayıcınızda açın:**
```
http://localhost:5000
```

## 📦 Proje Yapısı

```
Portfolyo 11/
├── main.py                 # Flask uygulaması
├── requirements.txt        # Python bağımlılıkları
├── utils/
│   ├── __init__.py
│   └── image_utils.py     # Renk analizi utilities
├── templates/
│   └── home.html          # Ana sayfa template
├── static/
│   ├── styles.css         # CSS stilleri
│   └── uploads/           # Yüklenen resimler
```

## 🛠️ Teknolojiler

- **Backend**: Flask (Python)
- **Frontend**: HTML5, CSS3, JavaScript
- **Image Processing**: PIL (Pillow), NumPy
- **Machine Learning**: scikit-learn (K-Means)

## 🎯 Kullanım

1. Ana sayfada "Dosya Seç" butonuna tıklayın
2. Analiz etmek istediğiniz görüntüyü seçin
3. "Yükle" butonuna tıklayın
4. Yüklenen görüntü ve renk istatistikleri görüntülenecektir
5. Herhangi bir renk kartına tıklayarak hex kodunu kopyalayabilirsiniz

## 🔧 Yapılandırma

### Environment Variables

Proje `env.example` dosyasından `.env` dosyası oluşturularak yapılandırılır. Gerekli değişkenler:

- `SECRET_KEY`: Flask session ve flash mesajları için gerekli (zorunlu)
- `FLASK_ENV`: `development` veya `production` (opsiyonel)
- `MAX_CONTENT_LENGTH`: Maksimum dosya boyutu (byte cinsinden, varsayılan: 16MB)
- `UPLOAD_FOLDER`: Upload klasörü yolu (varsayılan: static/uploads)
- `PORT`: Port numarası (varsayılan: 5000, Render otomatik atar)

## 🐛 Sorun Giderme

### Resim yüklenmiyor
- Dosya formatının desteklendiğinden emin olun (JPG, PNG, etc.)
- Dosya boyutunun limit içinde olduğunu kontrol edin
- `static/uploads` klasörünün yazılabilir olduğundan emin olun

### Renk analizi çalışmıyor
- scikit-learn ve Pillow kütüphanelerinin yüklü olduğundan emin olun
- Resmin geçerli bir görüntü dosyası olduğunu kontrol edin

## 📝 Lisans

Bu proje açık kaynak kodludur ve MIT lisansı altında lisanslanmıştır.

## 👤 Geliştirici

Bu proje eğitim ve portfolyo amaçlı geliştirilmiştir.

---

# 🎨 Image Color Analyzer (English)

A modern and user-friendly web application to analyze colors in your images. Detects dominant colors in uploaded images, displays hex codes, and provides one-click copy functionality.

## ✨ Features

- 🖼️ **Image Upload**: Supports JPG, PNG and other image formats
- 🎯 **Color Analysis**: Detects dominant colors using K-Means clustering algorithm
- 📊 **Color Statistics**: Shows usage percentage of each color
- 🎨 **Hex Codes**: Displays hex codes for all colors
- 📋 **Copy to Clipboard**: One-click hex code copying
- 📱 **Responsive Design**: Perfect appearance on mobile and desktop devices
- 🌙 **Modern UI**: Dark theme and glassmorphism effects

## 🚀 Quick Start

### Requirements

- Python 3.8+
- pip (Python package manager)

### Installation

1. **Clone the repository:**
```bash
git clone <repository-url>
cd "Portfolyo 11"
```

2. **Create virtual environment (recommended):**
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

3. **Install dependencies:**
```bash
pip install -r requirements.txt
```

4. **Set up environment variables:**
```bash
# Create .env file
cp env.example .env

# Edit .env file and set SECRET_KEY value
# Generate a secure secret key for production:
# python -c "import secrets; print(secrets.token_hex(32))"
```

5. **Create necessary directories:**
```bash
mkdir -p static/uploads
```

6. **Run the application:**
```bash
python main.py
```

7. **Open in browser:**
```
http://localhost:5000
```

## 📦 Project Structure

```
Portfolyo 11/
├── main.py                 # Flask application
├── requirements.txt        # Python dependencies
├── utils/
│   ├── __init__.py
│   └── image_utils.py     # Color analysis utilities
├── templates/
│   └── home.html          # Home page template
├── static/
│   ├── styles.css         # CSS styles
│   └── uploads/           # Uploaded images
```

## 🛠️ Teknolojiler

- **Backend**: Flask (Python)
- **Frontend**: HTML5, CSS3, JavaScript
- **Image Processing**: PIL (Pillow), NumPy
- **Machine Learning**: scikit-learn (K-Means)

## 🎯 Usage

1. Click "Choose File" button on the home page
2. Select the image you want to analyze
3. Click "Upload" button
4. Uploaded image and color statistics will be displayed
5. Click any color card to copy the hex code

## 🔧 Configuration

### Environment Variables

The project is configured by creating a `.env` file from `env.example`. Required variables:

- `SECRET_KEY`: Required for Flask sessions and flash messages (required)
- `FLASK_ENV`: `development` or `production` (optional)
- `MAX_CONTENT_LENGTH`: Maximum file size in bytes (default: 16MB)
- `UPLOAD_FOLDER`: Upload folder path (default: static/uploads)
- `PORT`: Port number (default: 5000, Render auto-assigns)

## 🐛 Troubleshooting

### Image not uploading
- Make sure the file format is supported (JPG, PNG, etc.)
- Check that the file size is within the limit
- Ensure `static/uploads` directory is writable

### Color analysis not working
- Make sure scikit-learn and Pillow libraries are installed
- Check that the image is a valid image file

## 📝 License

This project is open source and licensed under the MIT License.

## 👤 Developer

This project was developed for educational and portfolio purposes.

