from django.db import models
from django.urls import reverse


class TopClass(models.Model):
    class_name = models.CharField(max_length=35)
    disc = models.CharField(max_length=300)

    class Meta:
        verbose_name = 'Топ параметр'
        verbose_name_plural = 'Топ параметры'


class Position(models.Model):
    position_name = models.CharField(max_length=35)
    disc = models.CharField(max_length=300)

    slug = models.SlugField(max_length=228, unique=True, db_index=True)

    class Meta:
        verbose_name = 'Позиция'
        verbose_name_plural = 'Позиции'

    def get_absolute_url(self):
        return reverse('categories', kwargs={'category_id': self.id})


class Hero(models.Model):
    name = models.CharField(max_length=35)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    disc = models.TextField()
    top_class = models.ForeignKey(TopClass, on_delete=models.CASCADE)
    top_position = models.ForeignKey(Position, on_delete=models.CASCADE)
    bio = models.TextField()
    ultimate = models.CharField(max_length=35)
    ultimate_disc = models.TextField()
    photo = models.ImageField(upload_to="photos/%m/%d")

    skill_1 = models.CharField(max_length=35)
    skill_1_disc = models.TextField()
    skill_2 = models.CharField(max_length=35)
    skill_2_disc = models.TextField()
    skill_3 = models.CharField(max_length=35)
    skill_3_disc = models.TextField()

    class Meta:
        verbose_name = 'Перс'
        verbose_name_plural = 'Персы'

    def get_absolute_url(self):
        return reverse('ohe_hero', kwargs={'hero_slug': self.slug})
