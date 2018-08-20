from django import forms
from .models import Comment, Post


class PostSearchForm(forms.Form):
    search_word = forms.CharField(label='Search Word')

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = (
            'content',
        )
        widgets = {
            'content': forms.TextInput(
                attrs={
                    'class': 'content',
                    'placeholder': '댓글 달기...',
                }
            )
        }

    def clean_content(self):
        data = self.cleaned_data['content']
        errors = []
        if data == '':
            errors.append(forms.ValidationError('댓글 내용을 입력해주세요'))
        elif len(data) > 50:
            errors.append(forms.ValidationError('댓글 내용은 50자 이하로 입력해주세요'))
        if errors:
            raise forms.ValidationError(errors)
        return data