
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.template.loader import render_to_string

from blog.models import Post


def post_list(request):
    posts = Post.objects.order_by('-id')
    context = {
        'posts': posts,
    }
    # render는 주어진 1,2번째 인수를 사용해서
    # 1번째 인수: HttpRequest인스턴스
    # 2번째 인수: 문자열 (TEMPLATE['DIRS']를 기준으로 탐색할 템플릿 파일의 경로)
    # 3번째 인수: 템플릿을 랜더링 할때 사용할 객체 모음

    return render(request, 'blog/post_list.html', context)
    # return render(
    #     request=request,
    #     templates_name='blog/post_list.html',
    #     context=context,
    # )


def post_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    context = {
        'post': post,
    }
    return render(request, 'blog/post_detail.html', context)


def post_create(request):
    if request.method == 'POST':
        post = Post.objects.create(
            author=request.user,
            title=request.POST['title'],
            text=request.POST['text'],
        )
        # HTTP Redirection을 보낼 URl
        # http://localhost:8000/
        # /로 시작하면 절대경로, 절대경로의 시작은 도메
        return redirect('post-list')
        # return HttpResponse('id: {}, title: {}, text: {}, author: {}'.format(
        #     post.id,
        #     post.title,
        #     post.text,
        #     post.author
        # ))
    else:
        return render(request, 'blog/post_create.html',)
    # cur_file_path = os.path.abspath(__file__)
    # blog_dir_path = os.path.dirname(cur_file_path)
    # app_dir_path = os.path.dirname(blog_dir_path)
    # templates_dir_path = os.path.join(app_dir_path, 'templates')
    # blog_template_file_path = os.path.join(templates_dir_path, 'blog', 'post_list.html')
    # print(blog_template_file_path)
    # html = open(blog_template_file_path, 'rt').read()

    # 경로에 해당하는 HTML파일을 문자열로 로드해줌
    # html = render_to_string('blog/post_list.html')
    # 가져온 문자열을 돌려주기
    # return render(request, 'blog/post_list.html')




    # posts = Post.objects.all()
    # print(posts)
    # Post instance에서 title속성에 접근가능
    # HttpResponse에
    #
    # 글 목록
    # - 격전 참여시...
    # - 부정행위...
    # - PBE...
    #
    # 위 텍스트를 넣어서 리턴
    # result = '글 목록<br>'
    # for post in Post.objects.all():
    #     result +='{}<br>'.format(post.title)
    # return HttpResponse(result)

