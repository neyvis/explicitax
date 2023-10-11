from django.utils.translation import gettext_lazy as _
from django import forms

from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)

        labels = {
            "title": _("frase"),
            "text": _("descripción"),
        }
        help_texts = {
            "title": _("Escriba una frase que le guste."),
        }
        error_messages = {
            "title": {
                "max_length": _("Título demaciado largo"),
            },
        }