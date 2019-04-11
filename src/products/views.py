from django.views.generic import ListView,DetailView
from django.shortcuts import render, get_object_or_404
from django.http import request
from .models import product

class ProductListView(ListView):
    queryset = product.objects.all()
    template_name = "products/list.html"
    
    # def get_context_data(self, *args, **kwargs ):
    #     context = super(ProductListView, self).get_context_data(*args, **kwargs)
    #     print(context)
    #     return context

def product_list_view(request):
    queryset = product.objects.all()
    context = {
        'object_list':queryset,
    }
    return render(
        request,
        "products/list.html",
        context
        )


class ProductDetailView(DetailView):
    queryset = product.objects.all()
    template_name = "products/detail.html"
    
    def get_context_data(self, *args, **kwargs ):
        context = super(ProductDetailView, self).get_context_data(*args, **kwargs)
        print(context)
        return context

def product_detail_view(request, pk =None, *args, **kwargs):
    # object = product.objects.get(pk=pk)
    # instance = get_object_or_404(product,pk=pk)
    try:
        instance = products.objects.get(id=4)
    except product.DoesNotExist:
        print("no products here")
    except:
        print("huh?")
    
    qs = product.objects.filter(id=pk)
    if qs.exists() and qs.count() == 1:
        instance = qs.first()
    else:
        raise Http404("product doesn't exist")

    context = {
        'object':instance,
    }
    return render(
        request,
        "products/detail.html",
        context
        )