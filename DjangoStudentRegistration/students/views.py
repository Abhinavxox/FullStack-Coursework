from django.shortcuts import render,get_object_or_404, redirect
from courses.models import Course
from .models import Student
from .forms import StudentForm 

def register_student(request):

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        roll_number = request.POST.get('roll_number')
        course_id = request.POST.get('course')
        course = Course.objects.get(id=course_id)

        student = Student(
            name=name,
            email=email,
            phone=phone,
            address=address,
            roll_number=roll_number,
            course=course
        )
        student.save()
        return render(request, 'successpage.html',{'message':'Student registered successfully!'})
    
    courses = Course.objects.all()
    return render(request, 'register.html', {'courses': courses})

def update_student(request, roll_number):
    student = get_object_or_404(Student, roll_number=roll_number)
    courses = Course.objects.all()
    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            print ("Student updated successfully")
            return render(request, 'successpage.html',{'message':'Student updated successfully!'})
    else:
        form = StudentForm(instance=student)

    return render(request, 'update_student.html', {'form': form, 'student': student, 'courses': courses})

def delete_student(request, roll_number):
    student = get_object_or_404(Student, roll_number=roll_number)
    student.delete()
    return redirect('student_list') 

def student_list(request):
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students})