from django.shortcuts import render
from dashboard.forms import FormBarang
from dashboard.models import Barang
from django.contrib import messages
from django.shortcuts import render,redirect

# Create your views here.
def ubah_brg(request,id_barang):
    barangs=Barang.objects.get(id=id_barang)
    if request.POST:
        form=FormBarang(request.POST,instance=barangs)
        if form.is_valid():
            form.save()
            messages.success(request,"Data Berhasil diubah")
            return redirect('ubah_brg',id_barang=id_barang)
    else:
        form=FormBarang(instance=barangs)
        konteks = {
            'form' :form,
            'barangs' :barangs
        }
    return render(request,'ubah_brg.html',konteks)


def tambah_barang(request):
    if request.POST:
        form= FormBarang(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Data Berhasil Ditambahkan")
            form=FormBarang()
            konteks = {
                'form' : form,
            }
            return render(request,'tambah_barang.html',konteks)
    else:
        form=FormBarang()
        konteks = {
            'form':form,
        }
    return render(request,'tambah_barang.html',konteks)
    
def produk(request):
    titlenya="Produk"
    konteks = {
        'title':titlenya,
    }
    return render(request,'produk.html',konteks)

def Barang_View(request):
    barangs=Barang.objects.all()

    konteks={
        'barangs' :barangs,
    }
    return render(request,'tampil_brg.html',konteks)