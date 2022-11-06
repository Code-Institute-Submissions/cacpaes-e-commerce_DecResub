from .models import Comment
from django import forms



class CommentForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label="Name", max_length=80)
    email = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label="Email")
    body = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}), label="Comment")

    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')
