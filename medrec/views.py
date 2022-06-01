from django.shortcuts import render,redirect
from .forms import *
from .models import *
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse 
from django.contrib.auth.decorators import login_required


# Create your views here.
### Create a doctor and biller register view with accompanying html, then create login page for the two that links to patient profile (page we created)

def index(request):
    return render(request, 'medrec/index.html')

def doc_reg(request):

    if request.method=='POST':
        form = DoctorRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successful Provider Registration')
            return redirect('/doc_login')
        
        else:
            messages.error(request, 'Unable to register,Please try again')
    else:
        form = DoctorRegisterForm()
    
    context = {
        'form':form
    }
    return render(request, 'medrec/doc_reg.html', context)

def coder_reg(request):
    
    if request.method=='POST':
        form = BillerRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successful CodeSpecialist Registration')
            return redirect('/coder_login')
        
        else:
            messages.error(request, 'Unable to register,Please try again')
    else:
        form = BillerRegisterForm()
    
    context = {
        'form':form
    }
    return render(request, 'medrec/coder_reg.html', context)

def pat_reg(request):
    
    if request.method=='POST':
        form = PatientRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successful Patient Registration')
            return redirect('/pat_login')
        
        else:
            messages.error(request, 'Unable to register,Please try again')
    else:
        form = PatientRegisterForm()
    
    context = {
        'form':form
    }
    return render(request, 'medrec/pat_reg.html', context)

##dance with django on diagnosis page.





# def staff_login(request):
#     error = ''
#     user_page=''
#     if request.method == 'POST':
#         form = AuthenticationForm(request, data=request.POST)
#         if form.is_valid():
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']
#             user = authenticate(username=username, password=password)
#             if user is not None:
#                 login(request,user)
#                 error = ' no'
#                 hos_spec = request.user.groups.all()[0].user_name
#                 if 'next' in request.POST:
#                     return redirect (request.POST.get('next'))
#                 elif hos_spec == 'Physician':
#                     user_page = 'physician'
#                     context = {'error': error, 'user_page':user_page, 'form':form}
#                     return render(request, 'pat_reg', context)
#                 elif hos_spec == 'CodeSpecialist':
#                     user_page = 'codespec'
#                     context = {'error': error, 'user_page':user_page, 'form':form}
#                     return render(request, 'pat_reg', context)


#                 # elif 'next' in request.POST:
#                 #     return redirect (request.POST.get('next'))
#                 else:
#                     messages.info(request, f"Successful Login {username}")
#                     return redirect('pat_rec')

#     else:
#         form = AuthenticationForm()
    
#     context = {
#         'form':form
#     }

#     return render(request, 'medrec/doc_login.html', context)



def doc_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                if 'next' in request.POST:
                    return redirect (request.POST.get('next'))
                else:
                    messages.info(request, f"Successful Login {username}")
                    return redirect('patrec')
            else:
                messages.error(request, 'Invalid Credentials')
    else:
        form = AuthenticationForm()
    
    context = {
        'form':form
    }

    return render(request, 'medrec/doc_login.html', context)

def coder_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                if 'next' in request.POST:
                    return redirect (request.POST.get('next'))
                else:
                    messages.info(request, f"Successful Login {username}")
                    return redirect('patrec')
            else:
                messages.error(request, 'Invalid Credentials')
    else:
        form = AuthenticationForm()

    context = {
        'form':form
    }

    return render(request, 'medrec/coder_login.html', context)

def user_logout(request):
    if not request.user.is_active:
        return redirect('index')
    logout(request)
    return redirect('index')

def pat_rec(request):
    return render(request, 'medrec/pat_rec.html')