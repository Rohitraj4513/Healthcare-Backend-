 Healthcare Backend (Django REST API)

 
Build a secure backend for managing users, patients, doctors, and their mappings using Django REST Framework and JWT Authentication.


🚀 Setup Instructions (Windows)


1. Clone the Project


git clone https://github.com/Rohitraj4513/healthcare-backend.git


cd healthcare-backend


2. Install Requirements


pip install django djangorestframework djangorestframework-simplejwt


3. Run Migrations


python manage.py migrate


4. Start the Server


python manage.py runserver


Server will run at:
http://127.0.0.1:8000


🔥 API Testing Flow (Postman)


➡️ 1. Register


POST : http://127.0.0.1:8000/api/auth/register/



{


  "username": "testuser",
  "email": "test@example.com",
  "password": "testpassword123"

  
}



➡️ 2. Login (Get JWT Token)


POST : http://127.0.0.1:8000 /api/auth/login/

{
  "email": "test@example.com",
  "password": "testpassword123"
}
Response:


{
  "access": "your_token",
  "refresh": "your_refresh_token"
}


✅ Copy the access token.


➡️ 3. Set Authorization in Postman


Authorization → Type: Bearer Token


Paste your access token.


➡️ 4. Create Patient


POST: http://127.0.0.1:8000/api/patients/


{
  "name": "John Doe",
  "age": 30,
  "gender": "Male",
  "address": "USA"
}


➡️ 5. Create Doctor


POST : http://127.0.0.1:8000/api/doctors/


{
  "name": "Dr. Smith",
  "specialization": "Cardiologist"
}


➡️ 6. Map Patient to Doctor


POST: http://127.0.0.1:8000/api/mappings/


{
  "patient": 1,
  "doctor": 1
}

