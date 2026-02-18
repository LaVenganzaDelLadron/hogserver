from django.contrib import admin
from .models import User

# Register your models here.


admin.site.header = "Profile Admin"
admin.site.site_title = 'Profile Admin'
admin.site.index_title = 'Profile Admin'


class UserAdmin(admin.ModelAdmin):
    list_display = ['user_fname', 'user_lname', 'user_email','user_position']
    search_fields = ['user_fname', 'user_lname', 'user_email','user_position']

admin.site.register(User, UserAdmin)
