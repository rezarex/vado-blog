from django.shortcuts import render, redirect
from django.contrib import messages
from validate_email import validate_email
from .models import User
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from helpers.decorators import auth_user_should_not_access
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str, DjangoUnicodeDecodeError
from .utils import generate_token
from django.core.mail import EmailMessage
from django.conf import settings

'''
TODO: implement thread so as to have email sent concurently as user registers to avoid waiting for too long
'''

# def send_activation_email(user, request):
#     current_site = get_current_site(request)
#     email_subject ="Activation Needed for Account"
#     email_body = render_to_string('authentication/activate.html', {
#         'user': user,
#         'domain':current_site,
#         'uid':urlsafe_base64_encode(force_bytes(user.pk)),
#         'token': generate_token.make_token(user)
#     })

#     email = EmailMessage(subject=email_subject,
#                   body=email_body,
#                   from_email=settings.EMAIL_FROM_USER,
#                   to=[user.email]
#                   )
#     email.send()


@auth_user_should_not_access
def register(request):

    if request.method == "POST":
        context = {'has_error': False, 'data':request.POST}
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        if len(password)<6:
            messages.add_message(request, messages.WARNING, "The password entered is too short")

            context['has_error'] = True
        
        if password != password2:
            messages.add_message(request, messages.WARNING, "The passwords entered do not match!")

            context['has_error'] = True

        # if not validate_email(email):
        #     messages.add_message(request, messages.WARNING, "Enter a valid email")

        #     context['has_error'] = True

        if not username:
            messages.add_message(request, messages.WARNING, "Enter your username!")

            context['has_error'] = True

        if User.objects.filter(username = username).exists():
            messages.add_message(request, messages.WARNING, "Username taken, please choose another one")
            return render(request, 'authentication/register.html', context, status=409)

        if User.objects.filter(email = email).exists():
            messages.add_message(request, messages.WARNING, "Email exists in our database, please use another one")
            return render(request, 'authentication/register.html', context, status=409)

        if context['has_error']:
            return render(request, 'authentication/register.html', context)
        
        user = User.objects.create_user(username=username, email=email)
        user.set_password(password)
        user.save()

        # send_activation_email(user, request)

        messages.add_message(request, messages.SUCCESS, "Registration Succesful! You may login")

        return redirect('login')
    
    return render(request, 'authentication/register.html')


    
@auth_user_should_not_access
def login_user(request):

    if request.method == 'POST':
        context = {'data': request.POST}
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)


        # if not user.is_email_verified:
        #     messages.add_message(request, messages.WARNING, 'Email is NOT Verified, check email inbox or spam')

        #     return render(request, 'authentication/login.html', context)


        if not user:
            messages.add_message(request, messages.WARNING, 'Invalid credentials')

            return render(request, 'authentication/login.html', context)
        
        login(request, user)
        messages.add_message(request, messages.WARNING, f'Welcome {user.username}')
        return redirect(reverse('home'))


    return render(request, 'authentication/login.html')

def logout_user(request):

    logout(request)
    messages.add_message(request, messages.INFO, 'Successfully logged out!')

    return redirect(reverse('login'))


# def activate_user(request, uidb64, token):
    
#     try:
#         uid = force_str(urlsafe_base64_decode(uidb64))

#         user = User.objects.get(pk=uid)

#     except Exception as e:
#         user = None

#     if user and generate_token.check_token(user, token):
#         user.is_email_verified =True
#         user.save()

#         messages.add_message(request, messages.SUCCESS, "Email activated succesfully!, You may login.")

#         return redirect(reverse('login'))
    
#     return render(request, 'authentication/activate-failed.html', {'user':user})

    