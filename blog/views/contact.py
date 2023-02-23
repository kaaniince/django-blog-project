from django.shortcuts import render

def contact(request):
    context={
        'key':'baslik icerik naber'
    }
    return render(request,'pages/contact.html',context=context)