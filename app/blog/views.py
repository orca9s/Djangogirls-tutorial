import os

from django.http import HttpResponse


def post_list(request):
    cur_file_path = os.path.abspath(__file__)
    blog_dir_path = os.path.dirname(cur_file_path)
    app_dir_path = os.path.dirname(blog_dir_path)
    templates_dir_path = os.path.join(app_dir_path, 'templates')
    blog_template_file_path = os.path.join(templates_dir_path, 'blog', 'post_list.html')
    print(blog_template_file_path)
    html = open(blog_template_file_path, 'rt').read()
    return HttpResponse(html)
