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

from login import views

urlpatterns = [
                  path('', views.admin, name='admin'),
                  path('question/', include([
                      path(r'', views.admin_question),
                      path(r'all/', views.admin_question, name='admin_question'),
                      path(r'all/<int:tag>-page-<int:page>/', views.admin_question_all, name='question_all'),
                      path(r'update:<int:num>/', views.admin_question_update, name='question_update'),
                      path(r'groups/(<num>[0-9]{4})/', views.admin_question_groups, name='question_groups'),
                      path(r'upload/', views.admin_question_upload, name='question_upload'),
                      path(r'search/<str:arg>/', views.admin_question_search, name='question_search'),
                      path(r'download/', views.question_download, name='download_account'),
                      path(r'groups/new', views.admin_question_groups_new, name="question_groups_new"),
                  ])),
                  path('account/', include([
                      path(r'', views.admin_account),
                      path(r'all/', views.admin_account, name='admin_account'),
                      path(r'all/<int:tag>-page-<int:page>/', views.admin_account_all, name='account_all'),
                      path(r'update:<int:num>/', views.admin_account_update, name='account_update'),
                      path(r'groups/(<num>[0-9]{4})/', views.admin_account_groups, name='account_groups'),
                      path(r'upload/', views.admin_account_upload, name='account_upload'),
                      path(r'download/', views.account_download, name='download_account')
                  ])),
                  path('test/', views.admin_test, name='admin_test'),
                  path('forum/', views.admin_forum, name='admin_forum'),
                  path('syllabus/', views.admin_syllabus, name='admin_syllabus'),
                  path('homwork/', views.admin_homework, name='admin_homework'),
                  path('feedback/', views.admin_feedback, name='admin_feedback'),
                  path('login/', views.login, name='login'),
                  path('register/', views.register, name='register'),
                  path('logout/', views.logout, name='logout'),
                  path('captcha/', include('captcha.urls')),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
