from django.shortcuts import render, redirect
from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import login as auth_login, authenticate


from login.forms import SignupForm 

# Create your views here.
from django.http import HttpResponse 


# @csrf_protect
# def login(request):  
#    if request.method == 'POST':  
#          login = LoginForm(request.POST)
#          if login.is_valid():  
#             return HttpResponse("Logged In")
#          else:
#             return HttpResponse("Error while Logging in.")
#    else:
#       csrfContext = RequestContext(request)
#       login_form = LoginForm()
#       return render(request,'login.html',{'form': login_form},csrfContext)

@csrf_protect
def signup(request):
   csrfContext = RequestContext(request)  
   if request.method == 'POST':  
         signup = SignupForm(request.POST)
         if signup.is_valid(): 
            user = signup.save() 
            user.set_password(user.password)
            user.save()
            username = user.username
            raw_password = signup.cleaned_data.get('password')
            user = authenticate(username=username, password=raw_password)
            if user is not None:
               auth_login(request, user)
               return redirect('/show')
         
   signup_form = SignupForm()
   return render(request,'register.html',{'form': signup_form},csrfContext)

def home(request):
   return render(request,'home.html')