from django.contrib import admin

from .models import FAQ



@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('question', 'question_hi', 'answer_hi', 'question_en', 'answer_en')
    search_fields = ('question', 'question_hi', 'answer_hi', 'question_en', 'answer_en')