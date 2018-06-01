from django.db import models
from django.conf import settings
from django.utils import timezone

# 클래스가 데이터베이스처럼 동작하게 하고싶을때 사용


class Post(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateField(
        default=timezone.now)
    published_date = models.DateField(
        blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

# 객채를 문자열로 추가하고 싶을때 __str__사용
    def __str__(self):
        return self.title
