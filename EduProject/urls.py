"""
URL configuration for EduProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
from EduApp import views
from django.conf import settings
from django.conf.urls.static import static
from EduApp.views import SearchResultsView
from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_views 


urlpatterns = [
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('admin/', admin.site.urls),
    path('',views.home, name='home'),
    path('about/',views.about, name='about'),
    path('contact/',views.contact, name='contact'),
    path('payment/',views.paymentProcess, name='payment'),
    path('email_template/',views.email_template, name='email_template'),
    path('email/',views.email, name='email'),
    path('trainerProfile/',views.trainerProfile, name='trainerProfile'),
    path('addmission/',views.admission, name='addmission'),
    path('registration/',views.registration, name='registration'),
    path('login/',views.login, name='login'),
    path("logout/",LogoutView.as_view(), name="logout"),
    path('product/<int:id>', views.product, name='product_view',),
    path('Product_desc/<int:id>', views.Product_desc,name='Product_desc'),
   
    path('confirmation/', views.confirmation, name="confirmation"),
    path('search_Result/', views.Searchresult, name="search_results"),

    path('password_reset/',auth_views.PasswordResetView.as_view(template_name="ForgetPassword/password_reset.html"),name='password_reset'),

     path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(template_name="ForgetPassword/password_reset_done.html"),name='password_reset_done'),

     path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name="ForgetPassword/password_reset_confirm.html"),name='password_reset_confirm'),

    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(template_name="ForgetPassword/password_reset_complete.html"),name='password_reset_complete'),
 
    path('success/', views.payment_success, name='payment_success'),
    
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

