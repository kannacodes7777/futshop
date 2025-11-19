import json
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def login_user(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            data = request.POST
        username = data.get('username')
        password = data.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return JsonResponse({
                'status': True,
                'message': 'Login Berhasil!',
                'username': username,
            })
        else:
            return JsonResponse({
                'status': False,
                'message': 'Username atau password salah.',
            })
    return JsonResponse({'status': False, 'message': 'Metode tidak diizinkan'})

@csrf_exempt
def register(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            data = request.POST
        username = data.get('username')
        password = data.get('password')
        
        if not username or not password:
            return JsonResponse({'status': False, 'message': 'Username/Password kosong!'})

        if User.objects.filter(username=username).exists():
            return JsonResponse({'status': False, 'message': 'Username sudah digunakan.'})

        user = User.objects.create_user(username=username, password=password)
        user.save()

        return JsonResponse({'status': True, 'message': 'Akun berhasil dibuat!'})
            
    return JsonResponse({'status': False, 'message': 'Metode tidak diizinkan'})

@csrf_exempt
def logout_user(request):
    logout(request)
    return JsonResponse({'status': True, 'message': 'Logout berhasil!'})