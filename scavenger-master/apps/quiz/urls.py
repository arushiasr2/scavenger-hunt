from django.urls import path

from apps.quiz import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('questions', views.QuestionsView.as_view(), name='question'),
    path('result', views.BadgeView.as_view(), name='badge'),
    path('winners', views.WinnerView.as_view(), name='winners'),
]
