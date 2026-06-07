from django.shortcuts import redirect, render
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
    feedback = FeedbackForm.objects.get(user = request.user)

    return render(request, 'user/profile.html', {'feedback' : feedback})