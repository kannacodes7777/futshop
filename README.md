**Pertanyaan Tugas 2**
1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
3. Jelaskan peran settings.py dalam proyek Django!
4. Bagaimana cara kerja migrasi database di Django?
5. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
6. Apakah ada feedback untuk asisten dosen tutorial 1 yang telah kamu kerjakan sebelumnya?

**Jawaban Tugas 2**
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

2. Berikut bagan yang diminta:
![Bagan request](/assets/Bagan_Request.png)

3. Berkas settings.py berfungsi sebagai pusat kendali utama untuk sebuah proyek Django, di mana semua konfigurasi fundamental didefinisikan. Di dalam berkas ini, pengembang mendaftarkan semua aplikasi yang aktif melalui INSTALLED_APPS, mengatur koneksi ke database dalam DATABASES, menyimpan kunci keamanan esensial seperti SECRET_KEY, dan mengontrol mode pengembangan dengan DEBUG. Secara esensial, berkas ini adalah "konstitusi" proyek yang menentukan bagaimana semua bagian dari aplikasi saling terhubung dan beroperasi, menjadikannya fondasi bagi seluruh fungsionalitas dan keamanan aplikasi.

4. Cara kerja migrasi database di Django adalah proses dua langkah yang terstruktur untuk mengubah skema database sesuai dengan perubahan pada models.py. Pertama, perintah makemigrations akan mendeteksi perubahan pada model dan secara otomatis membuat sebuah berkas migrasi yang berisi kode dalam Python. Kemudian, perintah migrate akan membaca kode tersebut, menerjemahkannya menjadi perintah SQL yang sesuai, dan mengeksekusinya untuk menerapkan perubahan—seperti membuat atau mengubah tabel—pada database secara aman dan terlacak.

5. Menurut saya, Django adalah framework permulaan yang ideal karena Django menyediakan semua fitur esensial seperti admin panel dan sistem autentikasi secara bawaan. Strukturnya yang terarah dengan pola Model-View-Template (MVT) juga membimbing pemula untuk menulis kode yang terorganisir, sementara ORM-nya menyederhanakan interaksi database tanpa perlu SQL mentah dan fitur keamanannya melindungi dari ancaman umum. Kombinasi ini memungkinkan pemula untuk fokus pada logika aplikasi dan membangun proyek yang fungsional dengan cepat sambil mempelajari praktik terbaik dalam pengembangan perangkat lunak.

6. Tidak ada, asdos bekerja dengan sangat baik dan melayani semua permintaan mahasiswa dengan baik.

<br>**Pertanyaan Tugas 3**

1. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
 
2. Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
 
3. Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?

4. Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
 
5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

6. Apakah ada feedback untuk asdos di tutorial 2 yang sudah kalian kerjakan?

**Jawaban Tugas 3**

1. Dalam pengimplementasian sebuah platform, kita membutuhkan data delivery agar sistem dapat mengalirkan data antar komponen secara efisien dan skalabel.
Sistem ini bertindak seperti roda berputar otomatis di dalam sistem pengelolaan data, yang memastikan:
   1. Tidak ada data yang hilang jika salah satu komponen sedang tidak aktif.
   2. Tidak terjadi antrean macet saat volume data tinggi, karena setiap komponen dapat bekerja sesuai kecepatannya.
   3. Platform tetap terasa cepat bagi pengguna, karena tugas-tugas berat dapat dikerjakan di latar belakang tanpa mengganggu alur utama.

2. Menurut saya, antara JSON dan XML, yang lebih baik untuk pengembangan web modern adalah JSON.
Alasan utamanya adalah JSON lebih mudah dibaca dan sintaksnya jauh lebih ringkas dibandingkan XML, yang berarti ukuran datanya lebih kecil dan performa aplikasi lebih cepat. Popularitasnya meroket karena kompatibilitasnya yang sempurna dengan JavaScript, bahasa utama di dunia web.
Selain itu, struktur JSON yang berbasis key-value memberikan tampilan yang lebih familiar bagi developer, karena sangat mirip dengan objek atau dictionary dalam bahasa pemrograman. Hal ini membuat proses parsing dan manipulasi data menjadi sangat intuitif.
Meskipun XML memiliki fungsionalitas yang lebih kompleks seperti skema (XSD) dan namespace untuk kebutuhan enterprise, kesederhanaan dan efisiensi JSON membuatnya lebih unggul untuk sebagian besar kasus penggunaan saat ini.

3. Fungsi dari method is_valid() adalah untuk memeriksa apakah semua data yang dikirimkan oleh pengguna melalui form sudah aman, valid, dan sesuai aturan sebelum diproses atau disimpan. Metode ini akan mengembalikan nilai True jika semua data valid, dan False jika ada yang tidak valid. Kita membutuhkan method ini untuk: 
   1. Keamanan data: method is_valid() akan memeriksa apakah data yang diberikan pengguna berbahaya, dan bertindak sebagai lapisan perlindungan pertama. 
   2. Integritas data: method is_valid() memastikan data yang disimpan ke database itu sudah sesuai standar yang diterapkan oleh model, misalnya tidak ada elemen kosong.
   3. Pengalaman pengguna: Apabila validasi gagal, maka website akan menampilkan secara otomatis mengenai apa yang salah, sehingga memudahkan pengguna untuk memperbaikinya.

4. Kita membutuhkan csrf_token untuk melindungi aplikasi dari serangan siber bernama Cross-Site Request Forgery (CSRF). Serangan ini menipu pengguna yang sedang login untuk tanpa sadar melakukan aksi yang tidak mereka inginkan di website kita. Tanpa token ini, website kita akan menjadi rentan diserang oleh penyerang siber. Penyerang dapat memanfaatkannya dengan menipu pengguna yang sedang login untuk tanpa sadar mengirimkan perintah ke situs website kita dari sebuah situs berbahaya. Dengan cara ini, penyerang bisa memaksa pengguna untuk mengubah email, password, menghapus data, atau melakukan aksi penting lainnya hanya dengan menipu mereka untuk mengunjungi sebuah halaman web.

5. Step-by-step cara mengimplementasikan cek-list diatas:
   1. Saya memulai dengan membuat file forms.py dan mendefinisikan ProductForm yang merupakan ModelForm dari model Product. Ini adalah fondasi untuk fitur tambah produk.
   2. Selanjutnya, saya mengimplementasikan semua logika di main/views.py:
      1. Menambahkan view add_product yang menangani request GET (menampilkan form kosong) dan POST (memvalidasi dan menyimpan data dari form).
      2. Membuat 4 view baru (show_xml, show_json, show_xml_by_id, show_json_by_id) yang menggunakan serializer Django untuk mengubah data produk menjadi format XML dan JSON.
   3. Kemudian saya mendaftarkan semua view baru tersebut di main/urls.py, memberikan setiap view sebuah path URL yang unik, seperti /add-product/, /xml/, dll.
   4. Saya lalu mengembangkan isi dari Template dengan:
      1. Membuat base.html sebagai kerangka utama yang berisi navbar dan struktur dasar.
      2. Membuat template add_product.html yang berisi tag <form> dengan {% csrf_token %} dan me-render form dari view.
      3. Memodifikasi products.html untuk menambahkan tombol "Add New Product" yang mengarah ke URL add_product dan tombol "Detail" pada setiap produk.
   5. Menambahkan beberapa styling di static/css/style.css untuk mempercantik tampilan halaman form dan tombol-tombol baru.
   6. Menguji semua fungsionalitas di local server menggunakan python manage.py runserver.
   7. Setelah semua berfungsi, saya menambahkan domain server PWS ke CSRF_TRUSTED_ORIGINS dan ALLOWED_HOSTS di settings.py sebagai persiapan deployment.
   8. Terakhir, saya melakukan git commit untuk menyimpan semua perubahan, lalu git push untuk mendeploy kode ke server PWS.

6. Tidak ada, semua berjalan dengan baik dan lancar. Mungkin kemarin saat ingin membuka XML dan JSON by id di Postman agak bingung karena tidak dijelaskan pada tutorial bahwa id dapat diliat di kolom XML atau JSON terkait. Selebihnya seluruhnya berjalan dengan baik dan lancar.

7. Untuk masing-masing bukti screenshootnya:
   1. ![Get JSON](/assets/Get_JSON.png)
   2. ![Get XML](/assets/Get_XML.png)
   3. ![Get JSON by Id](/assets/Get_JSON_ById.png)
   4. ![Get XML by Id](/assets/Get_XML_ById.png)