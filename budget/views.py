from django.shortcuts import render


def login(request):
    return render(request, 'login.html')

# GET, POST
def register(request):
    if request.method == 'POST':
        password = request.POST['password']
        password_repeat = request.POST['password-repeat']
        if password != password_repeat:
            return render(request, 'register.html', {'error': 'Passwords do not match'})

    return render(request, 'register.html')