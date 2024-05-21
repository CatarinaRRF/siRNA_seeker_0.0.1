from django.urls import path, include
from django.views.generic import TemplateView
from .views import SignUpView

urlpatterns = [
    #path('', views.home, name='home'),
    path('', TemplateView.as_view(template_name='main/home.html'), name='home'),
    path("accounts/signup/", SignUpView.as_view(), name="signup"),
]

