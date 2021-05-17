from django.forms import ModelForm, DateInput
from .models import Post


class CreatePostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['author', 'type', 'date', 'title', 'text']
        widgets = {
            'date': DateInput(attrs={'type': 'date'})
        }
