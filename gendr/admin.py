from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from . models import All , AllImages , AddToFavorite , Category , Category2 


class SomeModelAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = '__all__'


admin.site.register(All,SomeModelAdmin)
admin.site.register(AllImages)
admin.site.register(AddToFavorite)
admin.site.register(Category)
admin.site.register(Category2)