from django.urls import path

from .views import get_question

app_name = 'api'

urlpatterns = [
    path('', get_question),
]
