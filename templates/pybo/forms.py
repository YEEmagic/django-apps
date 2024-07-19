from django import forms
from pybo.models import Question

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question # 사용할 모델
        fields = ['subject', 'content'] # Ques-Form에서 사용할 Question 모델의 속성