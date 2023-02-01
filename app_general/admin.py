from django.contrib import admin
from .models import Video
from embed_video.admin import AdminVideoMixin
from app_general.models import Contact,Course
# Register your models here.
class AdminVideo(AdminVideoMixin, admin.ModelAdmin):
    pass

admin.site.register(Video ,AdminVideo)
admin.site.register(Contact)
admin.site.register(Course)