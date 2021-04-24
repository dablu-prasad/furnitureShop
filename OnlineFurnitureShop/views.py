from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from OnlineFurnitureShop.models import Contact, CardDetail

price={'price':5000}

def home(request):
    
    return render(request,'home.html',price)

def contact(request):
     if request.method=='POST':
         name=request.POST['name']
         email=request.POST['email']
         phone=request.POST['phone']
         desc=request.POST['desc']
         ins=Contact(name=name,email=email,phone=phone,desc=desc)
         ins.save()

     return render(request,'contact.html')

def carddetail(request):
    if request.method=='POST':
        cardnumber = request.POST['cardnumber']
        cardholdername = request.POST['cardholdername']
        cvvnumber = request.POST['cvvnumber']
        expmonth = request.POST['expmonth']
        expyear = request.POST['expyear']
        det=CardDetail(cardnumber=cardnumber,cardholdername=cardholdername,cvvnumber=cvvnumber, expmonth=expmonth,expyear=expyear)
        det.save()
    return render(request,'carddetail.html',price)