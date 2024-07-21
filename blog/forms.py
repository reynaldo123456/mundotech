from django import forms

from .models import Blog

from ckeditor.fields import RichTextField

class TextForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea, required=True)
    name = forms.CharField(widget=forms.Textarea, required=True)
    email = forms.CharField(widget=forms.Textarea, required=True)
    time_begin = forms.DateTimeField(widget=forms.DateInput, required=True)
    time_final = forms.DateTimeField(widget=forms.DateInput, required=True)
    topic = forms.CharField(widget=forms.Textarea, required=True)

class AddBlogForm(forms.ModelForm):
    #description = RichTextField()
    
    class Meta:
        model = Blog
        fields = (
            "title",
            "category",
            "banner",
            "description",
            "CCI",
            "price",
        )