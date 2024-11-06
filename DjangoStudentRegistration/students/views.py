from django.shortcuts import render
from courses.models import Course
from .models import Student

def register_student(request):

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        roll_number = request.POST.get('roll_number')
        course_id = request.POST.get('course')
        course = Course.objects.get(id=course_id)

        
        # print('Student saved successfully')
        # print({
        #     'name': name,
        #     'email': email,
        #     'phone': phone,
        #     'address': address,
        #     'roll_number': roll_number,
        #     'course': course
        # })
        student = Student(
            name=name,
            email=email,
            phone=phone,
            address=address,
            roll_number=roll_number,
            course=course
        )
        student.save()
    
    courses = Course.objects.all()
    return render(request, 'register.html', {'courses': courses})
