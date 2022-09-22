# TODO: Implement Routings Here

from django.urls import path
from mywatchlist.views import show_xml #sesuaikan dengan nama fungsi yang dibuat
from mywatchlist.views import show_json #sesuaikan dengan nama fungsi yang dibuat
from mywatchlist.views import show_html


app_name = 'mywatchlist'

urlpatterns = [
    path('', show_html, name='show_html'),
    path('xml/', show_xml, name='show_xml'), #sesuaikan dengan nama fungsi yang dibuat
    path('json/', show_json, name='show_json'),
    path('html/', show_html, name='show_html'),
    
]