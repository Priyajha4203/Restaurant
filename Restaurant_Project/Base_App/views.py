from django.shortcuts import render
from django.http import HttpResponse
from Base_App.models import BookTable,AboutUs,Feedback,ItemList,Item

# Create your views here.

def HomeView(request):
    items=Item.objects.all()
    list=ItemList.objects.all()
    review=Feedback.objects.all()
    return render(request,"home.html",{'items' : items,'list' : list,'review' : review})

def AboutView(request):
    data=AboutUs.objects.all()
    return render(request,"about.html",{'data':data})

def MenuView(request):
    items=Item.objects.all()
    list=ItemList.objects.all()
    
    return render(request,"menu.html",{'items' : items,'list' : list})

def BookTableView(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        total_person=request.POST.get('total_person')       
        booking_data=request.POST.get('booking_data')
        
        if name!='' and email!='' and total_person!=0 and booking_data!='':
            data=BookTable(Name=name,Email=email,Phone_number=phone,Total_person=total_person,Booking_date=booking_data)
        data.save()
    return render(request,"book_table.html")

def FeedbackView(request):
    return render(request,"feedback.html")