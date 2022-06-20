from django.contrib import admin
from .models import CallbackRequest

# Register your models here.
class CallbackRequestAdmin(admin.ModelAdmin):
    list_display = ["request_date","name"]

admin.site.register(CallbackRequest,CallbackRequestAdmin)