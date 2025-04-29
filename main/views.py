from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, LoginForm
from django.http import JsonResponse
from .models import Accident
from .forms import AccidentForm
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about.html')

def contacts(request):
    return render(request, 'main/contacts.html')

def help_page(request):
    return render(request, 'main/help.html')

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'main/register.html', {'form': form})

def login_view(request):
    error_message = None

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                request,
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password']
            )
            if user is not None:
                login(request, user)
                return redirect('profile')
            else:
                error_message = "Неверное имя пользователя или пароль"
    else:
        form = LoginForm()

    return render(request, 'main/login.html', {'form': form, 'error_message': error_message})


def logout_view(request):
    logout(request)
    return redirect('index')

@login_required
def profile_view(request):
    return render(request, 'main/profile.html')

def accident_list_api(request):
    types = request.GET.get('types', '').split(',')
    accidents = Accident.objects.all()
    if types and types != ['']:
        accidents = accidents.filter(accident_type__in=types)

    data = []
    for a in accidents:
        data.append({
            'lat': a.latitude,
            'lon': a.longitude,
            'type': a.get_accident_type_display(),
            'title': a.title,
            'description': a.description
        })
    return JsonResponse(data, safe=False)

@login_required
def add_accident(request):
    if request.method == 'POST':
        form = AccidentForm(request.POST)
        if form.is_valid():
            accident = form.save(commit=False)
            accident.user = request.user
            accident.save()
            return redirect('index')
    else:
        lat = request.GET.get('lat')
        lon = request.GET.get('lon')
        form = AccidentForm(initial={'latitude': lat, 'longitude': lon})
    return render(request, 'main/add_accident.html', {'form': form})

from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_POST

@login_required
@require_POST
def delete_accident(request, accident_id):
    accident = get_object_or_404(Accident, id=accident_id)
    accident.delete()
    return redirect('profile')
