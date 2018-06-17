from django.shortcuts import render
from .models import Details,Expenses,SplitBill
from datetime import date

def Detail(request):
    return render(request, "details.html")

def Dinsert(request):
    name1 = request.POST['d2']
    email1 = request.POST['d3']
    mob1 = int(request.POST['d4'])
    addr1 = request.POST['d5']

    d = Details(name=name1,email=email1,phone=mob1,addr=addr1)
    d.save()

    details = Details.objects.all()

    return render(request,"links.html",{"details":details})

def Expense(request):
    return render(request,"expense.html")

def Einsert(request):
    income1=int(request.POST['e1'])
    house1=int(request.POST['e2'])
    utility1=int(request.POST['e3'])
    grocery1=int(request.POST['e4'])
    transport1=int(request.POST['e5'])
    health1=int(request.POST['e6'])
    entertain1=int(request.POST['e7'])
    debt1=int(request.POST['e8'])
    other1=int(request.POST['e9'])

    e=Expenses(income=income1,house=house1,utility=utility1,grocery=grocery1,transport=transport1,
               health=health1,entertainment=entertain1,
               debt=debt1,others=other1)
    e.save()

    expense=Expenses.objects.all()

    return render(request,'display_expense.html',{'expense':expense})



def Split(request):
    return render(request,"splitbill.html")

def Sinsert(request):
    fname1=request.POST['s1']
    fnum=int(request.POST['s2'])
    addr=request.POST['s3']
    amt1=int(request.POST['s4'])

    s=SplitBill(fname=fname1,pnum=fnum,addrs=addr,amt=amt1)
    s.save()

    return render(request,"links1.html")

def Sdisplay(request):
    bills=SplitBill.objects.all()

    return render(request,"display_bills.html",{"bills":bills})
