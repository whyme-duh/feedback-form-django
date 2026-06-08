from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.views import LoginView
from user.forms import UserRegistrationForm
from app.models import FeedbackForm



def sign_up(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('signin')   
    else:
        form = UserRegistrationForm()

    return render(request, 'user/signup.html', {'form': form })


def profile(request):

    feedbacks = FeedbackForm.objects.filter(user = request.user)

    has_submitted = feedbacks.exists()

    if has_submitted:  
        feedback = feedbacks.first()
    else:
        feedback = FeedbackForm()      
    return render(request, 'user/profile.html', {'feedback' : feedback, 'has_submitted' : has_submitted})