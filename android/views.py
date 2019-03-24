import hashlib
import json
import os
import re
import zipfile

from django.http import JsonResponse
from django.shortcuts import HttpResponse
from ranged_response import RangedFileResponse

from EC.settings import MEDIA_ROOT
from login import models as login_models


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
        return HttpResponse("你好")


def get_zip_file(input_path, result):
    files = os.listdir(input_path)
    for file in files:
        if os.path.isdir(input_path + '/' + file):
            get_zip_file(input_path + '/' + file, result)
    else:
        result.append(input_path + '/' + file)


def zip_file_path(input_path, output_path, output_name):
    """
    压缩文件
    :param input_path: 压缩的文件夹路径
    :param output_path: 解压（输出）的路径
    :param output_name: 压缩包名称
    :return:
    """
    f = zipfile.ZipFile(output_path + '\\' + output_name, 'w', zipfile.ZIP_DEFLATED)
    filelists = []
    get_zip_file(input_path, filelists)
    for file in filelists:
        f.write(file, file.replace(r'G:\server\EC\store\question', '').replace('\\', ''))
        print(file.replace(r'G:\server\EC\store\question', '').replace('\\', ''), file)
    # 调用了close方法才会保证完成压缩
    f.close()
    return output_path + r"/" + output_name


def question_download(request, ID):
    path = os.path.join(MEDIA_ROOT, 'question')
    path = os.path.join(path, str(ID))
    output_path = os.path.join(MEDIA_ROOT, 'download')
    file_name = str(ID) + '.zip'
    if os.path.exists(path):
        zip_file_path(path, output_path, file_name)
        file_path = os.path.join(output_path, file_name)
        """
        def file_itertor(file_path, chunk_size=512):
            with open(file_path, 'rb') as f:
                while True:
                    c = f.read(chunk_size)
                    if c:
                        yield c
                    else:
                        break

        response = StreamingHttpResponse(file_itertor(file_path))
        response['Content-Type'] = 'application/octet-stream'
        response['Content-Length'] = os.path.getsize(file_path)
        response['Content-Disposition'] = 'attachment;filename="{0}"'.format(file_name)
        return response

        """
        response = RangedFileResponse(request, open(file_path, 'rb'), content_type='audio/wav')
        response['Content-Disposition'] = 'attachment;filename="{0}"'.format(file_name)
        return response
    else:
        return HttpResponse("bad request")


def hash_code(s, salt='mysite'):
    h = hashlib.sha256()
    s += salt
    h.update(s.encode())
    return h.hexdigest()


def login(request):
    if request.method == "POST":
        receive_data = json.loads(request.body.decode())
        username = receive_data['name']
        password = receive_data['password']
        print(username, password)
        try:
            user = login_models.User.objects.get(name=username)
            if user.password == hash_code(password):
                message = "password correct"
            else:
                message = "password error"
        except:
            message = "user not exist"
    response = JsonResponse({"result": message}, safe=False)
    return response
