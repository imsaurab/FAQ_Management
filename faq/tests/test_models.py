import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'faq_project.settings')



import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from faq.models import FAQ

@pytest.mark.django_db
def test_faq_translation():
    faq = FAQ.objects.create(question="What is your name?", answer="My name is saurabh.")
    assert faq.get_translated_question('hi') == faq.question_hi

@pytest.mark.django_db
def test_faq_api():
    client = APIClient()
    response = client.get('/api/faqs/?lang=hi')
    assert response.status_code == 200
    