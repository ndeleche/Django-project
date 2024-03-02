from django.contrib import admin
from .models import Member

# Register your models here.


# admin.site.register(Member)

class MemberAdmin(admin.ModelAdmin):
    # list_editable = ()
    list_per_page = 5
    list_max_show_all = 5
    list_display = ('first_name', 'last_name', 'joined_date')


admin.site.register(Member, MemberAdmin)
