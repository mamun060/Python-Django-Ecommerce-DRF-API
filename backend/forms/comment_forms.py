from django import forms
from backend.models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name' , 'email' , 'comment']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control rounded-0', 'placeholder': 'Enter your name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control rounded-0', 'placeholder': 'Enter your email'}),
            'comment': forms.Textarea(attrs={'class': 'form-control rounded-0', 'rows': 4, 'placeholder': 'Enter your comment'}),
        }