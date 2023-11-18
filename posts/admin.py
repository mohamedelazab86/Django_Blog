from django.contrib import admin
from .models import Post,Category,Comment


# custimize for admin panel
class Postadmin(admin.ModelAdmin):
    list_display=['title','draft']
    list_filter=['title']
    search_fields=['title']

# Register your models here.
admin.site.register(Post,Postadmin)
admin.site.register(Category)
admin.site.register(Comment)
