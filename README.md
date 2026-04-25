# Sistem Prediksi Berbasis Machine Learning untuk Analisis Data Lari (Skripsi)

## Overview

Proyek ini merupakan implementasi tugas akhir (skripsi) yang bertujuan untuk membangun sistem prediksi berbasis machine learning menggunakan data aktivitas lari. Sistem ini dirancang untuk menganalisis berbagai faktor seperti jarak, elevasi, kategori lomba, dan kondisi lingkungan guna menghasilkan prediksi performa.

## Objectives

* Mengembangkan model machine learning untuk prediksi performa aktivitas lari
* Menganalisis pengaruh fitur seperti jarak, elevasi, dan cuaca terhadap hasil prediksi
* Mengimplementasikan sistem yang dapat digunakan untuk membantu pengambilan keputusan dalam aktivitas olahraga

## Dataset

Dataset yang digunakan:

* `utmb_with_weather_data.csv`

Dataset ini mencakup:

* Informasi aktivitas lari (jarak, elevasi, kategori)
* Data tambahan seperti kondisi cuaca
* Variabel target berupa performa (waktu/tempuh)

Catatan:

* Pastikan dataset tersedia di direktori root project sebelum menjalankan program

## Project Structure

```id="psk01"
PROJEK SKRIPSI/
│
├── output_Skripsi_Final_Lengkap/   # Hasil output model dan analisis
├── venv/                          # Virtual environment (tidak disarankan untuk di-upload)
├── __pycache__/                   # Cache Python
├── nutrition.py                   # Modul tambahan (jika ada preprocessing/fitur)
├── Skripsi.py                     # Script utama sistem
├── Train.ipynb                    # Notebook untuk training dan eksperimen
├── utmb_with_weather_data.csv     # Dataset utama
└── README.md                      # Dokumentasi proyek
```

## Workflow

1. Data Loading
   Membaca dataset dan memahami struktur data

2. Data Preprocessing

   * Membersihkan data
   * Menangani missing values
   * Feature engineering

3. Exploratory Data Analysis (EDA)

   * Analisis distribusi data
   * Korelasi antar fitur
   * Identifikasi pola

4. Modeling

   * Training model machine learning
   * Eksperimen dengan beberapa algoritma

5. Evaluation

   * Evaluasi performa model menggunakan metrik yang relevan
   * Analisis hasil prediksi

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Jupyter Notebook

## Installation

1. Clone repository:

```id="skr02"
git clone https://github.com/Mannasd/nama-repo-skripsi.git
```

2. Masuk ke direktori:

```id="skr03"
cd nama-repo-skripsi
```

3. Install dependencies:

```id="skr04"
pip install -r requirements.txt
```

## Usage

### Menjalankan Notebook

```id="skr05"
jupyter notebook
```

Buka:

* `Train.ipynb` untuk proses training dan analisis

### Menjalankan Script

```id="skr06"
python Skripsi.py
```

## Results

Hasil dari proyek ini meliputi:

* Model machine learning yang mampu melakukan prediksi performa lari
* Analisis faktor-faktor yang mempengaruhi hasil prediksi
* Output sistem yang dapat digunakan sebagai referensi pengambilan keputusan

## Future Improvements

* Hyperparameter tuning untuk meningkatkan akurasi model
* Penambahan fitur eksternal (misalnya data cuaca real-time)
* Deployment model ke aplikasi berbasis web (Streamlit)
* Integrasi pipeline machine learning yang lebih terstruktur

## Notes

* Folder `venv/` dan `__pycache__/` sebaiknya tidak di-upload ke repository
* Gunakan `.gitignore` untuk menjaga kebersihan repository

## Author

Muhammad Annas Darunnaja

## License

Proyek ini dibuat untuk keperluan akademik dan pengembangan portofolio.
