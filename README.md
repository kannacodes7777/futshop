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


**Pertanyaan Tugas 4**

1. Apa itu Django AuthenticationForm? Jelaskan juga kelebihan dan kekurangannya.
2. Apa perbedaan antara autentikasi dan otorisasi? Bagaiamana Django mengimplementasikan kedua konsep tersebut?
3. Apa saja kelebihan dan kekurangan session dan cookies dalam konteks menyimpan state di aplikasi web?
4. Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai? Bagaimana Django menangani hal tersebut?
5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).


**Jawaban Tugas 4**

1. Django AuthenticationForm adalah sebuah kelas Form bawaan dari Django (django.contrib.auth.forms) yang dirancang khusus untuk satu tugas: mengautentikasi pengguna. Form ini secara default meminta dua input: username dan password.
Fungsi utamanya adalah memvalidasi kredensial yang dimasukkan oleh pengguna. Ketika Anda memanggil form.is_valid(), AuthenticationForm akan melakukan beberapa pemeriksaan:
   1. Apakah username dan password diisi?
   2. Apakah ada pengguna dengan username tersebut di database?
   3. Apakah password yang dimasukkan cocok dengan password pengguna tersebut?
   4. Apakah akun pengguna tersebut aktif (is_active flag)?
   Jika semua validasi berhasil, kita bisa mendapatkan objek user yang terautentikasi dengan memanggil form.get_user().
   
   Kelebihan:

   a. Keamanan Bawaan: Sudah teruji dan menangani berbagai aspek keamanan secara otomatis, seperti proteksi terhadap timing attacks.

   b. Validasi Lengkap: Melakukan semua validasi yang diperlukan untuk login dalam satu panggilan .is_valid().

   c. Terintegrasi: Bekerja mulus dengan sistem autentikasi Django lainnya seperti fungsi login() dan authenticate().
   
   Kekurangan:

   a. Kurang Fleksibel: Secara default hanya menerima username.

   b. Tampilan Standar: Tampilan HTML yang dihasilkan standar.

2. Dalam sistem keamanan web, Autentikasi adalah proses verifikasi identitas pengguna, yang biasanya dimulai saat seseorang memasukkan data sensitif seperti username dan password untuk dicocokkan dengan yang ada di database. Untuk memastikan keamanan tingkat lanjut, proses ini seringkali diikuti oleh tahap verifikasi kedua, sebuah konsep yang yang dikenal sebagai Autentikasi Multi-Faktor (MFA), di mana sistem mengkonfirmasi kebenaran identitas pengguna melalui perangkat terdaftar atau email. Langkah tambahan ini memastikan bahwa meskipun kredensial utama dicuri, akses tidak sah tetap dapat dicegah. Setelah identitas pengguna berhasil diverifikasi sepenuhnya melalui proses autentikasi ini, barulah Otorisasi berperan, yaitu proses di mana sistem menentukan izin atau hak akses yang dimiliki oleh pengguna yang sudah terverifikasi tersebut, seperti apakah ia boleh mengakses data sensitif atau hanya halaman publik.

3. Kelebihan dan kekurangan cookies dan session:

   a. Cookies
      Kelebihan: Server tidak perlu menyimpan data, sehingga mengurangi beban. Ini bagus untuk skalabilitas.
      Kekurangan: Tidak aman untuk data sensitif karena disimpan di sisi klien dan bisa dibaca/diubah. Ukurannya sangat terbatas (sekitar 4KB).

   b. Session
      Kelebihan: Jauh lebih aman karena data sensitif tetap berada di server. Tidak ada batasan ukuran praktis.
      Kekurangan: Membutuhkan sumber daya (penyimpanan dan proses) di server untuk setiap pengguna aktif.

4a. Secara umum, penggunaan cookies tidak aman untuk secara default dalam pengembangan web. Hal ini disebabkan beberapa kekurangan cookie yang dapat dimanfaatkan oknum jahat:

   a. Pencurian (Hijacking): Jika tidak melalui koneksi HTTPS, pihak ketiga bisa "menguping" dan mencuri cookie.

   b. XSS (Cross-Site Scripting): Penyerang bisa menyuntikkan skrip di browser pengguna untuk mencuri cookie.

   c. CSRF (Cross-Site Request Forgery): Penyerang menipu pengguna untuk melakukan tindakan di situs lain saat pengguna sedang login.

4b. Cara Django menangani risiko tersebut adalah dengan menyediakan fitur-fitur keamanan sebagai berikut:

   a. CSRF Protection: Django memiliki perlindungan CSRF yang aktif secara default. Token {% csrf_token %} di dalam form memastikan bahwa request POST hanya datang dari situs kita sendiri, bukan dari situs lain.

   b. HttpOnly Cookies: Django secara default mengatur session cookie sebagai HttpOnly. Ini berarti cookie tersebut tidak bisa diakses oleh JavaScript di sisi browser, yang secara drastis mengurangi risiko pencurian cookie melalui serangan XSS.

   c. Signed Cookies: Session ID yang disimpan di cookie ditandatangani secara kriptografis. Jika pengguna mencoba mengubah Session ID di cookie mereka, tanda tangannya tidak akan cocok, dan Django akan menolak sesi tersebut.

   d. Opsi Secure: Django menyediakan pengaturan (SESSION_COOKIE_SECURE = True) yang memastikan cookie hanya dikirim melalui koneksi HTTPS, mencegah pengupingan.


5.  Implementasi Step-by-Step (Sesuai Checklist)
   
      a. Menghubungkan Model Product dengan User:

         1. Langkah pertama dan paling fundamental adalah mengedit main/models.py.
         2. Saya kemudian menambahkan user = models.ForeignKey(User, on_delete=models.CASCADE) ke dalam model Product. Ini menciptakan hubungan di mana setiap produk dimiliki oleh satu pengguna.
         3. Setelah mengubah model, saya menjalankan python manage.py makemigrations untuk membuat file migrasi dan python manage.py migrate untuk menerapkan perubahan ini ke database.

   b. Mengimplementasikan Registrasi, Login, dan Logout:
   
      1. Saya membuat tiga URL di urls.py untuk /register, /login, dan /logout yang menunjuk ke tiga view baru.

      2. Pada views.py, saya membuat register, login_user, dan logout_user.

      3. Untuk halaman yang memerlukan login (seperti halaman utama), saya menambahkan decorator @login_required di atas fungsi view show_main.

   c. Menampilkan Username: Di base.html, saya menambahkan blok {% if user.is_authenticated %} di dalam navbar. Di dalamnya, saya menampilkan {{ user.username }}.

   d. Implementasi Cookies:
   
      1. Di view login_user, setelah login(request, user) berhasil, saya membuat respons redirect.
      2. Saya mengatur cookie pada respons tersebut: response.set_cookie('last_login', formatted_time).
      3. Di view logout_user, saya menghapus cookie: response.delete_cookie('last_login').
      4. Untuk menampilkannya di header (base.html), cara terbaik adalah dengan Context Processor. Saya membuat file main/context_processors.py, membuat fungsi yang membaca request.COOKIES.get('last_login'), dan mendaftarkannya di settings.py. Ini membuat variabel cookie tersedia di semua template, sehingga saya bisa menampilkannya di base.html.

6. Menambahkan 2 user dan masing-masing user mempunyai 3 data dummy dengan bukti screenshoot:
   1. ![User1](/assets/User1.png)
   2. ![Get XML](/assets/User2.png)

**Pertanyaan Tugas 5**
1. Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!
2. Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design, serta jelaskan mengapa!
3. Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!
4. Jelaskan konsep flex box dan grid layout beserta kegunaannya!
5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!

**Jawaban Tugas 5**
1. Urutan prioritas CSS selector (dari tertinggi ke terendah):
   a. !important - Mengabaikan semua spesifisitas lain
   b. Inline styles (style="") - Spesifisitas 1000
   c. ID selector (#id) - Spesifisitas 100
   d. Class/Attribute/Pseudo-class (.class, [type], :hover) - Spesifisitas 10
   e. Element/Pseudo-element (div, ::before) - Spesifisitas 1
   f. Universal selector (*) - Spesifisitas 0

2. Responsive design menjadi konsep yang penting dalam pengembangan aplikasi web, karena beberapa hal:
   a. User Experience: Pengalaman konsisten di semua device
   b. Maintenance: Satu codebase untuk semua platform
   c. Market Reach: 60%+ traffic web berasal dari mobile
   Contoh aplikasi yang:
   a. Responsive: Google, Twitter, Instagram Web – tampilan menyesuaikan ukuran layar, navigasi tetap mudah diakses.
   b. Tidak responsive: Situs lama e-commerce yang hanya untuk desktop, menu dan gambar tidak menyesuaikan ukuran layar, sulit digunakan di mobile.

3. Perbedaan antara margin, border, dan padding adalah:
   a. Margin: Ruang di luar elemen, memisahkan elemen dengan elemen lain.
   b. Border: Garis di sekitar elemen. Bisa diatur warna, tebal, dan tipe garis.
   c. Padding: Ruang di dalam elemen, antara konten dengan border.
4. Konsep flexbox dan grid layout:
   a. Flexbox: digunakan untuk mengatur layout dalam satu dimensi (baris atau kolom). Berguna untuk membuat navbar, tombol, atau card yang sejajar dan mudah diatur jaraknya.
   b. Grid Layout: digunakan untuk layout dua dimensi (baris dan kolom). Berguna untuk halaman daftar produk, membuat card-product tersusun rapi.

5. Implementasi Checklist Step-by-Step
   a. Implementasikan fungsi untuk menghapus dan mengedit product
      1. Edit Product:
         1. Membuat edit_product.html yang menggunakan ProductForm dari Django untuk semua field sesuai model (name, price, description, thumbnail, category, stock, rating, brand, is_featured).
         2. Form ini sudah mengikat instance product, sehingga ketika user menekan Save Changes, data di-update secara otomatis.
         3. View edit_product menangani POST request dan melakukan redirect ke halaman detail product setelah berhasil disimpan.
      2. Delete Product:
         1. Membuat view delete_product yang menerima POST request.
         2. Pada product detail page, tombol delete memunculkan modal konfirmasi menggunakan JavaScript sebelum melakukan delete.
         3. Jika user menekan "Delete" di modal, product akan dihapus, dan user bisa di-redirect kembali sesuai kebutuhan (misal ke daftar product).
   b. Kustomisasi desain halaman menggunakan Tailwind CSS
      1. Halaman login & register: Membuat form dengan input field dan tombol bergaya modern (rounded corners, hover effect, spacing, fokus highlight).
      2. Halaman tambah product & edit product: Menggunakan form.as_p dengan styling Tailwind untuk form input, textarea, select, dan file upload. Tombol “Save Changes” dan “Cancel” diberi warna kontras (green untuk save, gray untuk cancel).
      3. Halaman detail product: Memisahkan bagian image dan info product menggunakan flex layout. Menambahkan tombol Edit dan Delete, dengan modal konfirmasi untuk delete. Responsive: layout menyesuaikan lebar layar menggunakan Tailwind flex-wrap dan min-w-[400px].
      4. Halaman daftar product (All Products): Jika tidak ada product, menampilkan pesan “Belum ada product yang terdaftar” dan placeholder image.Jika ada product, menggunakan card layout untuk menampilkan image, name, category, price, dan tombol “View Details”. Tombol edit & delete ditambahkan pada setiap card untuk user yang membuat product. Grid layout responsive menggunakan Tailwind flex-wrap dan gap antar card.
   c. Navbar yang responsive
      1. Desktop: Navbar horizontal dengan logo di kiri, link menu di kanan.
      2. Mobile: Navbar menyembunyikan menu, menampilkan tombol hamburger. Ketika tombol diklik, menu muncul di bawah secara vertikal. Menggunakan Tailwind classes seperti hidden, flex, md:flex untuk responsive control. Menambahkan animasi/transition untuk menu mobile agar lebih smooth.


# Pertanyaan Tugas 6
1.  Apa perbedaan antara synchronous request dan asynchronous request?
2. Bagaimana AJAX bekerja di Django (alur request–response)?
3. Apa keuntungan menggunakan AJAX dibandingkan render biasa di Django?
4. Bagaimana cara memastikan keamanan saat menggunakan AJAX untuk fitur Login dan Register di Django?
5. Bagaimana AJAX mempengaruhi pengalaman pengguna (User Experience) pada website?

# Jawaban Tugas 6
## 1. Perbedaan Synchronous dan Asynchronous
Synchronous Request (Sinkron) adalah permintaan yang memblokir. Saat sebuah permintaan dikirim, pengguna harus menunggu sampai server merespons dan halaman selesai dimuat ulang sebelum bisa melakukan hal lain.

Asynchronous Request (Asinkron) adalah permintaan yang tidak memblokir. Permintaan dikirim di latar belakang, dan pengguna bisa terus berinteraksi dengan halaman web tanpa harus menunggu. Saat respons dari server tiba, hanya bagian tertentu dari halaman yang diperbarui.

## 2. Alur Kerja AJAX di Django (alur request–response)
   a. AJAX (Asynchronous JavaScript and XML) di Django bekerja dengan memisahkan proses pengambilan data dari presentasi halaman.

   b. Aksi Pengguna: Pengguna melakukan sesuatu di halaman web, seperti menekan tombol "Like" atau mengisi form.

   c. JavaScript Mengirim Request: Sebuah fungsi JavaScript dipicu. Alih-alih me-refresh seluruh halaman, JavaScript menggunakan fetch() untuk mengirim permintaan HTTP (seperti GET atau POST) ke sebuah URL khusus di server Django.

   d. URL Django Merespons: urls.py di Django mencocokkan URL tersebut dengan sebuah view yang telah disiapkan untuk menangani permintaan AJAX.

   e. View Django Memproses: View tersebut melakukan logika yang diperlukan (misalnya, menyimpan data ke database, mengambil produk) tetapi tidak me-render template HTML.

   f. View Mengembalikan JSON: Sebagai gantinya, view mengembalikan data dalam format JSON (JavaScript Object Notation) menggunakan JsonResponse.

   g. JavaScript Menerima JSON: JavaScript di browser menerima data JSON ini.

   h. Update Halaman (DOM Manipulation): JavaScript kemudian menggunakan data tersebut untuk memperbarui bagian kecil dari halaman HTML secara langsung, tanpa perlu me-refresh.

## 3. Keuntungan Menggunakan AJAX
Menggunakan AJAX di Django memberikan beberapa keuntungan signifikan dibandingkan render biasa:

Pengalaman Pengguna Lebih Baik: Website terasa lebih cepat dan responsif karena tidak ada lagi layar putih saat menunggu halaman dimuat ulang. Interaksi terasa instan, mirip seperti menggunakan aplikasi desktop.

Mengurangi Beban Server & Bandwidth: Hanya data yang benar-benar dibutuhkan yang dikirim antara server dan browser, bukan seluruh halaman HTML. Ini membuat transfer data lebih efisien.

Interaktivitas yang Lebih Kaya: Memungkinkan pembuatan fitur-fitur modern seperti live search (hasil pencarian muncul saat mengetik), infinite scroll (konten baru dimuat saat menggulir ke bawah), dan notifikasi real-time.

## 4. Cara memastikan keamanan saat menggunakan AJAX untuk fitur Login dan Register di Django
Menggunakan CSRF (Cross-Site Request Forgery) Token: Ini adalah fitur keamanan terpenting. Setiap permintaan POST yang dikirim oleh AJAX wajib menyertakan CSRF token. JavaScript harus dikonfigurasi untuk membaca token dari halaman dan mengirimkannya dalam header permintaan. Ini memastikan bahwa permintaan tersebut sah dan berasal dari situs pengguna.

Validasi di Sisi Server: Jangan pernah mempercayai data dari pengguna. Semua data yang dikirim melalui AJAX (username, password, dll.) harus divalidasi di view Django menggunakan Django Forms (AuthenticationForm, UserCreationForm) sebelum diproses lebih lanjut. Ini mencegah injeksi data berbahaya.

Menggunakan HTTPS: Menggunakan HTTPS di server produksi agar semua komunikasi antara browser dan server terenkripsi, sehingga data sensitif seperti password tidak dapat disadap.

## 5. Pengaruh AJAX pada User Experience (UX)
AJAX secara dramatis meningkatkan pengalaman pengguna (UX) dengan cara berikut:

Kecepatan yang Terasa (Perceived Speed): Karena halaman tidak pernah memuat ulang sepenuhnya, website terasa jauh lebih cepat. Pengguna mendapatkan umpan balik instan atas tindakan mereka, yang membuat mereka merasa lebih memegang kendali.

Interaksi yang Mulus (Seamless Interaction): Memperbarui bagian-bagian kecil dari halaman menciptakan alur kerja yang tidak terputus. Pengguna tidak kehilangan konteks atau posisi mereka di halaman saat suatu aksi terjadi.

Mengurangi Gangguan: Pengguna dapat terus membaca atau berinteraksi dengan konten lain sementara aplikasi menyimpan data atau mengambil informasi baru di latar belakang. Ini menciptakan pengalaman yang lebih lancar dan tidak mengganggu.