from django.db import models
from django.utils import timezone

class Article(models.Model):
    title = models.CharField(max_length=150, blank=False, unique=False)
    content = models.TextField(blank=False, default='')
    year = models.PositiveSmallIntegerField(null=True, blank=True)
    image = models.ImageField(upload_to='media', blank=True, null=True)
    # created_at = models.DateTimeField(default=timezone.now)
    # updated_at = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title_with_year()

    def title_with_year(self):
        return "{} ({})".format(self.title, self.year)

    class Meta:
        verbose_name = 'CRUD Blog Web'
        verbose_name_plural = 'CRUD Blog Web'