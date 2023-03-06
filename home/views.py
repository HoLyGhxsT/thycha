from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.views.generic import TemplateView,View
from .models import (PortfolioMaster)
from django.core.mail import send_mail
from django.contrib import messages

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
# def ContactPageView(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         c_name = request.POST.get('c-name')
#         telno = request.POST.get('telno')
#         subject = request.POST.get('subject')
#         messageContent = request.POST.get('message')
        
#         data = {
#             'name': name,
#             'email': email,
#             'c_name': c_name,
#             'telno': telno,
#             'subject': subject,
#             'message': messageContent
#         }
        
#         print(data)
#         message = '''
#         Message: {}

#         From: {}
#         Name: {}
#         Company Name: {}
#         Contact No.: {}

#         '''.format(data['message'],data['email'],data['name'],data['c_name'],data['telno'])
#         try:
#             if(send_mail(data['subject'], message, '', ['faketest4410@gmail.com'])):
#                 messages.success(request, 'Thanks for contacting! We will get in touch with you soon')
#                 data = {}
#             else:
#                 messages.success(request, 'Not Allowed')
#             # return render(request, 'contact.html', context={messages})
#             return HttpResponseRedirect('/contact-us')
#         except:
#             messages.success(request, 'Something Went Wrong!, Please try again after sometime or use whatsapp')
#         data = {}
#     return render(request, "contact.html", {})
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