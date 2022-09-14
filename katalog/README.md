# TUGAS-2 PBP

### Nama : Taqiya Zayin Hanafie
### NPM  : 2106751335


**Link menuju aplikasi Heroku**
katalog: https://tugas2-pbp-taqiya.herokuapp.com/
example_app: https://tugas2-pbp-taqiya.herokuapp.com/example_app
 
**Bagan request client ke web aplikasi berbasis Django**
urls.py, views.py, models.py, dan berkas html memiliki kaitan sebagai komponen untuk memproses request client dan menghasilkan response. Berikut merupakan bagan request client ke web aplikasi berbasis Django sebagai berikut:
![This is an image](https://github.com/taqiyazayin4/Tugas/blob/main/katalog/flow1.jpeg)

**Jelaskan kenapa menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?**

Virtual environment merupakan sebuah alat untuk menciptakan environment yang terisolasi dari dependencies utama untuk menyimpan library hingga konfigurasi yang diinginkan. Hal ini sangat berguna ketika mengerjakan suatu proyek yang membutuhkan dependencies berbeda agar tercegah dari adanya error akibat perbedaaan versi hingga kompatibilitas. Selain itu, kita dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment dengan catatan, ketika sebuah aplikasi web melakukan penginstallan library maka akan disimpan secara global yang nantinya ketika akan ada update dari versi library yang digunakan maka aplikasi web tidak kompatibel karena tidak adanya virtual environmnent yang mengisolasi masing-masing modul.

**Jelaskan bagaimana cara kamu mengimplementasikan poin 1 sampai dengan 4 di atas.**
Pada poin pertama, saya mengimport render dari django.shortcuts untuk memproses data menjadi HTTPResponse dan mengimport CatalogItem dari katalog.models di views.py milik katalog. Untuk melakukan pengambilan data dari model, saya membuat fungsi show_katalog dengan parameter request pada views.py yang akan mereturn fungsi render(request, "katalog.html", context). katalog.html merupakan template httpresponse yang akan menampilkan output pada development server. context merupakan dictionaries yang terdiri dari keys seperti 'list_barang' dari models pada class CatalogItem,'nama', dan 'id'.

Pada poin kedua, saya mengimport path dari django.urls dan show_katalog dari katalog.views di urls.py milik katalog. Selanjutnya, saya membuat variabel app_name = 'katalog' dan membuat routing melalui list url_patterns pada urls.py dengan menambahkan path('', show_katalog, name='show_katalog'), untuk memetakan fungsi show_katalog pada views.py. Akan tetapi, kita harus menambahkan path('', include('katalog.urls')), terlebih dahulu pada list url_patterns urls.py miliki project_django sebelum urls.py milik katalog dapat diakses.

Pada poin ketiga, saya menjalankan perintah python manage.py loaddata initial_wishlist_data.json untuk memasukkan data pada file ke dalam database Django lokal. File initial_wishlist_data.json berisi data yang dapat dipetakan ke dalam HTML dengan syntax menyesuaikan dengan file katalog.html. Data tersebut tersimpan dalam CatalogItem yang diakses oleh dictionaries context pada keys 'list_barang' yang selanjutnya diproses menjadi bentuk html melalui pemanggilan return render(request, "katalog.html", context).

Pada poin keempat, saya melakukan add, commit, dan push perubahan yang telah saya lakukan dan disimpan ke dalam repository github saya. Saya membuat aplikasi pada heroku lalu menambahkan secret key berupa HEROKU_API_KEY dan HEROKU_APP_NAME. Selanjutnya, saya mengklik GitHub sebagai deployment method di heroku lalu menyambungkan repositori github saya ke heroku dan mendeploy secara otomatis sehingga aplikasi yang dibuat dapat dilihat. 

Referensi:
Django - Models. Retrieved 12 September 2022, from https://www.tutorialspoint.com/django/django_models.htm
Django Models. Retrieved 12 September 2022, from https://www.w3schools.com/django/django_models.php
Muhardian, A. (2017). Mengenal Virtualenv: Apa Saja yang Harus Kamu Ketahui?. Retrieved 12 September 2022, from https://www.petanikode.com/python-virtualenv/

