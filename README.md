🧑‍💼 Employee Management System (Django CRUD)

A simple Employee Management System built using Django that demonstrates full CRUD (Create, Read, Update, Delete) operations with a clean UI and Django ModelForm.

🚀 Features

➕ Add new employees

📋 View employee list

✏️ Update employee details

❌ Delete employee records

🛡 CSRF protection enabled

🧩 Uses Django ModelForm

🎨 Clean and responsive UI with custom CSS

🛠 Tech Stack

Backend: Python, Django

Frontend: HTML, CSS

Database: SQLite (default Django DB)

Tools: Django ORM, GitHub

📂 Project Structure
employee_project/
│
├── myapp/
│   ├── migrations/
│   ├── templates/
│   │   └── myapp/
│   │       ├── update.html
│   │       ├── index.html
│   ├── models.py
│   ├── forms.py
│   ├── views.py
│
├── db.sqlite3
├── manage.py
└── README.md

🧑‍💻 Model Used
class Employee(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    place = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name

🔄 Update Functionality

Uses Django ModelForm

Pre-fills employee data

Updates record without creating duplicates

def update_view(request, id):
    e = Employee.objects.get(id=id)

    if request.method == "POST":
        form = EmployeeForm(request.POST, instance=e)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = EmployeeForm(instance=e)

    return render(request, 'myapp/update.html', {'form': form})

▶️ How to Run the Project

Clone the repository

git clone https://github.com/your-username/employee-management-django.git


Navigate to project

cd employee-management-django


Create virtual environment (optional)

python -m venv venv
venv\Scripts\activate


Install Django

pip install django


Run migrations

python manage.py makemigrations
python manage.py migrate


Start server

python manage.py runserver


Open browser:

http://127.0.0.1:8000/

📌 Learning Outcomes

Django Models & ORM

ModelForm usage

CRUD operations

Form validation

Template rendering

Clean project structure
