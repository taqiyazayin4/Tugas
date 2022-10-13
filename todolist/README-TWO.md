# Tugas 6 PBP 
## Nama : Taqiya Zayin Hanafie 
## NPM : 2106751335 
### Link Aplikasi Heroku: https://tugas2-pbp-taqiya.herokuapp.com/todolist/

#### Jelaskan perbedaan antara asynchronous programming dengan synchronous programming.

Asynchronous Programming<br />
Asynchronous Programming merupakan model programming yang dapat menjalankan lebih eksekusi setiap waktunya atau bersifat multi-thread. Asynchronous juga memiliki non-blocking yang berarti model dapat mengerjakam operasi-operasi secara tidak terurut. Asynchronous Programming digunakan untuk task yang bersifat independen.
<br />
Synchronous Programming<br />
Synchronous Programming merupakan model programming yang hanya dapat menjalankan satu eksekusi setiap waktunya atau bersifat single-thread. Synchronous juga memiliki sifat blocking yang berarti model ini akan mengerjakan operasi-operasi secara terurut dan hanya dapat mengirim satu request dalam satu waktu. Synchronous Programming digunakan untuk task yang bersifat dependen sehingga tidak memerlukan pengukuran alur proses dan lebih mudah digunakan. Akan tetapi, program yang dibuat akan berjalan lebih lambat.
<br />

#### Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma Event-Driven Programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.

Event-Driven Programming merupakan sebuah paradigma dengan alur program berdasarkan pada event yang dilakukan antara user dan client. Contoh dari event yang dapat diimplementasikan adalah seperti "onClick" dan "onSubmit". Contoh penerapan Event-Driven Programming pada tugas ini adalah sebagai berikut:

Menampilkan '#creating-new-task-modal' dan menghapus task

    ```js
    $('#open-button').click(() => {
      $('#creating-new-task-modal').removeClass('hidden')
     
    })
    $(`#delete-${task.id}`).click(() => {
            $.ajax({
              url: `/todolist/delete-${task.id}`,
              type: 'DELETE',
              credentials: 'include',
              dataType: 'json',
              success: () => $(`#task-${task.id}`).remove()
            })
          })
    ```
<br />

#### Jelaskan penerapan asynchronous programming pada AJAX.
Penerapan Asynchronous Programming pada AJAX seperti AJAX POST dan AJAX GET berfungsi pada pengiriman request user. Data yang ditangkap akan dikirimkan ke server tanpa  browser reload. Setelah request berhasil dikirimkan, akan muncul respon.

<br />

#### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
1. Saya membuat fungsi ajax_get(request) pada views.py untuk memperoleh data sdalam bentuk json. Lalu saya membuat path /todolist/json. Selanjutnya, saya melakukan pemanggilan task menggunakan AJAX GET.
2. Saya membuat creating-new-task-modal pada creating_new_task.html dan menghubungkan tombol Add Task dengan fungsi untuk memunculkan modal tersebut. Selanjutnya, saya membuat ajax_post(request) pada views.py untuk menambahkan task baru ke dalam database. Lalu saya membuat path /todolist/add untuk membuat task baru.
