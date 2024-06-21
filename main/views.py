from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegistrationForm, LoginForm, ContactForm
from .models import User, Message

def index(request):
    return render(request, 'main/index.html')

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            messages.success(request, 'Registration successful. Please log in.')
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'main/register.html', {'form': form})


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            try:
                user = User.objects.get(username=username)
                if user.check_password(password):
                    request.session['user_id'] = user.id
                    request.session['username'] = user.username
                    messages.success(request, f'Welcome, {user.username}')
                    return redirect('index')
                else:
                    messages.error(request, 'Invalid password')
            except User.DoesNotExist:
                messages.error(request, 'Invalid username')
    else:
        form = LoginForm()
    return render(request, 'main/login.html', {'form': form})


def logout(request):
    request.session.flush()
    messages.success(request, 'Logged out successfully')
    return redirect('login')


def send_message_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            phone = form.cleaned_data['phone']
            message = form.cleaned_data['message']
            Message.objects.create(
                first_name=first_name,
                last_name=last_name,
                phone=phone,
                message=message
            )
            return redirect('index')
    return redirect('index')
