from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from app.forms import FeedbackFormField
from django.contrib.auth.decorators import login_required
from app.models import FeedbackForm

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

@login_required
def export_form_to_pdf(request, feedback_id):
    feedback = get_object_or_404(FeedbackForm, id = feedback_id)
    if not request.user.is_staff and feedback.user != request.user:
        messages.error(request, "Sorry, you are not eligible to download it")
        return redirect('profile')
    
    html_string = render_to_string('app/feedback_export_pdf.html', {'feedback' : feedback})

    response = HttpResponse(content_type ='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="Everest_Feedback_{feedback.id}.pdf"'

    pisa_status = pisa.CreatePDF(html_string, dest=response)

    if pisa_status.err:
           return HttpResponse("We ran into a formatting error", status=500)

    return response
