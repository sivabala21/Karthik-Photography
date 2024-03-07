from django.shortcuts import render
from django import forms
from django.http import HttpResponse
from django.urls import reverse
from .models import protraitPhoto,user,bridePhoto

# Create your views here.

#forms

class AppointmentForm(forms.Form):
    name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5'}))
    email = forms.EmailField(max_length=254, widget=forms.EmailInput(attrs={'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5'}))
    phoneno = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5'}))
    appointment_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5'}))



def home(request):

    return render(request,"home.html")




def book(request):
    if request.method == "POST":
        form=AppointmentForm(request.POST)
        if form.is_valid():
            sumbission=user.objects.create(name=form.cleaned_data['name'],
                                           email=form.cleaned_data['email'],
                                           phoneno=form.cleaned_data['phoneno'],
                                           appointment_date=form.cleaned_data['appointment_date'])

            print(sumbission)
            sumbission.save()
            return render(request,"book.html",{'form': form,'sumbited':True})
        
    else:
        form=AppointmentForm()
        return render(request,"book.html",{'form': form})


def about(request):
    
    return render(request,"about.html")


def bride(request):
    photo = bridePhoto.objects.all()

    # Pass photos to the template
    return render(request, 'products/bride.html', {'all_photos': photo})


def portraits(request):
    photo = protraitPhoto.objects.all()

    # Pass photos to the template
    return render(request, 'products/portraits.html', {'all_photos': photo})