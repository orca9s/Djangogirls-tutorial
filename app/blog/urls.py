from django.conf.urls import url

from .views import post_list, post_detail, post_create, post_delete, post_edit

urlpatterns = [
    # url의 첫 번째 인자: 매치될 URL정규표현식
    # url의 두 번째 인자: view function
    #   view function
    #       -> request를 받아서 response를 돌려주는 함수

    # blog.views에 있는 post_list함수를
    # 아래 url함수의 두 번째 인자로 전달
    #   (함수호출 아님)
    url(r'^$', post_list, name='post-list'),
    url(r'^post/(\d+)/$', post_detail, name='post-detail'),
    url(r'^post/(\d+)/delete/$', post_delete, name='post-delete'),
    url(r'^write/', post_create, name='post-create'),
    url(r'^post/(\d+)/edit/$', post_edit, name='post-edit'),

]
