from django.shortcuts import render

def contact(request):
    context={'isim':'Kaan İnce'}
    return render(request,'pages/contact.html',context=context)