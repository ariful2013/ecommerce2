from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout


from .tokens import account_activation_token
from .forms_auth import RegistrationForm, UserEditForm
# Import for Email
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.core.mail import send_mail
from django.contrib import messages
from django.contrib.auth import get_user_model
from orders.views import user_orders
User = get_user_model()


# Create your views here.


# def account_register(request):
#     return render(request, 'account/registration/register.html', {})

def account_register(request):
    if request.user.is_authenticated:
        return redirect('account:dashboard')

    if request.method == 'POST':
        registerForm = RegistrationForm(request.POST)
        if registerForm.is_valid():
            user = registerForm.save(commit=False)
            user.is_active = False
            user.save()

            # Setup Email
            current_site = get_current_site(request)
            subject = 'Activate your account'
            message = render_to_string('account/registration/account_activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })

            send_mail(subject, message, 'email@example.com',
                      [user.email], fail_silently=False)

            return render(request, 'account/registration/activation_message.html')
    else:
        registerForm = RegistrationForm()

    return render(request, 'account/registration/register.html', {'form': registerForm})


def account_activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, user.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return redirect('account:dashboard')
    else:
        return render(request, 'account/registration/invalid_message.html')


@login_required
def dashboard(request):
    orders = user_orders(request)
    return render(request,
                  'account/user/dashboard.html',
                  {'section': 'profile', 'orders': orders})


@login_required
def edit_details(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)
        if user_form.is_valid():
            user_form.save()
    else:
        user_form = UserEditForm(instance=request.user)

    return render(request, 'account/user/edit_details.html', {'user_form': user_form})


@login_required
def delete_user(request):
    user = User.objects.get(username=request.user)
    user.is_active = False
    user.save()
    logout(request)
    return redirect('account:delete_confirm')