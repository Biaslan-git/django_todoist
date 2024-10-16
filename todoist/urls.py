from django.urls import path
from .views import StartPageView, TodoistView


urlpatterns = [
    path('', StartPageView.as_view(), name='start_page'),
]
