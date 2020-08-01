from django import forms
from django.forms.utils import ErrorList

from .models import Article
from django.utils import timezone
from django.conf import settings


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        # fields = ['article_author', 'article_title', 'article_text', 'article_create_date',
        # 'article_published_date', 'article_image']
        fields = "__all__"
        widgets = {
            'article_author': forms.TextInput(attrs={'class': 'form-control'}),
            'article_title': forms.TextInput(attrs={'class': 'form-control'}),
            'article_text': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, data=None, files=None, auto_id='id_%s', prefix=None,
                 initial=None, error_class=ErrorList, label_suffix=None,
                 empty_permitted=False, instance=None, use_required_attribute=None,
                 renderer=None):
        super().__init__(data=None, files=None, auto_id='id_%s', prefix=None, initial=None, error_class=ErrorList,
                         label_suffix=None, empty_permitted=False, instance=None, use_required_attribute=None,
                         renderer=None)
        self.article_published_date = timezone.now()

    def __str__(self):
        return self.article_title

    def published(self):
        self.save()

    # class Meta:
    # verbose_name = 'Статья'
    # verbose_name_plural = 'Статьи'
