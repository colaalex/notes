from django.urls import path

from .views import NoteView, NoteDetails


urlpatterns = [
    path('', NoteView.as_view()),
    path('<int:pk>', NoteDetails.as_view())
]
