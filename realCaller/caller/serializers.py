from rest_framework import serializers
from .models import UserLog, Contacts

class UserLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserLog
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'phone')

class ContactsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacts
        fields = ('id', 'name', 'phone', 'registered_user', 'spam_count', 'email')
