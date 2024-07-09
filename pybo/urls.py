from django.urls import path

from . import views

urlpatterns = [
    path('', views.index), # ''안의 내용이 pybo/(뒤에오는내용) <<이 된다
]