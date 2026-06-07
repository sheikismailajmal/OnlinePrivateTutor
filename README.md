# Online Private Tutor

A web-based tutoring platform developed using Django that connects students with private tutors. The system allows students to find tutors, send tutoring requests, manage bookings, and interact with tutors through a user-friendly interface. Administrators can manage users, approve registrations, and monitor platform activities.

---

## Features

### Student Module
- Student Registration
- Student Login
- View Tutor Profiles
- Send Tutor Requests
- Book Tutors
- View Booking Status
- Manage Profile
- Submit Reviews and Ratings

### Tutor Module
- Tutor Registration
- Tutor Login
- View Student Requests
- Accept or Reject Requests
- Manage Profile
- View Reviews and Ratings

### Admin Module
- Admin Login
- Approve or Reject Student Registrations
- Approve or Reject Tutor Registrations
- Manage Students
- Manage Tutors
- Manage Bookings
- Manage Reviews
- View System Activities

---

## Technologies Used

- Python
- Django
- SQLite
- HTML5
- CSS3
- JavaScript
- Bootstrap

---

## Project Structure

```text
OnlinePrivateTutor/
│
├── app/
├── project/
├── static/
├── templates/
├── manage.py
└── README.md
```

---

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/sheikismajlajmal/OnlinePrivateTutor.git
cd OnlinePrivateTutor
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

### 3. Activate Virtual Environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux/Mac

```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install django
```

Or if a requirements file exists:

```bash
pip install -r requirements.txt
```

### 5. Apply Database Migrations

```bash
python manage.py migrate
```

### 6. Create Superuser

```bash
python manage.py createsuperuser
```

Follow the prompts to create the admin account.

### 7. Run Development Server

```bash
python manage.py runserver
```

Open:

```text
http://127.0.0.1:8000/
```

---

## User Roles

### Administrator

- Approve student registrations
- Approve tutor registrations
- Manage tutors and students
- Monitor bookings and reviews

### Student

- Register and login
- Search tutors
- Send booking requests
- Manage profile
- Give reviews

### Tutor

- Register and login
- Manage profile
- View requests
- Accept or reject bookings

---

## Screenshots

Add screenshots of:

1. Home Page
2. Student Registration
3. Student Login
4. Tutor Registration
5. Tutor Login
6. Admin Dashboard
7. Booking Page
8. Review Page

---

## Future Enhancements

- Online Payment Integration
- Video Call Support
- Real-Time Chat System
- Email Notifications
- OTP Verification
- Tutor Recommendation System
- Mobile Application

---

## Author

**Sheik Ismail Ajmal**

MCA (Cyber Security)  
Jain University

GitHub:
https://github.com/sheikismajlajmal

---

## License

This project is developed for educational and learning purposes.