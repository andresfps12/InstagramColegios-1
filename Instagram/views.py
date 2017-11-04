from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from Instagram.models import *
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'GET':
        return render(request, 'Register.html')
    else:
        name = request.POST['nombre_completo']
        username = request.POST['usuario']
        email = request.POST['correo']
        password = request.POST['password']
        usuarioDjango = User.objects.create_user(username = username,
                        password = password, email = email, first_name = name)
        miUsuario = MiUsuario(usuario_django = usuarioDjango)
        usuarioDjango.save()
        miUsuario.save()
        return redirect('Login')

@login_required
def home(request):
    return render(request, 'home.html')

@login_required
def profile(request):
    mi_usuario = MiUsuario.objects.get( pk = request.user.pk )
    context = { 'usuario_actual': mi_usuario }
    return render(request, 'profile.html', context)
