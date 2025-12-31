from django.shortcuts import render
from myapp.models import Student
# Create your views here.
def fakeview(request):
	s=Student.objects.all()
	d={'stud':s}
	return render(request,'myapp/fake.html',d)