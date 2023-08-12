from django.shortcuts import render, redirect, HttpResponse
from datetime import date
from .models import *

# Create your views here.


def home(request):
    
    return render(request, "home.html")



def registration(request):
    if request.method == "POST":
        id = request.POST.get("id")
        name = request.POST.get("name")
        userId = request.POST.get("userId")
        password = request.POST.get("password")
        dob = request.POST.get("dob")
        c = dob[ :4:]
        d = int(c)
        e = date.today().year
        r = e - d
        print("r = ",r)
        print(type(r))

        if r >= 18:
            print("you are eligible")
            mobile = request.POST.get("mobile")
        
            reg = Registration()
            existing_registration = Registration.objects.filter(
                id=id, userId=userId, passw=password, mobile=mobile
            ).first()

            if existing_registration:
                print("Duplicate record not allowed")
                msg = "Duplicate record not allowed"
        
                return render(request, "registration.html", {"msg": msg})
           
           
            else:
                reg.id = id
                reg.name = name
                reg.userId = userId
                reg.passw = password
                reg.dob = r
                reg.mobile = mobile
                reg.save()
                msg = 'Welcome You  are eligible'
                return render(request, "home.html", {"msg":msg})
        else:
            print("you are not eligible")
            msg = "you are not eligible"
            return render(request, "registration.html", {"msg":msg}, method="GET")

    else:
        return render(request, "registration.html")




def userLogin(request):
    if request.method == "POST":    
        userId = request.POST.get("userId")
        password = request.POST.get("password")        
        reg = Registration.objects.all()

        print(userId)
        print(password)
        print("=======================================")
      

        for i in reg:


            if userId == i.userId and password == i.passw:
                print("same")
                msg = 'Welcome...'
                return render(request, "vote.html", {"userId":userId})
            
            elif userId != i.userId and password != i.passw:
                continue        
        else:
            msg = 'Please enter correct  USERID and PASSWORD'
            return render(request, "userLogin.html", {"msg":msg})   
    else:
        return render(request, "userLogin.html")





def vote(request):
    if request.method == "POST":
        try:
            userId = request.POST.get("userId")
            can1 = request.POST.get("candidate")
            print(userId)
            print(can1)
            v1 = Vote()
            v1.userId = userId
            v1.candidate_politicalparties = can1
            v1.save()
            return redirect('/')
        except Exception as e:
            print(e)
            msg = "You have already Voted"
            return render(request, "userLogin.html", {"msg":msg})
    
    else:
    
        return render(request, "vote.html")


def admin(request):
    if request.method == "POST": 
        userId = request.POST.get("userId")
        password = request.POST.get("password")
        
        admi = Admin2.objects.all()

        print(userId)
        print(password)
        print("=======================================")

        for i in admi:
            if userId == i.userId and password == i.passw:
                print("same")
                msg = 'Welcome...'
                return redirect('/result')
                
            elif userId != i.userId and password != i.passw:
                continue

        else:
            msg = 'Please enter correct  USERID and PASSWORD'
            return render(request, "adminLogin.html", {"msg":msg})
        
    else:
        return render(request, "adminLogin.html")

            
        

def result(request):
    candidate1 = Vote.objects.filter(candidate_politicalparties = "BJP").count()
    candidate2 = Vote.objects.filter(candidate_politicalparties = "BSP").count()
    candidate3 = Vote.objects.filter(candidate_politicalparties = "AAP").count()
    candidate4 = Vote.objects.filter(candidate_politicalparties = "INC").count()
    
    data1 = Vote.objects.all()
    return render(request, "result.html",{"key":data1,"candidate1":candidate1, "candidate2":candidate2,"candidate3":candidate3,"candidate4":candidate4})



def createAdmin(request):
    if request.method == "POST":
        
        id = request.POST.get("id")
        name = request.POST.get("name")
        userId = request.POST.get("userId")
        password = request.POST.get("password")
        
        mobile = request.POST.get("mobile")
    
        reg = Admin2()
        reg.id = id
        reg.name = name
        reg.userId = userId
        reg.passw = password
        
        reg.mobile = mobile
        reg.save()
        msg = 'Welcome Admin'
        return redirect('/result')

    else:
        return render(request, "admin.html")



