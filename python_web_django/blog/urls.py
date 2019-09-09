from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    # path('index/', views.index),
    path('addConfig/', views.addConfig),
    path('user/', views.ret_user),
    path('selectConfig/', views.selectConfig),
    path('selectData/', views.selectData),
    path('autoSelect/', views.autoSelect),
    path('pubCrawl/', views.pubCrawl),
    path('crawl/', views.crawl),
    path('saveEdit/', views.saveEdit),
    path('delData/', views.delData),
    path('saveEditMoudle/', views.saveEditMoudle),
    path('delConfig/', views.delConfig),
    path('selectPie/', views.selectPie),
    # path('index/', views.index, name="index"),

]
