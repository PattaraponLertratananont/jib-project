from django.urls import path

# from rest_framework.routers import DefaultRouter

from .views import (
    WorkerListView
    # WorkerModeViewSetView
)

# router = DefaultRouter()
# router.register(r'', WorkerModeViewSetView)


urlpatterns = [
    path('', WorkerListView.as_view()),
    # path('', include(router.urls)),
]
