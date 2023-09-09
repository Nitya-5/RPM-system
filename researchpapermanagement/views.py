
import json
import logging
from django.shortcuts import render, redirect
from .forms import FileForm, StudentSignupForm, StudentLoginForm, FacultySignupForm, FacultyLoginForm
from .models import FileModel, Student, Faculty
from django.http import HttpResponse, JsonResponse
from django.urls import reverse


def home(request):
    return render(request, 'base.html')


def upload_file(request):
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('dashboard_show')
    else:
        form = FileForm()
    return render(request, 'upload_file.html', {'form': form})


def update_file(request, id):
    paper = FileModel.objects.get(id=id)
    form = FileForm(request.POST, request.FILES, instance=paper)
    if form.is_valid():
        form.save()
        return redirect('dashboard_show')
    else:
        print('error updating file')
    return render(request, 'update_paper.html', {'paper': paper})


def delete_paper(request, id):
    paper = FileModel.objects.get(id=id)
    paper.delete()
    return redirect('dashboard_show')


def file_list(request):
    files = FileModel.objects.all()
    return render(request, 'file_list.html', {'files': files})


def login_student(request):
    if request.method == 'POST':
        form = StudentLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            try:
                user = Student.objects.get(email=email, password=password)
            except Student.DoesNotExist:
                return redirect(reverse('SignUp'))
            return render(request, 'login_success.html')
    else:
        form = StudentLoginForm()
    return render(request, 'loginnew.html')


def login_faculty(request):
    if request.method == 'POST':
        form = FacultyLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            try:
                user = Faculty.objects.get(email=email, password=password)
            except Faculty.DoesNotExist:
                return redirect(reverse('SignUp'))
            return render(request, 'login_success.html')
    else:
        form = FacultyLoginForm()
    return render(request, 'loginnew.html')


def SignUp_student(request):
    if request.method == 'POST':
        form = StudentSignupForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            college = form.cleaned_data['college']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = Student(name=name, college=college, email=email,
                           password=password)
            user.save()
            return render(request, 'Signup_success.html')
    else:
        form = StudentSignupForm()
    return render(request, 'signup_faculty.html')


def SignUp_faculty(request):
    if request.method == 'POST':
        form = FacultySignupForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            college = form.cleaned_data['college']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = Faculty(name=name, college=college, email=email,
                           password=password)
            user.save()
            return render(request, 'Signup_success.html')
    else:
        form = FacultySignupForm()
    return render(request, 'signup_faculty.html')


def dashboard_show(request):
    papers = FileModel.objects.all()
    return render(request, 'dashboard_show.html', {'papers': papers})


def dashboard(request):
    return render(request, 'dashboard_base.html')


def login_admin(request):
    return render(request, 'dashboard.html')


def show(request):
    papers = FileModel.objects.all()
    return render(request, 'show.html', {'papers': papers})


"""
def createStudent(request):
    json_data = {}
    if request.method == 'POST':
        # Get the JSON data from the request body
        try:
            json_data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({'validation': 'Invalid JSON data'})
    name1 = json_data.get('name')
    college1 = json_data.get('college')
    email1 = json_data.get('email')
    password1 = json_data.get('password')
    for i in Student.objects.all():
        if i.email == email1:
            return JsonResponse({'validation': "False"})
    # I should set cookie
    Student(name=name1, password=password1,
            email=email1, college=college1).save()
    return JsonResponse({'validation': "True"})


def createFaculty(request):
    json_data = {}
    if request.method == 'POST':
        # Get the JSON data from the request body
        try:
            json_data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({'validation': 'Invalid JSON data'})
    name1 = json_data.get('name')
    college1 = json_data.get('college')
    email1 = json_data.get('email')
    password1 = json_data.get('password')
    for i in Faculty.objects.all():
        if i.email == email1:
            return JsonResponse({'validation': "False"})
    # I should set cookie
    Faculty(name=name1, password=password1,
            email=email1, college=college1).save()
    logger = logging.getLogger(__name__)
    logger.info(f"Phone number: {request.POST.get('name')}")
    return JsonResponse({'validation': "True"})
# to show the show page
"""

"""
def validateStudent(request):
    email = request.GET.get('email')
    password = request.GET.get('password')
    if email and password:
        for i in Student.objects.all():
            if i.email == email and i.password == password:
                return JsonResponse({'validation': True})

    return JsonResponse({'validation': False})


def validateFaculty(request):
    email = request.GET.get('email')
    password = request.GET.get('password')
    if email and password:
        for i in Faculty.objects.all():
            if i.email == email and i.password == password:
                return JsonResponse({'validation': True})
    return JsonResponse({'validation': False})
"""
