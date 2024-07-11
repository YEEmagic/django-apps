from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    # ''안의 내용이 pybo/(뒤에 오는 내용) <<이 된다
    path('<int:question_id>/', views.detail),
]