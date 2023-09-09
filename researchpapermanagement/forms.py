from django import forms
from .models import FileModel, Student, Faculty


class FileForm(forms.ModelForm):
    class Meta:
        model = FileModel
        fields = ['title', 'description', 'author', 'by', 'file']


class StudentSignupForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'college', 'email', 'password']


class FacultySignupForm(forms.ModelForm):
    class Meta:
        model = Faculty
        fields = ['name', 'college', 'email', 'password']


class StudentLoginForm(forms.Form):
    email = forms.CharField(max_length=30)
    password = forms.CharField(max_length=30)


class FacultyLoginForm(forms.Form):
    email = forms.CharField(max_length=30, help_text='Email address')
    password = forms.CharField(max_length=30, help_text='Password')
