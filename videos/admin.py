from django.contrib import admin
from videos.models import Video
# Register your models here.
#Allows you to access database through the admin page
admin.site.register(Video)

#another way to register a model with specificity to what fields are to be shown on django admin page
# class VideoLt(admin.ModelAdmin):
#     list_display = [
#         'title', 'author', 'description', 'youtube_vid', 'stars_count', 'category_id', 'skill_level_id', 'is_active'
#     ]
#admin.site.register(Video, VideoLt)