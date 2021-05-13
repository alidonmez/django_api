from rest_framework import serializers
from .models import FormEntry


class FormEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = FormEntry
        fields = ('name', 'dob', 'notes','created_at', 'updated_at')

    