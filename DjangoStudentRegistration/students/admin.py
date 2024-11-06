from django.contrib import admin
from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'roll_number', 'course')
    search_fields = ('name', 'roll_number')
    list_filter = ('course',)