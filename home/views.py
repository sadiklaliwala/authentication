from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout,login
# adminusername =admin password=admin
# username1=laliwalasadik password=sadikking2004
# username2=sheikh_sohel123456 password=sadikking2004
# Create your views here.
def index(request):
    if request.user:
        return render(request,'index.html')
    return render(request, 'login.html')
        
    # return render(request , 'index.html')
def login(request):
    if request.method =="POST":
        #check user credentials
        username=request.POST.get('username')
        password=request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not  None:
            login(request,user)
            return redirect("/index.html")
        else:
            return redirect("/login.html")

    # A backend authenticated the credentials
            
    # No backend authenticated the credentials

    return render(request , 'login.html')
def logoutuser(request):
    logout(request)
    return render(request , 'login.html')