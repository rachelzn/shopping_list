from django.shortcuts import render
from django.http import HttpResponseRedirect
from main.forms import ProductForm
from django.urls import reverse
from main.models import Product
from django.http import HttpResponse
from django.core import serializers

def show_main(request):
    # fetch all Product object from the application's database
    products = Product.objects.all()

    context = {
        'name': 'Rachel Heningtyas Zanetta Erari', # My Name
        'class': 'PBP A', # My PBP Class
        'products': products
    }

    return render(request, "main.html", context)

# add a new product when the form is submitted
def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "create_product.html", context)

# return data in XML format
# This function accepts a request as the parameter
# Create a variable to store all fetched Product objects.
def show_xml(request):
    data = Product.objects.all()
    # return the previously fetched data as XML
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

# return data in JSON format
def show_json(request):
    data = Product.objects.all()
    # return the previously fetched data as JSON
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
 
# Retrieving Data Based on ID in XML and JSON Formats
def show_xml_by_id(request, id):
    # store the query result of data with a specific ID from the Product model
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
def show_json_by_id(request, id):
    # store the query result of data with a specific ID from the Product model
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")