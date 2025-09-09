**PERTANYAAN**
1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
3. Jelaskan peran settings.py dalam proyek Django!
4. Bagaimana cara kerja migrasi database di Django?
5. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
6. Apakah ada feedback untuk asisten dosen tutorial 1 yang telah kamu kerjakan sebelumnya?

JAWABAN
1. Cara saya mengimplementasikan checklist diatas adalah sebagai berikut:
    1. Membuat repository lokal
    2. Membuat repository github
    3. Mendownload python environment ke dalam repository local
    4. Mengaktifkan environment tersebut
    5. Memasukkan requirements.txt
    6. Mendownload seluruh requirements.txt
    7. Mengaitkan repository lokal dengan github dengan menyantumkan url remote github pada lokal repo
    8. Membuat model product seperti mendefinisikan nama, harga, stok, category, dsb dalam models.py
    9. Melakukan migrasi dari database yang ada ke bentuk data yang ada di models.py
    10. Membuat komponen views untuk mendefinisikan fungsi yang akan membuka file html terkait, beserta data yang akan diiterasi atau ditunjukkan pada html tersebut.
    11. Membuat komponen urls untuk menavigasi alamat html sehingga user dapat mudah mengakses child page dari aplikasi kita melalui tombol navigasi yang disediakan.
    12. Membuat komponen html untuk membuat kerangka visual website
    13. Membuat komponen penata css untuk menambahkan value estetika website (tidak bisa dilihat dari deployed site, harus run local untuk melihatnya)
    14. Menjalankan seluruh aplikasi menggunakan command python manage.py runserver

2. Bagan dapat dilihat di /Bagan_Request.PNG

3. Berkas settings.py berfungsi sebagai pusat kendali utama untuk sebuah proyek Django, di mana semua konfigurasi fundamental didefinisikan. Di dalam berkas ini, pengembang mendaftarkan semua aplikasi yang aktif melalui INSTALLED_APPS, mengatur koneksi ke database dalam DATABASES, menyimpan kunci keamanan esensial seperti SECRET_KEY, dan mengontrol mode pengembangan dengan DEBUG. Secara esensial, berkas ini adalah "konstitusi" proyek yang menentukan bagaimana semua bagian dari aplikasi saling terhubung dan beroperasi, menjadikannya fondasi bagi seluruh fungsionalitas dan keamanan aplikasi.

4. Cara kerja migrasi database di Django adalah proses dua langkah yang terstruktur untuk mengubah skema database sesuai dengan perubahan pada models.py. Pertama, perintah makemigrations akan mendeteksi perubahan pada model dan secara otomatis membuat sebuah berkas migrasi yang berisi kode dalam Python. Kemudian, perintah migrate akan membaca kode tersebut, menerjemahkannya menjadi perintah SQL yang sesuai, dan mengeksekusinya untuk menerapkan perubahan—seperti membuat atau mengubah tabel—pada database secara aman dan terlacak.

5. Menurut saya, Django adalah framework permulaan yang ideal karena Django menyediakan semua fitur esensial seperti admin panel dan sistem autentikasi secara bawaan. Strukturnya yang terarah dengan pola Model-View-Template (MVT) juga membimbing pemula untuk menulis kode yang terorganisir, sementara ORM-nya menyederhanakan interaksi database tanpa perlu SQL mentah dan fitur keamanannya melindungi dari ancaman umum. Kombinasi ini memungkinkan pemula untuk fokus pada logika aplikasi dan membangun proyek yang fungsional dengan cepat sambil mempelajari praktik terbaik dalam pengembangan perangkat lunak.

6. Tidak ada, asdos bekerja dengan sangat baik dan melayani semua permintaan mahasiswa dengan baik.