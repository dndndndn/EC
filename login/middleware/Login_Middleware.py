import sys
from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import HttpResponse,redirect
from ..views import login,register,index


class IsLogin(MiddlewareMixin):
    list=['/admin','/captcha','/login','/register']

    def process_view(self, request, callback, callback_args, callback_kwargs):
        if not request.session.get('is_login', None):
            for s in self.list:
                if request.path.startswith(s):
                     return callback(request,*callback_args,**callback_kwargs)
            return redirect('/login/')
        return callback(request, *callback_args, **callback_kwargs)