"""
URL configuration for website project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.urls import include, path
from website import settings
from django.conf.urls.static import static
from user.views import sign_up, profile

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),
    path('signup/', sign_up, name = 'signup'),
    path('signin/', auth_views.LoginView.as_view(template_name = "user/signin.html" , redirect_authenticated_user = True), name ='signin'),
    path('logout/', auth_views.LogoutView.as_view(template_name = "user/signin.html" ), name ='logout'),
    path('profile/', profile , name ='profile'),
] 
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
