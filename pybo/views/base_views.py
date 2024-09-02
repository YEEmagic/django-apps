from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, get_object_or_404

from ..models import Question


def index(request):
    page = request.GET.get('page', '1')  # 페이지
    kw = request.GET.get('kw', '')  # 검색어
    question_list = Question.objects.order_by('-create_date')  # -가 앞에 붙으면 역순으로 정렬이다.
    if kw:
        question_list = question_list.filter(
            Q(subject__icontains=kw) |  # 제목 검색
            Q(content__icontains=kw) |  # 내용 검색
            Q(answer__content__icontains=kw) |  # 답변 내용 검색
            Q(author__username__icontains=kw) |  # 질문 글쓴이 검색
            Q(answer__author__username__icontains=kw)   # 답변 글쓴이 검색
        ).distinct()
    paginator = Paginator(question_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)
    context = {'question_list': page_obj, 'page':page, 'kw':kw}
    # (question_list >>> page_obj와 바뀜) context = {'question_list' : question_list}
    return render(request, 'pybo/question_list.html', context)
    # render 함수: python 데이터를 템플릿에 적용해 HTML로 반환하는 함수이다.
    # 질문 목록으로 생성한 question_list 데이터를 /../question_list.html 파일에 적용해 HTML을 생성한 후 리턴한다.
    # 이런 pybo/question_list.html 파일같은 것들을 template이라고 부른다.
    # 템플릿 파일은 html 파일과 비슷하지만 파이썬 데이터를 읽어서 사용할 수 있는 HTML 파일이다.


def detail(request, question_id):  # detail 함수를 추가한다. 매개변수가 request 이외에 question_id 가 추가되었다.
    question = get_object_or_404(Question, pk=question_id)  # Question.objects.get(id=question_id)
    context = {'question': question}
    return render(request, 'pybo/question_detail.html', context)
