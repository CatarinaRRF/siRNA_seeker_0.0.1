from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('search/', views.teste_view, name='search'),
    path('loading/', views.loading, name='loading'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('docs/', TemplateView.as_view(template_name='documentacion.html'), name='docs')
]