from django.shortcuts import render
from mywatchlist.models import MyWatchlistItem
from django.http import HttpResponse
from django.core import serializers


# TODO: Create your views here.
def show_html(request):
    return render(request, "mywatchlist.html", context)

data_watchlist = MyWatchlistItem.objects.all()
context = {
    'list_data': data_watchlist,
    'nama': 'Taqiya Zayin Hanafie',
    'id' : '2106751335'
}
def show_xml(request):
    data = MyWatchlistItem.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = MyWatchlistItem.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")


