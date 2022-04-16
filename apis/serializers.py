from rest_framework import serializers
from .models import Regisration,Contacts,Charts

class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Regisration
        fields = ['id','username','phonenumber','userimage','is_active','is_loggedin']

class ContactsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacts
        fields = ['user','username','phonenumber']

class ChartsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Charts
        fields = ['user','sentto','message','date_sent']