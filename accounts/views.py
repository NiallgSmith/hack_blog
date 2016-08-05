from django.shortcuts import render, redirect
from django.contrib import messages, auth
from .forms import UserRegistrationForm, UserLoginForm
from django.core.urlresolvers import reverse
from django.template.context_processors import csrf
from django.contrib.auth.decorators import login_required
from django.utils import timezone
import logging
from blog.models import Post
log = logging.getLogger(__name__)


def register(request):
    log.info("Handling register %s request", request.method)
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()

            user = auth.authenticate(email=request.POST.get('email'), password=request.POST.get('password1'))

            if user:
                messages.success(request, 'You have successfully registered')
                return redirect(reverse('profile'))

            else:
                messages.error(request, 'Unable to log you in at this time ')

    else:
        form = UserRegistrationForm()

    args = {'form': form}
    args.update(csrf(request))

    return render(request, 'register.html', args)


@login_required(login_url='/login/')
def profile(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'profile.html', {'posts': posts})


def login(request):
    log.info("Handling login %s request", request.method)
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            user = auth.authenticate(email=request.POST.get('email'), password=request.POST.get('password'))

            if user is not None:
                auth.login(request, user)
                messages.error(request, 'You have successfully logged in! ')
                return redirect(reverse('profile'))
            else:
                form.add_error(None, 'Your email or password was not recognised')
    else:
        form = UserLoginForm()

    args = {'form': form}
    args.update(csrf(request))
    return render(request, 'login.html', args)


def logout(request):
    log.info("Handling logout %s request", request.method)
    auth.logout(request)
    messages.success(request, 'You have successfully logged out')
    return redirect(reverse('index'))
