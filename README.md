# FAQ_Management
This is a Django-based FAQ management system that supports multi-language translations, a WYSIWYG editor, and a REST API for managing FAQs.

## Table of Contents
1. [Features](#features)
2. [Installation](#installation)
3. [API Usage](#api-usage)
4. [Running Tests](#running-tests)
5. [Code Quality](#code-quality)

6. [Contribution Guidelines](#contribution-guidelines)


---

## Features
- **Multi-language Support**: FAQs can be translated into multiple languages (e.g., English, Hindi).
- **WYSIWYG Editor**: Integrated with `django-ckeditor` for rich text formatting.
- **REST API**: Supports CRUD operations for FAQs with language-specific translations.
- **Caching**: Uses Redis for caching translations to improve performance.


---

## Installation

### Prerequisites
- Python 3.9 or higher
- PostgreSQL (or any other supported database)
- Redis (for caching)

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/faq-management.git
   cd faq-management
2.Create a virtual environment:
  ```bash
  python -m venv venv
  source venv/bin/activate  
3. Install dependencies:
   ```bash
   pip install -r requirements.txt  
4.Run migrations:
  ```bash
  python manage.py migrate
5.Start the development server:
  ```bash
  python manage.py runserver 

6. API Usage
  Endpoints
  List FAQs: GET /api/faqs/

  Create FAQ: POST /api/faqs/


  Retrieve FAQ: GET /api/faqs/{id}/

  Update FAQ: PUT /api/faqs/{id}/


 Delete FAQ: DELETE /api/faqs/{id}/

7 .Running Tests
  Prerequisites
  Install pytest and pytest-django:

  ```bash
  pip install pytest pytest-django pytest-cov
8.Run Tests
   ```bash
     pytest

9.Code Quality
  Linting
  Use flake8 to ensure your code follows PEP8 guidelines:
   ```bash

  flake8 faq

### Contribution Guidelines
   How to Contribute
  Fork the repository.

### Create a new branch:


 git checkout -b feature/your-feature-name
## Commit your changes:


  git commit -m "feat: Add your feature"
Push to the branch:

  git push origin feature/your-feature-name


## Commit Message Format
  Follow the Conventional Commits format:

  feat: A new feature.

  fix: A bug fix.

docs: Documentation changes.

 
