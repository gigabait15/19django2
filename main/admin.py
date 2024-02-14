from django.contrib import admin
from main.models import Students


#  admin.site.register(Students)


@admin.register(Students)
class StudentsAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'is_active', 'email', )
    list_filter = ('is_active', )
    search_fields = ('first_name', 'last_name', )