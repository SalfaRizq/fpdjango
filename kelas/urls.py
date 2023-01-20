
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from django.shortcuts import render
from dashboard.views import produk
from dashboard.views import produk, tambah_barang, Barang_View
from dashboard.views import*

def coba1(request) :
    return HttpResponse('Selamat Datang')

def coba2(request) :
    titlenya="Home"
    konteks = {
        'title':titlenya,
    }
    return render(request,'index.html',konteks)

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('',coba1),
    path('',coba2),
    path('produk/',produk),
    path('addbrg/' , tambah_barang),
    path('Vbrg/' ,Barang_View),
    path('ubah/<int:id_barang>',ubah_brg,name='ubah_brg'),
]
