from django.urls import path

from music import views

urlpatterns = [
    path('labs/create/', views.LabCreateView.as_view(), name='create'),
    path('labs/<int:pk>/', views.LabDetailView.as_view(), name='detail'),
    path('history/', views.LabHistoryView.as_view(), name='history'),
]
