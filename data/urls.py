from django.urls import path, re_path
from . import views

urlpatterns = [
path('', views.index, name="kembalidata"),
re_path(r'^delete/(?P<inputdelete>[0-9]+)/$', views.delete, name="namedelete"),
re_path(r'^id/(?P<inputdata>[\w-]+)/$', views.singleData, name="sluginput"),
path('edit', views.edit, name="nameedit"),
path('create', views.create, name="namecreate"),
]
