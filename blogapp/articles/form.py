from django import forms
from .models import Article


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content']
        
    def clean(self):
        data = self.cleaned_data
        title = data.get("title")
        qs = Article.objects.filter(title=title)
        if qs.exists():
            self.add_error("title", f"This \'{title}\' is already exists")
        return data

class ArticleFormOld(forms.Form):
    title = forms.CharField()
    content = forms.CharField()
    
    def clean_title(self):
        cleaned_data = self.cleaned_data
        title = self.cleaned_data.get("title")
        return title
    
    def clean(self):
        cleaned_data = self.cleaned_data
        print("All Data : " + str(cleaned_data))
        return cleaned_data
        