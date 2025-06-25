from django.urls import path
from main import views

urlpatterns = [
    path('poems/test/', views.poem_test_view, name='test'),
]