from django.shortcuts import render, redirect

from registration.forms import StaffForm


# Create your views here.
def add_staff(request):
    if request.method=='POST':
        form=StaffForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_staff')

    else:
        form = StaffForm()
        return render(request, 'register.html',{'form':form})
