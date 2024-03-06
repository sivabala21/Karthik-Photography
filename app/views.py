from django.shortcuts import render

# Create your views here.

def home(request):

    return render(request,"home.html")


def portraits(request):
    
    return render(request,"products/portraits.html")



def book(request):
    
    return render(request,"book.html")


def about(request):
    
    return render(request,"about.html")


def bride(request):
    return render(request,"products/wedding.html")

