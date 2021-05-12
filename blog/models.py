from django.db import models
 
 
class Post(models.Model):    
    title = models.CharField(
        max_length=200,
        verbose_name="Заголовок"
        )

    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
        verbose_name="Автор"
        )

    body = models.TextField(
        null=True,
        blank=True,
        verbose_name="Описание"
        )
    
    published = models.DateTimeField(
        auto_now_add=True,
        db_index=True,
        verbose_name="Опубликовано")
    
    rubric = models.ForeignKey(
        "Rubric",
        null=True,
        on_delete=models.PROTECT,
        verbose_name="Рубрика")
 
    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Статьи"
        verbose_name = "Статья"
        ordering = ['-published']

class Rubric(models.Model):
    name = models.CharField(
        max_length=20,
        db_index=True,
        verbose_name="Название"
        )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Рубрики"
        verbose_name = "Рубрика"
        ordering = ['name']