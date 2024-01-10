from django.contrib import admin
from .models import Newsletter_Subscribe

@admin.register(Newsletter_Subscribe)
class Newsletter_SubscribeAdmin(admin.ModelAdmin):
    list_display = ('lang', 'email', 'join_at')
    list_filter = ('lang', 'join_at')
    search_fields = ('email',)
    ordering = ('-join_at',)
