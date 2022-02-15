from django import forms
from main.models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['subject', 'content']
        labels = {
            'subjects':'제목',
            'content': '내용',
        }