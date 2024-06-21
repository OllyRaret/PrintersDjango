from django.shortcuts import render

def contact(request):
    return render(request, 'contact/contact.html')

def contact_about(request):
    return render(request, 'contact/about.html')