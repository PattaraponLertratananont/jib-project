from django.urls import path
from .views import WorkerListView

urlpatterns = [
    path('', WorkerListView.as_view()),
]
