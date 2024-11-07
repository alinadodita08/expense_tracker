from django.shortcuts import render


def login(request):
    return render(request, 'login.html')

def password_num(password):
    numbers = '1234567890'
    count = 0
    for character in password:
        if character in numbers:
            count += 1
    return count
        
def password_special_char(password):
    special_characters = "!#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
    count = 0
    for character in password:
        if character in special_characters:
            count += 1
    return count

# GET, POST
def register(request):
    if request.method == 'POST':
        password = request.POST['password']
        password_repeat = request.POST['password-repeat']
        if password != password_repeat:
            return render(request, 'register.html', {'error': 'Passwords do not match'})
        if len(password) < 8:
            return render(request, 'register.html', {'error': 'Password should be at least 8 characters.'})
        if password_num(password) < 3:
            return render(request, 'register.html', {'error': 'Password should have at least 3 numbers.'})
        if password_special_char(password) < 1:
            return render(request, 'register.html', {'error': 'Password should have at least 1 special character.'})
            

    return render(request, 'register.html')