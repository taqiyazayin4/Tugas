from django.urls import path
from todolist.views import *

app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('register/', register, name='register'), 
    path('login/', login_user, name='login'), 
    path('logout/', logout_user, name='logout'), 
    path('creating-new-task/', creating_new_task, name='creating_new_task'), 
    path('update-status/<int:id>', update_status, name='update_status'),
    path('delete/<int:id>', remove_task, name='remove_task'), 
    path('json/', ajax_get, name='ajax_get'),
    path('add/', ajax_post, name='ajax_post'),
]