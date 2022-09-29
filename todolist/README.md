# Tugas 4 PBP 
## Nama : Taqiya Zayin Hanafie 
## NPM : 2106751335 
### Link Aplikasi Heroku: https://tugas2-pbp-taqiya.herokuapp.com/todolist/

 #### Apa kegunaan {% csrf_token %} pada elemen <form>? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen <form>?
{% csrf_token %} adalah tag _random_ yang berfungsi untuk memproteksi Cross Site Request Forgery (CSRF) dari serangan. Setiap sesi pengguna. {% csrf_token %} memberikan token unik untuk proses request. Apabila terdapat request yang masuk, server akan mengecek kesesuaian token. Maka dari itu, jika token tidak sesuai/tidak ditemukan maka request tidak akan dijalankan. <br />

Apabila tidak ada {% csrf_token %} pada elemen <form> maka request yang masuk dapat dijalankan tanpa ada pengecekan token. Hal ini membuat server mudah untuk diserang.

 #### Apakah kita dapat membuat elemen <form> secara manual (tanpa menggunakan generator seperti {{ form.as_table }})? Jelaskan secara gambaran besar bagaimana cara membuat <form> secara manual.
kita dapat membuat elemen <form> secara manual, yaitu dengan membuat class form pada forms.py dan disesuaikan dengan models. Selanjutnya. buat fungsi untuk mengakses formnya pada file views.py dan file html sebagai template. Pada file html disisipkan tag <form> {{ form }} </form> pada lokasi yang disesuaikan atau menggunakan generator lainnya.

 #### Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.
User menginput data lalu mengklik tombol yang mengsubmit data tersebut. Browser akan meng-generate dan meneruskan HTTP Request dari html ke `views.py`. Data akan diolah dan akan dicek validitas dengan method is_valid. Setelah itu, data disimpan dalam database dengan method save()sehingga data dapat ditampilkan pada browser ketika html dipanggil.  <br />

 #### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
 1. Membuat aplikasi todolist dengan menjalankan perintah python manage.py startapp todolist
 2. Menambahkan path todolist dengan mencantumkan `path('todolist/', include('todolist.urls')), pada urlpatterns di urls.py project_django. Selain itu, mendaftarkan todolist pada bagian INSTALLED_APPS di settings.py project_django.
 3. Membuat sebuah model todolist pada models.py sebagai berikut:
```shell
    from django.db import models
    from django.contrib.auth.models import User

    class Task(models.Model):
        user = models.ForeignKey(User, on_delete=models.CASCADE)
        date = models.DateField(auto_now_add=True)
        title = models.CharField(max_length=255)
        description = models.TextField()
        is_finished = models.BooleanField(default = False)
```
4. implementasikan form registrasi, login, dan logout dengan membuat fungsi pada views.py sebagai berikut:

```shell
    def register(request):
        form = UserCreationForm()
        
        if request.method == "POST":
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Akun telah berhasil dibuat!')
                return redirect('todolist:login')
        
        context = {'form':form}
        return render(request, 'register.html', context)

    def login_user(request):
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('todolist:show_todolist')
            else:
                messages.info(request, 'Username atau Password salah!')
        context = {}
        return render(request, 'login.html', context)

    def logout_user(request):
        logout(request)
        return redirect('todolist:login')
```


5. Pada views.py todolist terdapat fungsi show_todolist yang berfungsi untuk me-render ke halaman utama sebagai berikut:
```shell
@login_required(login_url='/todolist/login/')
def show_todolist (request):
    data_todolist = Task.objects.filter(user=request.user)
    context = {
        'tasks' : data_todolist,
        'username': request.user.username,
    }

   
    return render(request, "todolist.html", context)
```
 Selanjutnya, saya membuat file todolist.html sebagai template untuk menampilkan data yang terdiri dari tabel berisi tanggal pembuatan, judul, dan deskripsi serta button.<br />
6. Pada forms.py todolist, terdapat class Form yang berfungsi untuk pengambilan data judul dan deskripsi. Pada views.py todolist terdapat fungsi creating_new_task sebagai berikut:
 ```shell @login_required(login_url='/todolist/login/')
def creating_new_task(request):
    form_task = Form()

    if request.method == 'POST':
        form_task = Form(request.POST)
        form_task.instance.user = request.user
        if form_task.is_valid():
            form_task.save()
            
            return redirect('todolist:show_todolist')
    context = {'form': form_task}
    return render(request, 'creating_new_task.html', context)
    ```
    Selanjutnya, saya membuat file creating_new_task.html pada folder templates untuk menampilkan halaman form untuk pembuatan task. Pada file tersebut, terdapat tag `<form>`, generator {{ form.as_table }}, tag `<table>`, dan button untuk menambah task. File html ini juga dipanggil oleh fungsi create_task sebagai handle views.py untuk request formnya. Detail codenya bisa dilihat di file create_task.html.<br />

7. Membuat routing dengan menambahkan path pada urlpatterns di urls.py todolist agar fungsi dapat diakses sebagai berikut:
```shell
urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('register/', register, name='register'), 
    path('login/', login_user, name='login'), 
    path('logout/', logout_user, name='logout'), 
    path('creating-new-task/', creating_new_task, name='creating_new_task'), 
    path('update-status/<int:id>', update_status, name='update_status'),
    path('remove-task/<int:id>', remove_task, name='remove_task'), 
]```

8. Saya melakukan add, commit, dan push perubahan yang telah saya lakukan dan disimpan ke dalam repository github saya. Selanjutnya, saya mengklik GitHub sebagai deployment method di heroku lalu menyambungkan repositori github saya ke heroku dan mendeploy secara otomatis sehingga aplikasi yang dibuat dapat dilihat. 

9. 
![UserA](https://github.com/taqiyazayin4/Tugas/blob/42f9ff1d45ab1eb4082cc0c93598f9d57fb2b972/todolist/Screen%20Shot%202022-09-29%20at%2009.13.06.png)
![UserB](https://github.com/taqiyazayin4/Tugas/blob/42f9ff1d45ab1eb4082cc0c93598f9d57fb2b972/todolist/Screen%20Shot%202022-09-29%20at%2009.15.45.png)


