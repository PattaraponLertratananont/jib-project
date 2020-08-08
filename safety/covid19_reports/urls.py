from django.urls import include,path
from .views import Covid19ReportView

urlpatterns = [
    path('', Covid19ReportView.as_view()),
]