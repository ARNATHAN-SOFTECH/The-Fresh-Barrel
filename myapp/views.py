from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def fish(request): 
    return render(request, "fish.html")

def poultry(request):
    return render(request,"poultry.html")

def mutton(request):
    return render(request,"mutton.html")

def faq(request):
    return render(request, 'faq.html')

def terms_conditions(request):
    return render(request, 'terms_conditions.html')

def blog(request):
    return render(request, 'blog.html')

def privacy_policy(request):
    return render(request, 'privacy_policy.html')

def refund_policy(request):
    return render(request, 'refund_policy.html')

def contact_us(request):
    return render(request, 'contact_us.html')