from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'app/home.html')

def feedback_form(request):
    return render(request, 'app/feedback.html')