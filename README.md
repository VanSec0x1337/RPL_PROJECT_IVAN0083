RPL PROJECT — SISTEM MANAJEMEN DATA MAHASISWA

<div align="center">

  <img src="https://readme-typing-svg.demolab.com?font=Orbitron&weight=900&size=42&duration=3000&pause=1000&color=10B981&center=true&vCenter=true&width=750&lines=RPL+PROJECT;Django+Mahasiswa;CRUD+Management;Responsive+Web+Application" alt="RPL Project" />

<br><br>

  <p style="color: #059669; font-size: 18px; font-weight: 600;">
    Sistem manajemen data mahasiswa berbasis Django dengan autentikasi, CRUD,
    validasi form, audio player, dan desain responsif.
  </p>

  <br>

  <a href="https://vansec1337.pythonanywhere.com/accounts/login/?next=/mahasiswa/">
    <img src="https://img.shields.io/badge/LIVE%20WEBSITE-10B981?style=for-the-badge&logo=django&logoColor=white" alt="Live Website">
  </a>

</div>

<div align="center">
  <h2 style="color: #10B981; font-weight: 700;">TENTANG PROJECT</h2>
</div>

RPL PROJECT adalah aplikasi web praktikum Rekayasa Perangkat Lunak (RPL) yangdibangun menggunakan Django. Aplikasi ini digunakan untuk mengelola datamahasiswa melalui sistem autentikasi dan operasi CRUD (Create, Read, Update,Delete).

Aplikasi menyediakan halaman login sebelum pengguna dapat mengakses sistemmanajemen mahasiswa. Setelah berhasil login, pengguna dapat melihat daftarmahasiswa, menambahkan data baru, mengedit data, menghapus data, sertamenggunakan fitur pendukung seperti audio player dan desain responsif.

🌐 Live Website:https://vansec1337.pythonanywhere.com/accounts/login/?next=/mahasiswa/

<div align="center">
  <h2 style="color: #10B981; font-weight: 700;">FITUR UNGGULAN</h2>
</div>

<table align="center">
<tr>
<td align="center" width="50%">

🔐 AUTENTIKASI

Login menggunakan sistem autentikasi Django sebelum mengakses halaman mahasiswa.

</td>
<td align="center" width="50%">

👨‍🎓 DATA MAHASISWA

Menampilkan daftar mahasiswa yang tersimpan di database.

</td>
</tr>

<tr>
<td align="center" width="50%">

➕ CREATE

Menambahkan data mahasiswa baru melalui form input.

</td>
<td align="center" width="50%">

✏️ UPDATE

Mengubah data mahasiswa yang sudah tersimpan.

</td>
</tr>

<tr>
<td align="center" width="50%">

🗑️ DELETE

Menghapus data mahasiswa dari sistem.

</td>
<td align="center" width="50%">

✅ VALIDASI FORM

Validasi input dengan pesan error yang mudah dipahami pengguna.

</td>
</tr>

<tr>
<td align="center" width="50%">

🎵 AUDIO PLAYER

Pemutar musik latar dengan kontrol play/pause.

</td>
<td align="center" width="50%">

📱 RESPONSIVE DESIGN

Tampilan dirancang agar dapat digunakan pada berbagai ukuran perangkat.

</td>
</tr>
</table>

<div align="center">
  <img src="https://readme-typing-svg.demolab.com?font=Rajdhani&weight=700&size=30&duration=3200&pause=1100&color=10B981&center=true&vCenter=true&width=650&lines=HALAMAN+APLIKASI" alt="Application Pages" />
</div>

Halaman

Fungsi

🔐 Login

Autentikasi pengguna sebelum masuk ke sistem

🏠 Halaman Utama

Halaman sambutan dan ringkasan aplikasi

👨‍🎓 Daftar Mahasiswa

Melihat seluruh data mahasiswa

➕ Tambah Mahasiswa

Menambahkan data mahasiswa

✏️ Edit Mahasiswa

Mengubah data mahasiswa

🗑️ Hapus Mahasiswa

Menghapus data mahasiswa

🚪 Logout

Keluar dari sistem dengan aman

<div align="center">
  <img src="https://readme-typing-svg.demolab.com?font=Rajdhani&weight=700&size=30&duration=3200&pause=1100&color=10B981&center=true&vCenter=true&width=650&lines=TEKNOLOGI+YANG+DIGUNAKAN" alt="Technology Stack" />
</div>

<div align="center">



</div>

Dependency

Project menggunakan beberapa package utama:

Django==5.1.2
gunicorn
whitenoise
dj-database-url
psycopg2-binary

<div align="center">
  <img src="https://readme-typing-svg.demolab.com?font=Rajdhani&weight=700&size=30&duration=3200&pause=1100&color=10B981&center=true&vCenter=true&width=650&lines=PREVIEW+WEBSITE" alt="Website Preview" />
</div>

<div align="center">

  <h3>🔐 Halaman Login</h3>

  <a href="https://cdn.corenexis.com/f/FskQ1KtYugg.png">
    <img src="https://cdn.corenexis.com/f/FskQ1KtYugg.png" alt="Preview Halaman Login RPL Project" width="850">
  </a>

<br><br>

  <p>
    <i>Tampilan awal halaman login sebelum pengguna masuk ke sistem.</i>
  </p>

</div>

<br>

<div align="center">

  <h3>📊 Dashboard / Halaman Utama</h3>

  <a href="https://cdn.corenexis.com/f/FPypwvKEImV.png">
    <img src="https://cdn.corenexis.com/f/FPypwvKEImV.png" alt="Preview Dashboard RPL Project" width="850">
  </a>

<br><br>

  <p>
    <i>Tampilan dashboard setelah pengguna berhasil melakukan login.</i>
  </p>

</div>

💡 Preview: Klik gambar untuk membuka screenshot dalam ukuran penuh.

<div align="center">
  <h2 style="color: #10B981; font-weight: 700;">MODEL DATA</h2>
</div>

Model utama yang digunakan adalah Mahasiswa dengan field:

Field

Tipe

Keterangan

nim

CharField

Nomor Induk Mahasiswa, maksimal 15 karakter dan unik

nama

CharField

Nama mahasiswa, maksimal 100 karakter

programstudi

CharField

Program studi, maksimal 50 karakter

<div align="center">
  <img src="https://readme-typing-svg.demolab.com?font=Rajdhani&weight=700&size=30&duration=3200&pause=1100&color=10B981&center=true&vCenter=true&width=650&lines=STRUKTUR+PROJECT" alt="Project Structure" />
</div>

RPL_PROJECT_IVAN0083/
│
├── accounts/
│   ├── templates/
│   │   └── accounts/
│   │       └── login.html
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── mahasiswa/
│   ├── migrations/
│   ├── static/
│   │   └── mahasiswa/
│   │       ├── audio/
│   │       │   └── music.mp3
│   │       ├── css/
│   │       │   └── style.css
│   │       ├── img/
│   │       │   └── bahlil.gif
│   │       └── js/
│   │           └── main.js
│   │
│   ├── templates/
│   │   └── mahasiswa/
│   │       ├── base.html
│   │       ├── index.html
│   │       ├── daftar.html
│   │       ├── tambah.html
│   │       └── edit.html
│   │
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── rpl_project/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── db.sqlite3
├── manage.py
├── requirements.txt
└── Procfile

<div align="center">
  <img src="https://readme-typing-svg.demolab.com?font=Rajdhani&weight=700&size=30&duration=3200&pause=1100&color=10B981&center=true&vCenter=true&width=650&lines=QUICK+START" alt="Quick Start" />
</div>

1. Clone Repository

git clone https://github.com/VanSec0x1337/RPL_PROJECT_IVAN0083.git
cd RPL_PROJECT_IVAN0083

2. Buat Virtual Environment

Windows:

python -m venv venv
venv\Scripts\activate

Linux / macOS:

python3 -m venv venv
source venv/bin/activate

3. Install Dependency

pip install -r requirements.txt

4. Jalankan Migration

python manage.py migrate

5. Buat User & Password Sendiri

Aplikasi tidak memerlukan akun bawaan dari pemilik project. Untuk mencobaaplikasi secara lokal, buat akun Django sendiri menggunakan perintah berikut:

python manage.py createsuperuser

Django akan meminta:

Username:
Email address:
Password:
Password (again):

Masukkan username dan password milik sendiri. Contoh:

Username: demo
Email address: demo@example.com
Password: ********
Password (again): ********

⚠️ Catatan: Jangan menggunakan atau membagikan username/password pribadimilik pemilik project. Setiap orang yang menjalankan project secara lokalsebaiknya membuat akun sendiri.

Setelah akun berhasil dibuat, jalankan server:

6. Jalankan Development Server

python manage.py runserver

Kemudian buka:

http://127.0.0.1:8000/accounts/login/

Login menggunakan username dan password yang baru saja dibuat.

Alternatif: Membuat User Biasa Tanpa Superuser

Jika hanya ingin membuat akun untuk login ke aplikasi tanpa akses admin,gunakan Django Shell:

python manage.py shell

Kemudian:

from django.contrib.auth.models import User

User.objects.create_user(
    username="demo",
    email="demo@example.com",
    password="PasswordDemo123!"
)

Keluar dari shell:

exit()

Setelah itu login menggunakan:

Username : demo
Password : PasswordDemo123!

Untuk project yang akan digunakan oleh banyak orang, jangan commitpassword asli ke repository. Contoh password di atas hanya untuk demonstrasilokal dan sebaiknya diganti dengan password sendiri.

Login ke Live Website

Live demo tersedia di:

https://vansec1337.pythonanywhere.com/accounts/login/?next=/mahasiswa/

Untuk live website, akun yang digunakan bergantung pada database deployment.README ini tidak menyediakan username/password pemilik project. Jika inginorang lain dapat mencoba live demo menggunakan akun masing-masing, aplikasiperlu menyediakan fitur registrasi atau admin perlu membuatkan akun padadatabase deployment.

<div align="center">
  <h2 style="color: #10B981; font-weight: 700;">ALUR PENGGUNAAN</h2>
</div>

┌───────────────────────┐
│       LOGIN PAGE      │
│  Username + Password  │
└───────────┬───────────┘
            │
            ▼
┌───────────────────────┐
│    HALAMAN UTAMA      │
│   Dashboard / Home    │
└───────────┬───────────┘
            │
            ▼
┌───────────────────────┐
│   DAFTAR MAHASISWA    │
│    View Data / CRUD   │
└───────┬───────┬───────┘
        │       │
        ▼       ▼
   ┌────────┐ ┌────────┐
   │ TAMBAH │ │  EDIT  │
   └────┬───┘ └────┬───┘
        │           │
        └─────┬─────┘
              ▼
       ┌──────────────┐
       │     DATA     │
       │   MAHASISWA  │
       └──────┬───────┘
              │
              ▼
         ┌─────────┐
         │ DELETE  │
         └─────────┘

<div align="center">
  <h2 style="color: #10B981; font-weight: 700;">KEAMANAN</h2>
</div>

Aplikasi menggunakan autentikasi Django untuk membatasi akses ke halamanmanajemen mahasiswa. View utama dilindungi dengan login_required, sehinggapengguna harus login terlebih dahulu sebelum mengakses fitur mahasiswa.

Sistem login menggunakan username + password dari Django Authentication.Akun dapat dibuat sendiri menggunakan createsuperuser atau melalui DjangoShell, sehingga pengguna tidak perlu menggunakan akun pribadi pemilik project.

Form POST juga menggunakan mekanisme CSRF protection bawaan Django.

<div align="center">
  <h2 style="color: #10B981; font-weight: 700;">LIVE DEMO</h2>

  <br>

  <a href="https://vansec1337.pythonanywhere.com/accounts/login/?next=/mahasiswa/">
    <img src="https://img.shields.io/badge/🚀%20BUKA%20WEBSITE-10B981?style=for-the-badge" alt="Open Website">
  </a>

<br><br>

  <p>
    <b>RPL Project — Django Student Management System</b>
  </p>
  <p>
    Dibuat untuk kebutuhan praktikum Rekayasa Perangkat Lunak.
  </p>

</div>

<div align="center">

👨‍💻 AUTHOR

Ivan Surya Buwana

NIM: G.211.24.0083Program Studi: Teknik Informatika

<br>



<br><br>

© 2026 RPL Project — Ivan Surya Buwana

</div>
