from rest_framework import serializers

from django.conf import settings
from . import models


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Note
        fields = ['id', 'title', 'content']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        if data['title'] == '':
            data['title'] = data['content'][:min(len(data['content']), settings.TITLE_LENGTH)]
        return data
