from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import Food
from .forms import FoodForm

# Create your views here.
def hview(request):

    return render(request,"food/home.html",{})

def fview(request):
    form = FoodForm()
    if request.method == 'POST':
        form = FoodForm(request.POST)
        form.save()
        return redirect('/a1/sv/')

    return render(request,"food/add_food.html",{"form":form})

def sview(request):

    return render(request,"food/show.html",{})