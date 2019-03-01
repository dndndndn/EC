from django.shortcuts import render, HttpResponse
from django.shortcuts import redirect
from django.urls import reverse
from django.http import FileResponse, StreamingHttpResponse, JsonResponse
from . import models as login_models
from android import models as android_models
import hashlib
import os
import json
from openpyxl import load_workbook
from django.core.paginator import Paginator
from EC.settings import MEDIA_ROOT
import re
# Create your views here.
def resources_get(request, path):
    path = re.sub(r'-', r'\\', path)
    file_path = os.path.join(MEDIA_ROOT, path)
    print(file_path, 'yes')
    try:
        data = request.GET
        file_name = data.get("file_name")
        with open(file_path, 'rb') as f:
            image_data = f.read()
        return HttpResponse(image_data, content_type="image/png")
    except Exception as e:
        print(e)
        return HttpResponse(str(e))
