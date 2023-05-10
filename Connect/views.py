from django.views import View
from django.shortcuts import render
from .models import CallbackRequest
from .forms import ContactForm
from django.http import HttpResponseRedirect
from django.core.mail import send_mail, BadHeaderError
from django.conf import settings
from django.http import HttpResponse

# Create your views here.
# class Callback(View):
#     # specify the model to use
#     model = CallbackRequest
#     fields = ('name', 'phone', 'comment')
#     template_name = '_connect.html'
#     success_url = '/'
    
#     def get(self, request, *args, **kwargs):
#         return render(request, self.template_name)

#     def post(self, request, *args, **kwargs):
#         form = self.model(request.POST)
#         if form.is_valid():
#             # <process form cleaned data>
#             return HttpResponseRedirect('/')

#         return render(request, self.template_name, {'form': form})

def Callback_view(request):
        if request.method == 'POST':
                success = False
                form = ContactForm(request.POST)
                if form.is_valid():
                        form.save()
                        success = True
                        return render(request, '_connect.html')

        form = ContactForm()
        context = {'form': form}
        return render(request,'_connect.html',context)
#     def form_valid(self, form):
#         success = False        
#         subject = "Website Inquiry" 
#         body = {
#                 'name': form.cleaned_data['name'],  
#                 'mobile': form.cleaned_data['phone'], 
#                 'comment': form.cleaned_data['comment'], 
#                 'callback URL': self.request.get_full_path
#                 }
#         message = "\n".join(body.values())
#         self.object = form.save()
#         try:
#                 send_mail(subject, message, settings.Email_HOST_USER, ['codesquare01@gmail.com',])                 
#         except BadHeaderError:
#                 return HttpResponse('Invalid header found.')
#         success = True
#         return super(self).form_valid(form)
        
        
