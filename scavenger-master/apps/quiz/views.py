from datetime import date, timedelta

from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import CreateView, TemplateView

from apps.quiz.forms import QuestionForm, WinnerForm
from apps.quiz.models import Question, Winner


class IndexView(TemplateView):
    template_name = 'index.html'


class QuestionsView(CreateView):
    template_name = 'questions.html'
    form_class = QuestionForm

    def form_valid(self, form):
        data = form.data
        count = 0
        for i in range(1, len(Question.objects.all())+1):
            question = Question.objects.get(question=data.get("question{}".format(i)))
            if question.answer == data.get('answer{}'.format(i)):
                count += 1
        self.request.session['count'] = count
        return redirect(reverse('badge'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['questions'] = Question.objects.all()
        return context


class BadgeView(CreateView):
    template_name = 'badge.html'
    form_class = WinnerForm

    def form_valid(self, form):
        self.object = form.save()
        if self.request.FILES.get('image'):
            self.object.image = self.request.FILES.get('image')
            self.object.save()
            self.request.session['count'] = None
        return redirect(reverse('winners'))


class WinnerView(TemplateView):
    template_name = 'winners.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        self.request.session['count'] = None
        prev_week = date.today() - timedelta(days=7)
        context['winners'] = Winner.objects.filter(created__gte=prev_week)
        return context
