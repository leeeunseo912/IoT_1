from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.contrib import messages
from .forms import CommentForm
from .models import Comment
# Create your views here.
def index(request):
  
    return render(request, 'main/index.html')

# @login_required(login_url='common:login')
def comment_create(request):
    """
    후기등록
    """
    # if request.method == 'POST':
    #     form = CommentForm(request.POST)
    #     if form.is_valid():
    #         comment = form.save(commit=False)
    #         comment.author = request.user
    #         comment.create_date = timezone.now()
    #         comment.save()
    #         return redirect('main: index')
    # else:
    #     form = CommentForm()
    
    # context = {'form':form}
    # return render(request, 'main/camping_detail.html', context)
    return render(request,'main/comment.html')


# @login_required(login_url='common:login')
# def comment_modify(request, comment_id):
#     """
#     후기수정
#     """
#     question = get_object_or_404(Comment, pk=comment_id)
#     if request.user != question.author:
#         messages.error(request, '수정권한이 없습니다')
#         return redirect('pybo:detail', question_id=question.id)
#     if request.method == "POST":
# # 질문 수정을 위해 값 덮어쓰기
#         form = CommentForm(request.POST, instance=question)
#         if form.is_valid():
#             comment = form.save(commit=False)
#             comment.author = request.user
#             comment.modify_date = timezone.now() # 수정일시 저장
#             comment.save()
#             return redirect('main:comment', comment_id=comment.id)
#     else:
#         # 질문 수정 화면에 기존 제목, 내용 반영
#         form = CommentForm(instance=question)
#     context = {'form': form}
#     return render(request, 'main/camping_detail.html', context)

# @login_required(login_url='common:login')
# def comment_delete(request, comment_id):
#     """
#     후기삭제
#     """
#     comment = get_object_or_404(Comment, pk=comment_id)
#     if request.user != comment.author:
#         messages.error(request, '삭제권한이 없습니다')
#         return redirect('main:commnet', comment_id=comment.id)
#     comment.delete()
#     return redirect('main:comment')

def camping_detail(request):
  
    return render(request, 'main/camping_detail.html')

def campinfo(req):
    return render(req, 'main/campinfo.html')