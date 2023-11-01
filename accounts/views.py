from django.shortcuts import render , redirect
from .forms import SignupForm , UserForm , ProfileForm 
from .models import Profile 
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login 
from gendr.models import All





def signup(request):
        if request.method == "POST":
            form=SignupForm(request.POST)
            if form.is_valid():
                form.save()
                try :
                    usernames = form.cleaned_data['username']
                    passwords = form.changed_data['password1']
                    user = authenticate(username=usernames,password=passwords)
                    login(request,user)

                    return redirect('/accounts/login')
                except :
                    return redirect('/accounts/login')
                
        else:
            form=SignupForm()

        return render(request,'registration/signup.html',{'form':form})


def profile(request):
    profile=Profile.objects.get(user=request.user)

    return render(request,'profile/profile.html',{'profile':profile})



def edit_profile(requset):
    profile = Profile.objects.get(user=requset.user)
    if requset.method == "POST":
        user_form = UserForm(requset.POST , instance=requset.user)
        profile_form = ProfileForm(requset.POST,requset.FILES,instance=profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            myprofile = profile_form.save(commit=False)
            myprofile.user = requset.user
            myprofile.save()
            return redirect('/accounts/profile')
    else:
        user_form = UserForm(instance=requset.user)
        profile_form = ProfileForm(instance=profile)


    return render(requset,'profile/profile_edit.html',{
        'user_form':user_form,
        'profile_form':profile_form
    })



def user_favourites(request):
    user_favourites = All.objects.filter(like=request.user)
    return render(request,'profile/user_favourite.html',{'user_favourites':user_favourites})

