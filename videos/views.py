from django.shortcuts import render
from . models import Video
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin

# Create your views here.
class VideoListView(ListView):
    model = Video
    #Default, takes up videos/templates/videos/video_list.html if exist 
    #template_name = 'videos/templates/videos/video_list.html' 
    #show video list in alphabetical order
    queryset = Video.objects.order_by('title')

class VideoThumbsView(ListView):
    model = Video
    template_name = "videos/video_thumbs.html"

    #to filter records by category for the thumbnail view
    # get only videos from stipulated category_id (category_id is passed in from the videos/url.py)
    def get_queryset(self):
        return Video.objects.filter(category_id = self.kwargs['category_id']).filter(is_active = True)#the last filter by is_active help delete logically

class VideoDetailsView(DetailView):
    model = Video
    template_name = "videos/video_details.html"

# using a form to create data input
class VideoCreateView(SuccessMessageMixin, CreateView):
    model = Video
    fields = ['title', 'author', 'description', 'youtube_vid', 'stars_count', 'category_id', 'skill_level_id', 'is_active' ] #tuple or list can be used
    template_name = "videos/video_forms.html" #default template name here is video_forms which is preferred because there's anpother 
    #view called update view that also needs the template
    #send back to video list after successful creation of new video details
    success_message = 'Video Added!'
    success_url = reverse_lazy('videos-list')

# using a form to delete data physically
class VideoDeleteView(SuccessMessageMixin, DeleteView):
    model = Video
    template_name = "videos/video_confirm_delete.html"
    #send back to video list after successful delete of video
    success_message = 'Video Deleted!'
    success_url = reverse_lazy('videos-list')

# using a form to edit data 
class VideoUpdateView(SuccessMessageMixin, UpdateView):
    model = Video
    fields = ['title', 'author', 'description', 'youtube_vid', 'stars_count', 'category_id', 'skill_level_id', 'is_active' ] #tuple or list can be used
    template_name = "videos/video_forms.html" #default template name here is video_forms which is preferred because there's anpother 
    #view called update view that also needs the template
    #send back to video list after successful editting of video
    success_message = 'Video Saved!'
    success_url = reverse_lazy('videos-list')

