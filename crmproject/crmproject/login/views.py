from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect


def add_login(request):
    context_set = {}  # A set object
    context_dict = dict(context_set)  # Convert set to dictionary
    if request.method == 'POST':
        staffid = request.POST.get('staffid')
        password = request.POST.get('password')

        user = authenticate(request, staffid=staffid, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            error_message = 'Invalid staffid or password.'
        return render(request, 'login.html', {'Invalid staffid or password.'}, context=context_dict)
    else:
        return render(request, 'login.html', context=context_dict)
