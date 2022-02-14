from django import forms
from main.models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['subject', 'content']
        
        widgets = {
            'subject' : forms.TextInput(attrs={'class':'form-control'}),
            'content' : forms.Textarea(attrs={'class': 'form-control', 'rows': 10})
        }

        labels = {
            'subjects':'제목',
            'content': '내용',
        }