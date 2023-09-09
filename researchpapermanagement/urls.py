from django.urls import path
from . import views
urlpatterns = [

    path('upload/', views.upload_file, name='upload_file'),
    path('files/', views.file_list, name='file_list'),
    path('', views.home, name='home'),
    path('login/student', views.login_student, name='login_student'),
    path('signup/student', views.SignUp_student, name='signup_student'),
    path('signup/faculty', views.SignUp_faculty, name='signup_faculty'),
    path('login/faculty', views.login_faculty, name='login_faculty'),
    path('login/admin', views.login_admin, name='login_admin'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('dashboard/show', views.dashboard_show, name='dashboard_show'),
    path('papers', views.show, name='papers'),
    path('update/<int:id>', views.update_file, name="update_file"),
    path('delete/<int:id>', views.delete_paper, name="delete"),
]
