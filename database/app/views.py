from django.shortcuts import render
from .models import Student, Course, Course2, Student2, Enrollment
# Create your views here.
from datetime import date

def index(request):
    # students = Student.objects.all()
    # courses = Students.objects.get(id=1)
    # python = Course.objects.get(name='Python')
    # student = python.students_set.create(name='Bob')
    # student = Student.objects.create(name='Tom')
    # python.student_set.add(Student)
    # st = Student.objects.get(id=3)
    # his = Course.objects.get(name='History')
    # his.student_get.add(st)
    # res = Student.objects.get(id=3).course.all()
    #
    # django = Course2.objects.create(name='Django')
    # tom = Student2.objects.create(name='Tom')
    # res, _ = Enrollment.objects.create(student=tom, course=django, date='2023-11-11', mark=5)

    # st = Student2.objects.get(id=2)
    # crs = Course2.objects.get(id=1)
    # # res = st.course.all()
    # res = crs.student2_set.all()

    return render(request, 'app/index.html', context={'students': res})










