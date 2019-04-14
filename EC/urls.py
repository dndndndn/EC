"""EC URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib.staticfiles.urls import static
from django.urls import path, include

from android import views as android_views
from login import views as login_views

urlpatterns = [
                  path('admin/', include('login.urls')),
                  #   path('out/',include('circuit.urls')),
                  path('', login_views.ins, name='in'),
                  path('index/', login_views.index, name='index'),
                  path('login/', android_views.login, name='android_login'),
                  path('resources/<path:path>/', android_views.resources_get, name='resource_get'),
                  path('question/<int:ID>', android_views.question_download, name='question_download')

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler400 = login_views.bad_request
handler403 = login_views.permission_denied
handler404 = login_views.page_not_found
handler500 = login_views.page_error
