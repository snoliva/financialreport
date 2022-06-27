from django.contrib import admin
from .models import Profile, Savings, Spends, Revenues
# Register your models here.
admin.site.register(Profile)
admin.site.register(Revenues)
admin.site.register(Spends)
admin.site.register(Savings)
