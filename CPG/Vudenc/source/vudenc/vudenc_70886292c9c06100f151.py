from rest_framework import serializers
from rest_framework.validators import ValidationError
from .models import Message
"""
    Message Serializer class
    """
model = Message
fields = 'sent_by', 'room', 'text', 'attachment'
