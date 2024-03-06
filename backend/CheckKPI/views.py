from django.db.models import Sum, F
from django.db.models.functions import Round
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json

from CRUD.models import *

# Create your views here.

@csrf_exempt
def check_api(request, type):
    """
    通用的``model``的CRUD

    :param ``request``: 請求
    :param ``type``: 查詢的形式

    :return: ``JsonResponse``
    """

    if type == 'Popular':
        queryset = OrderDetail.objects.values('product__name').annotate(sales_quantity=Sum('quantity')).order_by('-sales_quantity')[:10]
        
        if not queryset:
            return JsonResponse({'success': False, 'error': '查無資料'})
        
        querylist = list(queryset)
        
        return JsonResponse({'success': True, 'data': querylist}, safe=False)
    elif type == 'TotalSales':
        queryset = OrderDetail.objects.values('product__name').annotate(
            total_sales=Sum(Round(F('quantity') * F('product__price')), output_field=models.IntegerField())
        ).order_by('-total_sales')[:10]
        
        if not queryset:
            return JsonResponse({'success': False, 'error': '查無資料'})
        
        querylist = list(queryset)
        
        return JsonResponse({'success': True, 'data': querylist}, safe=False)