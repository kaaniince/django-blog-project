from django import forms
from blog.models import ArticlesModel
class AddArticleModelForm(forms.ModelForm):
    class Meta:
        model= ArticlesModel
        exclude=('author','slug')