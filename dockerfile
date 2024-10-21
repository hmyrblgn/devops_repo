# Python 3.9 tabanlı bir imaj kullan
FROM python:3.9-slim

# Çalışma dizinini ayarla
WORKDIR /app

# Gereksinim dosyasını kopyala ve bağımlılıkları yükle
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Uygulama kodunu kopyala
COPY . .

# Servisi başlat
CMD ["python", "notification_service.py"]
