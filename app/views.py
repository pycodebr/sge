from django.shortcuts import render
from . import metrics


def home(request):
    context = dict()
    context['product_metrics'] = metrics.get_product_metrics()
    context['sales_metrics'] = metrics.get_sales_metrics()
    return render(request, 'home.html', context)
