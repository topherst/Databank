from django.contrib import admin
from .models import NotePost

class NotePostAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "status", "created_on")
    list_filter = ("status",)
    search_field = ["title", "content"]
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(NotePost, NotePostAdmin)
