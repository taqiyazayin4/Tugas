from django.urls import path
from todolist.views import show_todolist
from todolist.views import register #sesuaikan dengan nama fungsi yang dibuat
from todolist.views import login_user
from todolist.views import logout_user 
from todolist.views import creating_new_task
from todolist.views import update_status
from todolist.views import remove_task

app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('register/', register, name='register'), 
    path('login/', login_user, name='login'), 
    path('logout/', logout_user, name='logout'), 
    path('creating-new-task/', creating_new_task, name='creating_new_task'), 
    path('update-status/<int:id>', update_status, name='update_status'),
    path('remove-task/<int:id>', remove_task, name='remove_task'), 
]