from django.shortcuts import render
from django.contrib import messages
from app.forms import FeedbackFormField

# Create your views here.
def home(request):
    return render(request, 'app/home.html')

def feedback_form(request):
    if request.method == "POST":
        form = FeedbackFormField(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Thank you! Your form has been sumbitted.')
        else:
            messages.error(request, "Something went wrong, try again!")
    else:
        form = FeedbackFormField()

    return render(request, 'app/feedback.html', {'form' : form})