from django.forms import ModelForm

from apps.quiz.models import Question, Winner


class QuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = ()


class WinnerForm(ModelForm):
    class Meta:
        model = Winner
        fields = ('name', 'image')


