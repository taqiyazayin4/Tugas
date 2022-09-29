# TUGAS-3 PBP

### Nama        : Taqiya Zayin Hanafie
### NPM         : 2106751335
### Link Heroku : https://tugas2-pbp-taqiya.herokuapp.com/mywatchlist

1. 
|                 | JSON                                                            | XML                                 | HTML                      |   |
|-----------------|-----------------------------------------------------------------|-------------------------------------|---------------------------|---|
| Form            | JavaScript Object Notation berbasis JavaSript                   | Extensive Markup Language           | Hypertext markup language |   |
| Sifat Dokumen   |Self-describing sehingga mudah untuk dibaca              | Self-descriptive (Kode dapat merepresentasikan data yang ingin disampaikan)                                      | Mengandung data dan representasi data                      |   |
| Mendukung Array | Mendukung                                                       | Kurang Mendukung                    | Mendukung                 |   |
| Case sensitive      | Iya                              |Iya                        | Tidak        |   |
| Comment         | Tidak dapat mendukung comment                                   | Support comment                     | Support comment           |   |
| Encoding        | UTF-8 encoding                                                  | Mendukung berbagai variasi encoding | UTF-8 encoding            |   |
| Tipe Tag        | User Defined                                                    | User Defined                        | Predefined                |   |
| Root Element    | Tidak perlu                                                     |Perlu                                | Tidak perlu               |   |
| Data Storage    | Pada file JSON terpisah dalam bentuk key-value pairs dan arrays | Pada file XML terpisah              | Pada tag                  |   |
| Extension       | .json                                                           | .xml                                | .html                     |   |

2. Data delivery berfungsi untuk memanipulasi data antara dua format dan menampilkan data berdasarkan request dari client pada platform. Dengan demikian, data develiry memberikan kemudahan untuk menampilkan data dengan format file yang diinginkan client.

3. 
a. Pertama, saya menjalankan python manage.py startapp mywatchlist untuk membuat aplikasi mywatchlist.
b. Menambahkan path('', show_html, name='show_html'), pada url.py mywatchlist sehingga user dapat mengakses http://localhost:8000/mywatchlist
c. Membuat model di models.py mywatchlist yaitu sebagai berikut:
 ```shell
from django.db import models
class MyWatchlistItem(models.Model):
    title = models.CharField(max_length=255)
    review = models.TextField()
    watched = models.TextField()
    rating = models.IntegerField()
    release_date = models.DateField()
```
d. Saya menambahkan data untuk objek MyWatchList dengan komponen seperti contoh berikut: 
 ```shell
"model": "mywatchlist.mywatchlistitem",
        "pk": 1,
        "fields": {
            "title": "Siapa kamu?",
            "review": "Good",
            "watched": "Yes",
            "rating": 4,
            "release_date" : "2006-10-10"
```  
e. Pada views.py mywatchlist, saya membuat fungsi show_html(request), def show_xml(request), dan def show_json(request) untuk menyajikan data dalam format sesuai dengan request client.
f. Membuat routing dengan menambahkan path pada urls.py mywatchlist sebagai berikut:
 ```shell
    path('xml/', show_xml, name='show_xml'), 
    path('json/', show_json, name='show_json'),
    path('html/', show_html, name='show_html'),
  ```
  Maka dari itu, client dapat mengakses mywatchlist dengan format HTML, XML, dan JSON
g. Saya melakukan add, commit, dan push perubahan yang telah saya lakukan dan disimpan ke dalam repository github saya. Selanjutnya, saya mengklik GitHub sebagai deployment method di heroku lalu menyambungkan repositori github saya ke heroku dan mendeploy secara otomatis sehingga aplikasi yang dibuat dapat dilihat. 
4. Screenshot Postman
![HTML](https://github.com/taqiyazayin4/Tugas/blob/main/mywatchlist/Screen%20Shot%202022-09-22%20at%2010.42.59.png)
![JSON](https://github.com/taqiyazayin4/Tugas/blob/main/mywatchlist/Screen%20Shot%202022-09-22%20at%2008.03.34.png)
![XML](https://github.com/taqiyazayin4/Tugas/blob/main/mywatchlist/Screen%20Shot%202022-09-22%20at%2008.03.43.png)
5. Menambahkan unit test pada tests.py sebagai berikut:
 ```shell
from audioop import reverse
from urllib import response 
from django.test import TestCase, Client
from django.urls import resolve

class Test(TestCase):
    
    def test_xml(self):
        response = Client.get('/mywatchlist/xml/')
        self.assertEqual(response.status_code,200)
    def test_json(self):
        response = Client.get('/mywatchlist/json/')
        self.assertEqual(response.status_code,200)
    def test_html(self):
        response = Client.get('/mywatchlist/html/')
        self.assertEqual(response.status_code,200)
   
Sumber referensi:
https://www.geeksforgeeks.org/difference-between-json-and-xml/
https://bsharptech.com.au/html-vs-json-whats-the-difference/#:~:text=HTML%20is%20a%20relatively%20simple,for%20data%20storage%20and%20transfer.
