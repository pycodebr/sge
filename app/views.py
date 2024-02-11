import json
from django.shortcuts import render
from . import metrics


def home(request):
    product_metrics = metrics.get_product_metrics()
    sales_metrics = metrics.get_sales_metrics()
    graphic_product_category_metric = metrics.get_graphic_product_category_metric()
    graphic_product_brand_metric = metrics.get_graphic_product_brand_metric()
    context = {
        'product_metrics': product_metrics,
        'sales_metrics': sales_metrics,
        'product_count_by_category': json.dumps(graphic_product_category_metric),
        'product_count_by_brand': json.dumps(graphic_product_brand_metric),
    }
    return render(request, 'home.html', context)
