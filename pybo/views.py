# from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Question, Answer
from .forms import QuestionForm

# def index(request):
#     return HttpResponse("안녕하세요, pybo에 오신 것을 환영합니다.")

def index(request):
    question_list = Question.objects.order_by('-create_date') # -가 앞에 붙으면 역순으로 정렬이다.
    context = {'question_list' : question_list}
    return render(request, 'pybo/question_list.html', context)
    # render 함수: python 데이터를 템플릿에 적용해 HTML로 반환하는 함수이다.
    # 질문 목록으로 생성한 question_list 데이터를 /../question_list.html 파일에 적용해 HTML을 생성한 후 리턴한다.
    # 이런 pybo/quesiton_list.html 파일같은 것들을 template이라고 부른다.
    # 템플릿 파일은 html 파일과 비슷하지만 파이썬 데이터를 읽어서 사용할 수 있는 HTML 파일이다.

def detail(request, question_id): # detail 함수를 추가한다. 매개변수가 request 이외에 question_id 가 추가되었다.
    question = get_object_or_404(Question, pk=question_id) # Question.objects.get(id=question_id)
    context = {'question': question}
    return render(request, 'pybo/question_detail.html', context)

def answer_create(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    # answer = Answer(question=question, content=request.POST.get('content'), create_date=timezone.now())
    question.answer_set.create(content=request.POST.get('content'), create_date=timezone.now())
    return redirect('pybo:detail', question_id=question.id)

def question_create(request):
    form = QuestionForm()
    return render(request, 'pybo/question_form.html', {'form': form})