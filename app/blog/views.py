import os

from django.http import HttpResponse
from django.template.loader import render_to_string


def post_list(request):
    # cur_file_path = os.path.abspath(__file__)
    # blog_dir_path = os.path.dirname(cur_file_path)
    # app_dir_path = os.path.dirname(blog_dir_path)
    # templates_dir_path = os.path.join(app_dir_path, 'templates')
    # blog_template_file_path = os.path.join(templates_dir_path, 'blog', 'post_list.html')
    # print(blog_template_file_path)
    # html = open(blog_template_file_path, 'rt').read()

    # 경로에 해당하는 HTML파일을 문자열로 로드해줌
    html = render_to_string('blog/post_list.html')
    # 가져온 문자열을 돌려주기
    return HttpResponse(html)
