from django.contrib import admin
from social_bookmarking.models import Bookmark

class BookmarkAdmin(admin.ModelAdmin):
    list_display    = ('title', 'status')
    list_filter     = ('title', 'status')
    search_fields   = ('title', 'status')
    list_editable   = ('status',)

admin.site.register(Bookmark, BookmarkAdmin)

