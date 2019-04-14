from django.shortcuts import redirect
from django.shortcuts import reverse
from django.utils.deprecation import MiddlewareMixin


class IsLogin(MiddlewareMixin):
    list = ['/admin', '/captcha', '/login', '/register', '/resources', '/question']

    def process_view(self, request, callback, callback_args, callback_kwargs):
        if not request.session.get('is_login', None):
            for s in self.list:
                if request.path.startswith(s):
                     return callback(request,*callback_args,**callback_kwargs)
            return redirect(reverse('in'))
        return callback(request, *callback_args, **callback_kwargs)