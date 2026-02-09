from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from website.forms import ContactForm, NewsletterForm
# Create your views here.


def index(request):
    return render(request, 'website/index.html')

def shop(request):
    return render(request, 'website/shop.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if  form.is_valid():
            form.save()

    form = ContactForm()
    context = {'form':form}
    return render(request, 'website/contact.html', context)

def newsletter(request):
    if request.method == "POST":
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
    form = NewsletterForm()
    return HttpResponseRedirect('/')


def shopping_cart(request):
    return render(request, 'website/shopping-cart.html')

def check_out(request):
    return render(request, 'website/check-out.html')

def faq(request):
    return render(request, 'website/faq.html')


def product(request):
    return render(request, 'website/product.html')

def about_us(request):
    return render(request, 'website/about-us.html')

def services(request):
    return render(request, 'website/services.html')



def test(request):
    return HttpResponse('<h1>salam</h1>')

