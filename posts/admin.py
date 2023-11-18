from django.contrib import admin
from .models import Post,Category,Comment
from django_summernote.admin import SummernoteModelAdmin


# custimize for admin panel
class Postadmin(SummernoteModelAdmin):
    list_display=['title','draft']
    list_filter=['title']
    search_fields=['title']
    summernote_fields = ('content',)

# Register your models here.
admin.site.register(Post,Postadmin)
admin.site.register(Category)
admin.site.register(Comment)
