from django.contrib import admin

# Register your models here.
from .models import Carlist,Showeroom_model,Review

admin.site.register(Carlist)
admin.site.register(Showeroom_model)
admin.site.register(Review)