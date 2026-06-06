

from django.urls import path
from app.views import feedback_form, home


urlpatterns =[
    path('', home, name='index'),
    path('feedback-form/', feedback_form, name='feedback'),
] 
