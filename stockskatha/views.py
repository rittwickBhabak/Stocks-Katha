from django.views.generic import TemplateView
from blog.models import Post 

class Home(TemplateView):
    template_name='index.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["post_list"] = Post.objects.all().order_by('-edited_at')
        return context
    
    