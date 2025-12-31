FakeProject – Django CRUD Application

A simple Django-based CRUD (Create, Read, Update, Delete) web application designed for learning and practice. This project demonstrates core Django concepts such as models, forms, views, templates, and database operations.

🚀 Features

➕ Add new records

📄 View records

✏️ Update existing records

❌ Delete records

🎨 User-friendly HTML & CSS UI

🔒 CSRF protection enabled

🛠️ Technologies Used

Backend: Python, Django

Frontend: HTML, CSS

Database: SQLite (default Django DB)

📂 Project Structure
fakeproject/
│
├── myapp/
│   ├── migrations/
│   ├── templates/
│   │   └── myapp/
│   │       ├── insert.html
│   │       ├── update.html
│   │       └── display.html
│   ├── models.py
│   ├── forms.py
│   ├── views.py
│   └── urls.py
│
├── fakeproject/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── manage.py
└── README.md

⚙️ Installation & Setup
1️⃣ Clone the Repository
git clone https://github.com/Deepaknani07/fakeproject.git
cd fakeproject

2️⃣ Create Virtual Environment (Optional but Recommended)
python -m venv venv
venv\Scripts\activate   # Windows

3️⃣ Install Django
pip install django

4️⃣ Run Migrations
python manage.py makemigrations
python manage.py migrate

5️⃣ Start Development Server
python manage.py runserver

6️⃣ Open in Browser
http://127.0.0.1:8000/

🧪 Usage

Use the Insert page to add data

View all records on the Display page

Edit data using the Update option

Remove records using Delete
