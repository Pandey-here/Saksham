"""saksham_latest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings


urlpatterns = [
    #path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('login/',views.user_login,name='user_login'),
    path('signup/',views.user_signup,name='user_signup'),
    path('donate/',views.donate,name='donate'),
    path('submit/',views.success,name='success'),
    #path('current/',views.current,name='current'),
    path('logout/',views.user_logout,name='user_logout'),
    path('gallary/',views.gallary2,name='gallary'),
    path('blog/',views.blog, name='blog'),
    path('upload/',views.upload, name='upload'),
    path('sitemap.xml',views.sitemap,name='sitemap'),





###EMAIL CONFIGURATION
#for changing password via email

    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name='home/reset_password_sent.html'),name='password_reset_done'),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='home/reset_password.html'),name='password_reset_confirm'),
    path('reset_password/',auth_views.PasswordResetView.as_view(template_name='home/changepass.html'), name='reset_password'),

    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='home/password_reset_confirm.html'),name='password_reset_complete'),

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


# urlpatterns +=staticfiles_urlpatterns()
