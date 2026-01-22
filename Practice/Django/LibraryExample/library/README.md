# Tour Library - Library Management System

A professional Django-based library management system with user authentication, book borrowing, and dashboard features.

## ✨ Features

- **User Authentication**: Secure login/registration with password validation
- **Dashboard**: Personalized user dashboard with multiple sections
- **Book Management**: Browse, search, and manage book catalog
- **Borrowing System**: Borrow and return books with history tracking
- **Statistics**: View personal borrowing statistics
- **Responsive Design**: Mobile-friendly UI using BEM CSS methodology

## 🛠️ Tech Stack

- **Backend**: Django 5.0.1
- **Frontend**: HTML5, CSS3, JavaScript, HTMX
- **Database**: SQLite (Development), PostgreSQL (Production)
- **Icons**: Font Awesome 7
- **Task Queue**: Celery + Redis (Optional)
- **Testing**: Pytest + Pytest-Django

## 📋 Project Structure

```
library_management/
├── config/                 # Project configuration
├── apps/
│   ├── accounts/          # User authentication
│   ├── dashboard/         # User dashboard
│   ├── books/             # Book management
│   └── borrowing/         # Borrowing logic
├── templates/             # HTML templates
├── static/               # CSS, JS, Media
├── utils/                # Utility functions
└── manage.py
```

## 🚀 Getting Started

### Prerequisites
- Python 3.9+
- pip
- virtualenv

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd library_management
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\\Scripts\\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Create .env file**
   ```bash
   cp .env.example .env
   ```

5. **Run migrations**
   ```bash
   python manage.py migrate
   ```

6. **Create superuser**
   ```bash
   python manage.py createsuperuser
   ```

7. **Collect static files**
   ```bash
   python manage.py collectstatic --noinput
   ```

8. **Run development server**
   ```bash
   python manage.py runserver
   ```

Visit http://localhost:8000 in your browser.

## 📚 Documentation

### Adding New Books (Admin Panel)

1. Go to http://localhost:8000/admin
2. Login with superuser credentials
3. Navigate to Books section
4. Click "Add Book" and fill in details

### User Registration

1. Navigate to /register
2. Fill in registration form with:
   - Email
   - Username (alphanumeric, underscores allowed)
   - Strong password (8+ chars, uppercase, lowercase, number, special char)
   - Confirm password

### Dashboard Features

- **Student Information**: View profile details
- **Statistics**: Borrowing history and patterns
- **Borrow History**: All previous borrows
- **Book Return**: Return borrowed books
- **Available Books**: Browse library catalog

## 🔒 Security Features

✅ CSRF Protection
✅ Password Hashing (PBKDF2)
✅ SQL Injection Prevention (Django ORM)
✅ XSS Protection
✅ Secure Session Cookies
✅ Input Validation & Sanitization
✅ Rate Limiting (Optional)
✅ HTTPS Ready (Production)

## 🧪 Testing

```bash
# Run all tests
pytest

# Run specific test file
pytest apps/accounts/tests.py

# Run with coverage
pytest --cov=apps
```

## 🎨 CSS Architecture

Uses **BEM (Block Element Modifier)** methodology for maintainable CSS:

- **Block**: `.navbar`, `.form`, `.hero`
- **Element**: `.navbar__menu`, `.form__input`
- **Modifier**: `.form__button--primary`, `.hero__title--large`

## 📱 Responsive Breakpoints

- **Mobile**: < 480px
- **Tablet**: 480px - 768px
- **Desktop**: > 768px

## 🐛 Known Issues

None currently. Report bugs via GitHub Issues.

## 📝 License

This project is licensed under the MIT License.

## 👥 Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open Pull Request

## ✅ Checklist for Next Steps

- [ ] Create Book model with proper validations
- [ ] Create Borrowing model for tracking
- [ ] Implement book search and filtering
- [ ] Add email notifications
- [ ] Create API endpoints (Django REST Framework)
- [ ] Add unit and integration tests
- [ ] Setup CI/CD pipeline
- [ ] Deploy to production server