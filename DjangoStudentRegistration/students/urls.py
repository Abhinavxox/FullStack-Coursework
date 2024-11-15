from django.urls import path
from . import views

urlpatterns = [
     path('list/', views.student_list, name='student_list'),
    path('register/', views.register_student, name='register_student'),
    path('update/<str:roll_number>/', views.update_student, name='update_student'),
    path('delete/<str:roll_number>/', views.delete_student, name='delete_student'),
]