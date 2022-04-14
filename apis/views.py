from django.shortcuts import render
from django.contrib.auth.hashers import make_password,check_password
from .serializers import RegistrationSerializer,ContactsSerializer,ChartsSerializer
from .models import Regisration,Contacts,Charts
# Create your views here.
