from django.contrib import admin
from .models import Room,Message
# Register your models here.


admin.site.register(Room)
admin.site.register(Message)

#login to admin web using 127.0.0.1:8000/admin