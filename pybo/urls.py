from django.urls import path

from . import views

app_name = 'pybo'
urlpatterns = [
    path('', views.index, name='index'),
    # ''안의 내용이 pybo/(뒤에 오는 내용) <<이 된다
    path('<int:question_id>/', views.detail, name='detail'),
    path('answer/create/<int:question_id>/', views.answer_create, name='answer_create'),
    path('question/create/', views.question_create, name='question_create'),
]