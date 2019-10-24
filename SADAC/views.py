from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import View


from .forms import ContactForm
from django.shortcuts import render, get_object_or_404
from .models import Blog

def allblogs(request):
    blogs = Blog.objects
    return render(request, 'SADAC/allblogs.html', {'blogs':blogs})

def detail(request, blog_id):
    blogdetail = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'SADAC/detail.html', {'blog':blogdetail})

class HomeView(TemplateView):
    template_name = 'SADAC/index.html'

class IndustryView(TemplateView):
    template_name = 'SADAC/industries.html'

    
class AboutView(TemplateView):
    template_name = 'SADAC/about.html'


def contact(request):
    template = 'SADAC/contact.html'

    if request.method == "POST":
        form = ContactForm(request.POST)

        if form.is_valid():
            form.save()
            form = ContactForm()

    else:
        form = ContactForm()

    context ={
        'form' : form,
    }
    return render(request, template, context)







# def contact(request):
#     Contact_form = ContactForm
#     if request.method == 'POST':
#         form = Contact_form(data = request.POST)
#
#         if form.is_valid():
#             contact_name = request.POST.get('name')
#             contact_email = request.POST.get('email')
#             contact_content = request.POST.get('message')
#
#
#             content ={
#                 'contact_name' : request.POST.get('name'),
#                 'contact_email' : request.POST.get('email'),
#                 'contact_content' : request.POST.get('message'),
#             }
#             email = EmailMessage(
#             "New Contact Form Message",
#             content,
#             "SADAC" + '',
#             ['mutwiri333@gmail.com'],
#             header = {'Reply to ': contact_email}
#             )
#         email.send()
#         return redirect('SADAC:contact')
#     return render(request, 'SADAC/contact.html', {'form': Contact_form})
