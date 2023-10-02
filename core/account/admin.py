from django.contrib import admin
from .models import Profile, Department
# Register your models here.

admin.site.register(Department)


class ProfileAdmin(admin.ModelAdmin):
    list_display = ["user", "phone_number", "department"]
    list_filter = ["department"]
    search_fields = ["phone_number"]


admin.site.register(Profile, ProfileAdmin)