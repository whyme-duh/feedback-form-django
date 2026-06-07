

from django.urls import path
from app.views import feedback_form, home, export_form_to_pdf


urlpatterns =[
    path('', home, name='index'),
    path('feedback-form/', feedback_form, name='feedback'),
    path('feedback/download/<int:feedback_id>/', export_form_to_pdf, name='download_feedback_pdf'),
] 
