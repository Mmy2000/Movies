from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from . models import All , AllImages , Category , Language


class SomeModelAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = '__all__'


admin.site.register(All,SomeModelAdmin)
admin.site.register(AllImages)
admin.site.register(Category)
admin.site.register(Language)


