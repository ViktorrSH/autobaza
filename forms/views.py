from django.shortcuts import render, render_to_response, redirect
from django.template.loader import get_template
# Create your views here.
from .models import car
from .forms import CarForm


def index(request):
    cars = car.objects.all()
    context = {'car': cars}
    return render(request, 'index.html', context)



def addcar(request):
    if request.method == 'POST':
        form = CarForm(request.POST)
        if form.is_valid():
            newcar = car(name=request.POST['name'], country=request.POST['country'])
            newcar.save()
            return redirect('/')
    else:
        form = CarForm


    context = {'form': form}
    return render(request, 'sign.html', context)







