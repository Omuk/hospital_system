from django.shortcuts import render,redirect,get_object_or_404
from .forms import *
from .models import *
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse 
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse 
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import *
from django.core import serializers


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
    form =MedicalRecordForm()
    code_forms = medicalRecord.objects.all()

    return render(request, 'medrec/pat_rec.html', {'form':form, 'code_forms': code_forms})

def postCode(request):
    if request.method == "POST":
        form =MedicalRecordForm(request.POST)
        if form.is_valid():
            instance = form.save()
            code_inst_ser = serializers.serialize('json', [instance,])

            return JsonResponse({'instance':code_inst_ser},status=200)
        else:
            return JsonResponse({'error': form.errors}, status=400)
    
    return JsonResponse({'error': ''}, status=400)

#                                                          ###FINAL PART
def patient_search(request):
    if 'term' in request.GET:
        patient = Patient.objects.filter(name__istartswith=request.GET.get('term'))
        names = list()
        for pat_search in patient:
            names.append(pat_search.name)
            return JsonResponse(names, safe=False)
    
    return render(request, 'app_auto/patsearch.html')

@api_view(['GET'])
def getData(request):
    response = Response()
    todos = ICDSearch.objects.all()
    todos_serializer = ICDSearchSerializer(todos, many=True)

    response.data = {
        'todos':todos_serializer.data 
    }
    return response

@api_view(['POST'])
def post_code(request):
    response = Response()

    code_to_save = request.data.get('code_to_save')

    code_serializer = ICDSearchSerializer(data={'title': code_to_save})

    if code_serializer.is_valid ():
        code_serializer.save()

    sel_codes = ICDSearch.objects.all()

    code_serializer = ICDSearchSerializer(sel_codes, many=True)

    response.data = {
        'sel_codes': code_serializer.data
    }

    return response


def del_code(request, code_id):
    response = Response()

    code_del = get_object_or_404(ICDSearch,id=code_id)
    code_del.delete()

    sel_codes = ICDSearch.objects.all()

    code_serializer = ICDSearchSerializer(sel_codes, many=True)

    response.data = {
        'sel_codes': code_serializer.data
    }

    return response


def pat_diagnosis(request, pk):
    icd_form = medicalRecord.objects.get(id=pk)
    form = MedicalRecordForm(instance=icd_form)

    context = {'icd_form': icd_form, 'form':form}
    if request.method =='POST':
        form = MedicalRecordForm(request.POST, instance=icd_form)
        if form.is_valid():
            form.save()

            return redirect('patrec')
    return render(request, 'medrec/pat_rec.html')

def medrec_View(request):
    form =MedicalRecordForm()
    code_forms = medicalRecord.objects.all()

    return render(request, 'medrec/code_index.html', {'form':form, 'code_forms': code_forms})


# def postCode(request):
#     if request.method == "POST":
#         form =MedicalRecordForm(request.POST)
#         if form.is_valid():
#             instance = form.save()
#             code_inst_ser = serializers.serialize('json', [instance,])

#             return JsonResponse({'instance':code_inst_ser},status=200)
#         else:
#             return JsonResponse({'error': form.errors}, status=400)
    
#     return JsonResponse({'error': ''}, status=400)

    