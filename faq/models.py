from django.db import models

from ckeditor.fields import RichTextField
from django.utils.translation import gettext_lazy as _
from googletrans import Translator
from django.core.cache import cache

def translate_text(text, dest_lang):
    translator = Translator()
    try:
        translation = translator.translate(text, dest=dest_lang)
        return translation.text
    except Exception as e:
        print(f"Translation failed: {e}")
        return text  # Fallback to the original text if translation fails

class FAQ(models.Model):
    id = models.AutoField(primary_key=True)  # Explicit primary key
    question = models.TextField(_("Question"))
    answer = RichTextField(_("Answer"))
    question_hi = models.TextField(_("Question (Hindi)"), blank=True, null=True)
    answer_hi = RichTextField(_("Answer (Hindi)"), blank=True, null=True)
    question_en = models.TextField(_("Question (English)"), blank=True, null=True)
    answer_en = RichTextField(_("Answer (English)"), blank=True, null=True)
    def get_translated_question(self, lang):
        """
        Retrieve the translated question based on the language code.
        Fallback to the default question if the translation is not available.
        """
        return getattr(self, f"question_{lang}", self.question)

    def get_translated_answer(self, lang):
        """
        Retrieve the translated answer based on the language code.
        Fallback to the default answer if the translation is not available.
        """
        return getattr(self, f"answer_{lang}", self.answer)
    

    def save(self, *args, **kwargs):
        # Automatically translate the question and answer into Hindi and Bengali
        if not self.question_hi:
            self.question_hi = translate_text(self.question, 'hi')
        if not self.answer_hi:
            self.answer_hi = translate_text(self.answer, 'hi')
        if not self.question_en:
            self.question_en = translate_text(self.question, 'en')
        if not self.answer_en:
            self.answer_en = translate_text(self.answer, 'en')
        super().save(*args, **kwargs)
        
    def __str__(self):
        return self.question
    


def get_translated_question(self, lang):
    cache_key = f"faq_{self.id}_question_{lang}"
    cached_question = cache.get(cache_key)
    if cached_question:
        return cached_question
    translated_question = getattr(self, f"question_{lang}", self.question)
    cache.set(cache_key, translated_question, timeout=60 * 60)  # Cache for 1 hour
    return translated_question    