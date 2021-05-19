from django.shortcuts import redirect, render
from .models import *

def index(request):
    context ={
        'dojos': Dojo.objects.all(),
    }
    return render(request, 'index.html', context)

def create_dojo(request):
    if request.method == 'POST':
        all_dojos = Dojo.objects.all()
        for dojo in all_dojos:
            if request.POST['name'] == dojo.name or request.POST['name'] == '':
                return redirect('/')
        Dojo.objects.create(name=request.POST['name'], city=request.POST['city'], state=request.POST['state'], desc='desc')
    return redirect('/')

def create_ninja(request):
    if request.method == 'POST':
        dojo = Dojo.objects.get(id=request.POST['dojo'])
        Ninja.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], dojo_id=dojo)
    return redirect('/')

def dojo_delete(request, dojo_id):
    dojo = Dojo.objects.get(id=dojo_id)
    dojo.delete()
    return redirect('/')