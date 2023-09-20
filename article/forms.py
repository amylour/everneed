from .models import Article
from slugify import slugify
from django import forms
from djrichtextfield.widgets import RichTextWidget


class ArticleForm(forms.ModelForm): 
    """ Form to create/edit an article """
    title = forms.CharField(max_length=200)

    excerpt = forms.CharField(widget=forms.Textarea(attrs={"rows": 5}))

    content = forms.CharField(widget=RichTextWidget())

    class Meta:
        model = Article
        fields = ['title', 'image_alt', 'excerpt', 'content']

        labels = {
            "title": "Article Title",
            "image_alt": "Describe Image",
            "excerpt": "Excerpt",
            "content": "Content",
        }

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.slug = slugify(instance.title)
        if commit:
            instance.save()
        return instance
