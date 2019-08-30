from django.urls import path
from . import views

urlpatterns = [
    # path('index/', views.index),
    path('addConfig/', views.addConfig),
    path('user/', views.ret_user),
    path('selectConfig/', views.selectConfig),
    path('selectData/', views.selectData),
    path('autoSelect/', views.autoSelect),
    path('pubCrawl/', views.pubCrawl)
]
