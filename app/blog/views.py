from django.http import HttpResponse


def post_list(request):
    return HttpResponse('<html><body>Post List</body></html>')