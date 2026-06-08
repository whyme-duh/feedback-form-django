import os

from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from app.forms import FeedbackFormField
from django.contrib.auth.decorators import login_required
from app.models import FeedbackForm
from website import settings

def home(request):
    return render(request, 'app/home.html')

@login_required
def feedback_form(request):
    submmited = True
    if FeedbackForm.objects.filter(user = request.user).exists():
        submmited = False
    
    if request.method == "POST":
        form = FeedbackFormField(request.POST)
        if form.is_valid():
            feedback_instance = form.save(commit=False)
            feedback_instance.user = request.user
            feedback_instance.save()
            messages.success(request, f'Thank you! Your form has been sumbitted.')
            return redirect('index')
        else:
            messages.error(request, "Something went wrong, try again!")
    else:
        form = FeedbackFormField()

    return render(request, 'app/feedback.html', {'form' : form, 'submitted' : submmited})

from django.template.loader import render_to_string
from xhtml2pdf import pisa
from xhtml2pdf.files import pisaFileObject
from django.contrib.staticfiles import finders
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

@login_required
def export_form_to_pdf(request, feedback_id):
    feedback = get_object_or_404(FeedbackForm, id = feedback_id)
    if not request.user.is_staff and feedback.user != request.user:
        messages.error(request, "Sorry, you are not eligible to download it")
        return redirect('profile')
    
    pisaFileObject.getNamedFile = lambda self: self.uri

    font_path = finders.find('font/Noto_Sans_Devanagari/static/NotoSansDevanagari-Regular.ttf')

    if not font_path:
        font_path = os.path.join(settings.BASE_DIR, 'app', 'static', 'font', 'Noto_Sans_Devanagari', 'static', 'NotoSansDevanagari-Regular.ttf')
    try:
        font_path = font_path.replace('\\', '/')
        pdfmetrics.registerFont(TTFont('NotoSansDevanagari', font_path))
    except Exception as e:
        pass

    
    html_string = render_to_string('app/feedback_export_pdf.html', {'feedback': feedback, 'nepali_font_path': font_path})

    response = HttpResponse(content_type ="application/pdf")
    response["Content-Disposition"] = f'attachment; filename="Everest_Admin_Feedback_{feedback.id}.pdf"'
    pisa.CreatePDF(html_string, dest=response, encoding='utf-8')
    return response

