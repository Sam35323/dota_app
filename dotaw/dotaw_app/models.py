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
        return reverse('categories', kwargs={'cat_slug': self.slug})


class Hero(models.Model):
    name = models.CharField(max_length=35, verbose_name="наме")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    disc = models.TextField(verbose_name="диск")
    top_class = models.ForeignKey(TopClass, on_delete=models.CASCADE, verbose_name="топ сласс")
    top_position = models.ForeignKey(Position, on_delete=models.CASCADE, verbose_name="Топ позицион")
    bio = models.TextField(verbose_name='Биография')
    ultimate = models.CharField(max_length=35, verbose_name="Ультимате")
    ultimate_disc = models.TextField(verbose_name="Ультимате_диск")
    photo = models.ImageField(upload_to="photos/%m/%d", default='i.png', verbose_name="пхото")

    skill_1 = models.CharField(max_length=35, verbose_name="скилл1")
    skill_1_disc = models.TextField(verbose_name="URL")
    skill_2 = models.CharField(max_length=35, verbose_name="скилл2")
    skill_2_disc = models.TextField(verbose_name="URL")
    skill_3 = models.CharField(max_length=35, verbose_name="скилл3")
    skill_3_disc = models.TextField(verbose_name="URL")

    class Meta:
        verbose_name = 'Перс'
        verbose_name_plural = 'Персы'

    def get_absolute_url(self):
        return reverse('ohe_hero', kwargs={'hero_slug': self.slug})

    def save(self, *args, **kwargs):
        from django.utils.text import slugify
        self.slug = slugify(self.name)
        super(Hero, self).save(*args, **kwargs)