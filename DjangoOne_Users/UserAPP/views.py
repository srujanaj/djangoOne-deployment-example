from django.shortcuts import render
from UserAPP.models import User
from .import forms, loginform
#Login imports
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate,login,logout
# Create your views here.

def index(request):
    context_dict = {'text':'hello world','number':100}
    return render(request,'UserAPP/index.html',context=context_dict)

@login_required
def special(request):
    return HttpResponse("You are Logged in, Nice!")

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def users(request):
    users_list = User.objects.order_by('FirstName')
    userslist = {'list':users_list}
    return render(request,'UserAPP/userlist.html',context = userslist)

def signup(request):
    form= forms.UserForm()

    if request.method == 'POST':
        form=forms.UserForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return users(request)
        else:
            print("Form invalid!")

    return render(request,'UserAPP/signup.html',{'form':form})

def register(request):

    registered=False

    if request.method == 'POST':

        user_form=loginform.UserForm(data=request.POST)
        profile_form = loginform.UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():

            user=user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user=user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered=True

        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form= loginform.UserForm()
        profile_form = loginform.UserProfileForm()

    return render(request,'UserAPP/registration.html',{'user_form':user_form,'profile_form':profile_form,'registered':registered})

def user_login(request):

    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Account Not active")
        else:
            print("Login Failed !")
            print("Username: {} and Password: {}".format(username,password))
            return HttpResponse("Invalid Login Details !")

    else:
        return render(request,'UserAPP/login.html', {})
