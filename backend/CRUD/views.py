from django.forms import model_to_dict
from django.db import IntegrityError
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.core.files.storage import FileSystemStorage
import json

from CRUD.models import *

# Create your views here.

@csrf_exempt
def model_api(request, model_name, id=None):
    """
    通用的``model``的CRUD

    :param ``request``: 請求
    :param ``model_name``: ``model``的名稱
    :param ``id``: 指定要刪除的資料的``id``

    :return: ``JsonResponse``
    """

    def data_from_frontend():
        """
        前端傳來的Ajax資料
        """
        if request.FILES:
            if 'file' in request.FILES:
                img_file = request.FILES['file']
                fs = FileSystemStorage(location='product/')
                fs.save(img_file.name, img_file)

        if request.POST:
            posts = {}
            for field in request.POST:
                posts[field] = request.POST[field]

            return posts
        else:
            try:
                return json.loads(request.body.decode('utf-8'))
            except:
                return False
    
    # 從global namespace找model
    try:
        model = globals()[model_name]
    except KeyError:
        return JsonResponse({'success': False, 'error': 'Invalid model name'})

    model_queryset = model.objects

    # 取得全部或者有參數條件的資料
    if request.method == 'GET':
        params = request.GET.dict()

        queryset = None
        if params:
            queryset = model_queryset.filter(**params)
        else:
            queryset = model_queryset.all()
        

        if not queryset:
            return JsonResponse({'success': False, 'error': '查無資料'})
        
        querylist = list(queryset.values())
        
        return JsonResponse({'success': True, 'data': querylist}, safe=False)
    # 新增資料 從HTTPRequest的body中的資料
    elif request.method == 'POST':
        try:
            instance = model_queryset.create(**data_from_frontend())
            return JsonResponse({'success': True, 'data': model_to_dict(instance)}, safe=False)
        except IntegrityError:
            return JsonResponse({'success': False, 'error': '不可重複'}, safe=False)
    # 修改資料 從HTTPRequest的body中的資料
    elif request.method == 'PUT':
        frontend_data = data_from_frontend()

        if type(frontend_data) == list:
            response_instance = []
            for data in frontend_data:
                instance = model_queryset.filter(id=data['id']).first()
                if not instance:
                    return JsonResponse({'success': False, 'error': 'id:' + data['id'] + ' 查無資料'})
                
                for key, value in data.items():
                    setattr(instance, key, value)

                instance.save()
                response_instance.append(model_to_dict(instance))
        else:
            instance = model_queryset.filter(id=frontend_data['id']).first()
            if not instance:
                return JsonResponse({'success': False, 'error': '查無資料'})
            
            for key, value in frontend_data.items():
                setattr(instance, key, value)

            instance.save()
            response_instance = model_to_dict(instance)

        return JsonResponse({'success': True, 'data': response_instance}, safe=False)
    # 刪除資料 依照id刪除資料
    elif request.method == 'DELETE':
        instance = model_queryset.filter(id=id).first()
        if not instance:
            return JsonResponse({'success': False, 'error': '查無資料'})
        
        instance.delete()
        return JsonResponse({'success': True, 'message': '刪除成功'})
    else:
        return JsonResponse({'success': False, 'error': '請求方法錯誤'})