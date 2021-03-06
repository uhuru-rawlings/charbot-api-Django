"""chartapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from apis.views import registration_view,login_view,getuser,resetpassword_view,getcontact,getcharts,addchat,addcontact_view
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/signup', registration_view, name="registration"),
    path('api/login', login_view, name="userlogin"),
    path('api/getuser', getuser, name="userdetails"),
    path('api/resetpassword', resetpassword_view, name="resetpassword"),
    path('api/addcontact', addcontact_view, name="addcontact"),
    path('api/contacts', getcontact, name="contacts"),
    path('api/chats', getcharts, name="chats"),
    path('api/addchats', addchat, name="addchats"),
]
