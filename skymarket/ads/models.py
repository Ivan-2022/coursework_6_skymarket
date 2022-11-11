from django.conf import settings
from django.db import models


class Ad(models.Model):
    title = models.CharField(max_length=200, verbose_name="Наименование")
    price = models.PositiveIntegerField(verbose_name="Цена")
    description = models.CharField(max_length=500, null=True, blank=True, verbose_name="Описание")
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="ads",
                               verbose_name="Автор объявления")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Время создания объявления")
    image = models.ImageField(upload_to='ads/', null=True, blank=True, verbose_name="Фото")

    class Meta:
        ordering = ('-created_at',)
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'

    def __str__(self):
        return self.title


class Comment(models.Model):
    text = models.CharField(max_length=2000, verbose_name="Комментарий")
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="comments",
                               verbose_name="Автор комментария")
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE, related_name="comments", verbose_name="Объявление")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Время создания комментария")

    class Meta:
        ordering = ('-created_at',)
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return self.text
