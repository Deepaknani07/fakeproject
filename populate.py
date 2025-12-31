import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fakeproject.settings')
django.setup()
from faker import Faker
from myapp.models import Student
f = Faker()
def generate_data(n):
    for i in range(n):
        fname=f.name()
        froll=f.random_int(min=1,max=10000)
        fmarks=f.random_int(min=35,max=100)
        fdob=f.date_of_birth()
        fplace=f.address()
        femail=f.email()
        e = Student.objects.get_or_create(name=fname,roll=froll,marks=fmarks,place=fplace,email=femail,dob=fdob)
generate_data(20)
    
