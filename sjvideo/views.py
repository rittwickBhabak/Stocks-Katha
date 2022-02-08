from dataclasses import fields
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.views.generic import TemplateView, UpdateView, DetailView, DeleteView, CreateView, ListView
from .models import Video

class Home(ListView):
    model = Video 

class AllNote(ListView):
    template_name=  'sjvideo/note_list.html'
    model = Video 

class AddLesson(CreateView):
    fields = "__all__"
    model = Video 

class ViewLesson(DetailView):
    model = Video 

class UpdateLesson(UpdateView):
    fields = "__all__"
    model = Video 

def update_notes(request, pk):
    if request.method == 'POST':
        video = get_object_or_404(Video, pk=pk)
        notes = request.POST.get('notes')
        if len(notes.strip()):
            video.notes = notes 
            video.save()
            return JsonResponse({"status": "saved"})
    return JsonResponse({"status": "notupdated"})

def update_download_url(request, pk):
    if request.method == 'POST':
        video = get_object_or_404(Video, pk=pk)
        download_url = request.POST.get('download_url')
        video.download_url = download_url 
        video.save()
        return JsonResponse({"status": "saved", "new_url": video.download_url})
    return JsonResponse({"status": "notupdated"})
