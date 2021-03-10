from django.shortcuts import render, redirect
from .models import Data
from .partials.forms import FormFiled

def index(request):
    data = Data.objects.all()
    form = FormFiled(request.POST or None)
    send = {
    'img': '/data/img/anime.jpg',
    'data': data,
    'form' : form,
    }
    return render(request, 'data/data.html', send)

def singleData(request, inputdata):
    data = Data.objects.get(id=inputdata)

    profile = {
    'profile' : data,
    }
    return render(request, 'data/profile.html', profile)

def delete(request, inputdelete):
    Data.objects.filter(id=inputdelete).delete()
    return redirect('kembalidata')

def edit(request):
    if request.method == 'POST':
        edit = Data.objects.get(id=request.POST['idedit'])
        edit.nama = request.POST['namaedit']
        edit.nim = request.POST['nimedit']
        edit.alamat = request.POST['alamatedit']
        edit.status = request.POST['statusedit']
        edit.save()
        return redirect('kembalidata')
    else:
        return redirect('kembalidata')

def create(request):
    form = FormFiled(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('kembalidata')
