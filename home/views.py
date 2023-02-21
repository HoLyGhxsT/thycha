from django.http import JsonResponse
from django.views.generic import TemplateView,View
from .models import (PortfolioMaster)
from django.template.loader import render_to_string
from django.shortcuts import render

# Create your views here.
class HomePageView(TemplateView):
    template_name = "home.html"
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        
        return context
    
class ContactPageView(TemplateView):
    template_name = "contact.html"
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        
        return context
    
class AboutPageView(TemplateView):
    template_name = "about.html"
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        
        return context
    
class OurTeamPageView(TemplateView):
    template_name = "team.html"
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        
        return context

# class PortfolioView(TemplateView):
#     template_name = "portfolio.html"
#     def post(self, request):
#         context = {}
#         # itemlist = PortfolioMaster.objects.values('id','id__id','id__name','id__name','id__desc','id__thumbnailimage')
#         itemlist = PortfolioMaster.objects.all()
#         context = {
#             'itemlist':itemlist.distinct()
#         }
#         html = render_to_string('portfolio.html',context)
#         return JsonResponse({'STATUS':1,'html':html})

def PortfolioView(request):
    itemlist = PortfolioMaster.objects.all()
    return render(request, "portfolio.html", {"itemlist":itemlist})
    
class MoreView(TemplateView):
    template_name = "render/more.html"
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        
        try:
            context['item'] = PortfolioMaster.objects.filter(id=self.request.GET.get('item')).values('image1','image2','image3','image4','image5','image6','image7','image8')[0]
        except:
            pass
        return context