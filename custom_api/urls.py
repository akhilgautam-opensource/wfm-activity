from django.urls import path
from .views import WfmActivityDetail

urlpatterns = [
    path('wfm-activity/<int:pk>/', WfmActivityDetail.as_view()),
]
