from django.shortcuts import render , redirect
from .forms import SignupForm , UserForm , ProfileForm 
from .models import Profile 
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login 
from gendr.models import All
from django.contrib import messages
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage
from django.urls import reverse




def signup(request):
        if request.method == "POST":
            form=SignupForm(request.POST)
            if form.is_valid():
                form.save()
                usernames = form.cleaned_data['username']
                passwords = form.cleaned_data['password1']
                user = authenticate(username=usernames,password=passwords)
                login(request,user)

                return redirect('/accounts/login')     
        else:
            form=SignupForm()

        return render(request,'registration/signup.html',{'form':form})


def profile(request):
    profile=Profile.objects.get(user=request.user)

    return render(request,'profile/profile.html',{'profile':profile})

def forgotPassword(request):
    if request.method == 'POST':
        email = request.POST['email']
        if User.objects.filter(email=email).exists():
            user = User.objects.get(email__exact=email)

            # Reset password email
            current_site = get_current_site(request)
            mail_subject = 'Reset Your Password'
            message = render_to_string('registration/password_reset_email.html', {
                'user': user,
                'domain': current_site,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user),
            })
            to_email = email
            send_email = EmailMessage(mail_subject, message, to=[to_email])
            send_email.send()

            messages.success(request, 'Password reset email has been sent to your email address.')
            return redirect('login')
        else:
            messages.error(request, 'Account does not exist!')
            return redirect(reverse('accounts:forgotPassword'))
    return render(request, 'registration/password_reset_form.html')

def resetpassword_validate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User._default_manager.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        request.session['uid'] = uid
        messages.success(request, 'Please reset your password')
        return redirect(reverse('accounts:resetPassword'))
    else:
        messages.error(request, 'This link has been expired!')
        return redirect('login')

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

