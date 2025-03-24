import json
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from ai.models import AIResult
from . import metrics


@login_required(login_url='login')
def home(request):
    product_metrics = metrics.get_product_metrics()
    sales_metrics = metrics.get_sales_metrics()
    graphic_product_category_metric = metrics.get_graphic_product_category_metric()
    graphic_product_brand_metric = metrics.get_graphic_product_brand_metric()
    daily_sales_data = metrics.get_daily_sales_data()
    daily_sales_quantity_data = metrics.get_daily_sales_quantity_data()
    ai_result = AIResult.objects.first()
    if ai_result is not None:
        ai_result = ai_result.result
    else:
        ai_result = 'Nenhum agente disponível'

    context = {
        'product_metrics': product_metrics,
        'sales_metrics': sales_metrics,
        'product_count_by_category': json.dumps(graphic_product_category_metric),
        'product_count_by_brand': json.dumps(graphic_product_brand_metric),
        'daily_sales_data': json.dumps(daily_sales_data),
        'daily_sales_quantity_data': json.dumps(daily_sales_quantity_data),
        'ai_result': ai_result,
    }

    return render(request, 'home.html', context)
