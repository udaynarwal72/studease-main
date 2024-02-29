from django.contrib import admin
# we imported contact through this..
from studease.models import contact
from studease.models import loginDetails
# Register your models here.
admin.site.register(contact) #registered our model through this..¸
admin.site.register(loginDetails)