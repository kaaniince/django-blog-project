from django.shortcuts import render



def homepage(request):
    
    context={
        'isim':'Kaan İnce'
    }
    return render(request,'pages/homepage.html',context=context)