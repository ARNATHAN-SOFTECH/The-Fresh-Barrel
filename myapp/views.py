from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def fish(request): 
    return render(request, "fish.html")

def poultry(request):
    return render(request,"poultry.html")

def mutton(request):
    return render(request,"mutton.html")