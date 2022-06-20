from django.views.generic.detail import DetailView
from django.shortcuts import render
from .models import CallbackRequest
from .forms import CallbackForm

# Create your views here.
class CallbackDetailView(DetailView):
    # specify the model to use
    model = CallbackRequest
    template_name = '_connect.html'
    
    def get_context_data(self, *args, **kwargs):
       context = super(index, self).get_context_data(*args, **kwargs)
       context['form'] = CallbackForm()
       return context

    def form_valid(self, form):
        success = False
        if self.method == "POST":
                form = CallbackForm(self.POST)
        if form.is_valid():
                subject = "Website Inquiry" 
                body = {
                        'name': form.cleaned_data['name'],  
                        'mobile': form.cleaned_data['phone'], 
                        }
                message = "\n".join(body.values())
                cb = form.save(commit=False)                
                cb.save()
                try:
                        send_mail(subject, message, {{settings.host_user}}, [{{settings.email}}]) 
                except:
                        return HttpResponse('Invalid header found.')
                #return HttpResponseRedirect('./')
        else:
                form = CallbackForm()
                if 'success' in request.GET:
                    success = True
        
