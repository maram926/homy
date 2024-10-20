from django.shortcuts import redirect, render
from .forms import SignupForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache




def deesh(request):
    return render(request , 'dash/deesh.html')

def singlechef(request):
    return render(request , 'dash/singlechef.html')


def chefs(request):
    return render(request , 'dash/chefs.html')


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST) 

        if form.is_valid():
            form.save()
          
            return redirect('/login/')

    else: 
        form =  SignupForm()        

    return render(request , 'dash/signup.html' , 
    {
        'form':form
    }
    )

@never_cache
def Base(request):
    return render(request , 'dash/Base.html')



@login_required
def login(request):
    return render(request , 'dash/login.html' )
