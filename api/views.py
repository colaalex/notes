from django.shortcuts import render
from django.db.models import Q
from rest_framework import generics

from . import models
from .serializers import NoteSerializer


class NoteView(generics.ListCreateAPIView):
    queryset = models.Note.objects.all()
    serializer_class = NoteSerializer

    def get_queryset(self):
        query = self.request.GET.get('query', None)
        if query:
            qs = models.Note.objects.filter(Q(title__icontains=query) | Q(content__icontains=query))
            return qs
        return super(NoteView, self).get_queryset()


class NoteDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Note.objects.all()
    serializer_class = NoteSerializer
