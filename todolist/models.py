from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    # Django mengemulasi perilaku batasan SQL ON DELETE CASCADE dan juga menghapus objek yang berisi ForeignKey
    # buat hubungan pada model yang belum ditentukan, Anda dapat menggunakan nama model
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    is_finished = models.BooleanField(default = False)
