from django.shortcuts import redirect,render
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def home_view(request):
    return render(request, "iplapp/home.html")


def signup_view(request):
    if request.method == "POST":
        print(request.POST)
        uname = request.POST.get("un")
        pwd = request.POST.get("pwd")
        email = request.POST.get("email")
        print(uname,pwd,email)
        
        # restrikstion lgana   user name alredy hai to -User alredy exists- ye smg retun dega
        if(User.objects.filter(username=uname).exists()):
            return render(request,"iplapp/signup.html", {'err':"User alredy exists"})
        else:
            User.objects.create_user(username=uname, email=email, password=pwd)
            return redirect("/login/")
        
    return render(request, "iplapp/signup.html")




def login_view(request):
    if request.method == "POST":
        un = request.POST.get("un")
        pwd = request.POST.get("pwd")
        
        user = authenticate(request, username=un, password=pwd)
        
        
        if user is None:
            return render(request, "iplapp/login.html",{'err': "Invalid Creaditionals"})
        else:
            login(request,user)
            return redirect("/create/")
        
    return render(request, "iplapp/login.html")









@login_required
def create_view(request):
    if request.method == "POST":
        print(request.POST)
        j = request.POST.get("jn")
        pn = request.POST.get("pn")
        rn = request.POST.get("rn")
        wk = request.POST.get("wk")
        tn = request.POST.get("tn")
        obj = Player(jno=j, pname=pn, runs=rn, wickets=wk, tname=tn)   # iske andar ke ye jno,pname .... ye model.py me jo hai wo hi dalna pdta hai
        obj.save()
        
        return redirect('/display/')
    
    return render(request, "iplapp/create.html")


@login_required
def display_view(request):
    
    ipldb = Player.objects.all()
    context = {"db": ipldb}
    return render(request, "iplapp/display.html", context)


@login_required
def update_view(request, n):
    obj = Player.objects.get(jno = n)
    context = {"p":obj}
    if(request.method == "POST"):
        obj = Player.objects.get(jno = n)
        print(request.POST)
#        u_j = request.POST.get("jn")
        u_pn = request.POST.get("pn")
        u_rn = request.POST.get("rn")
        u_wk = request.POST.get("wk")
        u_tn = request.POST.get("tn")
#        obj.jno = u_j
        obj.pname = u_pn
        obj.runs = u_rn
        obj.wickets = u_wk
        obj.tname = u_tn
        
        obj.save()
        return redirect('/display/')
    
    print("In update view", n)
    return render(request, "iplapp/update.html", context)



@login_required
def delete_view(request, n):
    print("In delete view", n)
    
    obj = Player.objects.get(jno = n)
    obj.delete()
    
    return redirect("/display/")
