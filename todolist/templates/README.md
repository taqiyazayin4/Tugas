# Tugas 5 PBP 
## Nama : Taqiya Zayin Hanafie 
## NPM : 2106751335 
### Link Aplikasi Heroku: https://tugas2-pbp-taqiya.herokuapp.com/todolist/

#### Apa perbedaan dari Inline, Internal, dan External CSS? Apa saja kelebihan dan kekurangan dari masing-masing style?
Inline, Internal, dan External CSS adalah metode menambahkan CSS ke file HTML.
a. Inline <br />
Kode ditulis pada atribut elemen HTML secara langsung dengan kelebihan mudah untuk melakukan modifikasi dan memiliki proses HTTPRequest yang lebih kecil. Inline memiliki kekurangan dalam sisi efiensi dan struktur ketika menggunakan styling sebab pengimplementasian harus dilakukan pada tiap elemen.<br />

b. Internal <br />
Kode ditulis dalam tag <style> pada tag <head>. Kelebihannya yaitu tidak memerlukan file CSS terpisah dengan mengimplementasikan tag sehingga lebih mudah untuk menyusun tampilan. Kekurangannya perlu membuat beberapa tag pada file-file jika menggunakan CSS yang sama. Selain itu, proses load pada website lebih lambat.<br />

c. External <br />
Kode ditulis secara terpisah pada file dengan ekstensi .css dan berisi properti style dengan mengimplementasikan tag atribut. Kelebihannya, memiliki struktur file yang baik karena properti berada pada file terpisah. Akan tetapi, style pada external akan di-override apabila terdapat inline dan internal. Apabila file gagal untuk dipanggil, halaman yang ditampilkan akan menjadi berantakan.<br />

#### Apa Jelaskan tag HTML5 yang kamu ketahui.
`<h1> hingga <h6>`: Heading HTML <br />
`<a>` : Mendefinisikan Hyperlink <br />
`<b>`: Membuat bold <br />
`<body>` : Mendefinisikan bagian body pada suatu dokumen <br />
`<br>` : Menghasilkan line break tunggal<br />
`<button>` : Membuat tombol <br />
`<div>` : Menunjukan suatu bagian dalam dokumen <br />
`<form>` : Mendefinisikan form HTML <br />
`<head>` : Mendefinsikan suatu head dokumen <br />
`<header>` : Header suatu bagian bagian <br />
`<html>` : Root dari dokumen HTML <br />
`<img>` : Menunjukan suatu gambar <br />
`<input>` : Mendefiniskan suatu kontrol input <br />
`<li>` : Mendefiniskan suatu list <br />
`<p>` : Mendefinisikan suatu paragraf <br />
`<ul>` : Mendefinisikan suatu daftar tak terurur <br />

#### Apa Jelaskan tipe-tipe CSS selector yang kamu ketahui.
Terdapat element selector yang memanfaatkan tag HTML sebagai selector tanpa diawali # maupun titik. Selain itu, ada ID selector yang memanfaatkan ID pada tag sebagai selector dengan diawali #. Class selector memanfaatkan Class pada tag sebagai selector dengan diawali titik.

#### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
1. Kustomisasi templat HTML dengan bootstrap. Saya membuat tampilan pada halaman login, register, create-task, dan todolist. todolist dibuat dengan mengimplementasikan cards sehingga tiap penambahan task akan menampilkan  satu card dengan task tunggal.
2. Membuat keempat halaman yang dikustomisasi menjadi responsive dengan memanfaatkan media query. Saya menambahkan fitur hover untuk membuat halaman lebih menarik.