from django.db import models
from django.db.models.signals import pre_save
from django.shortcuts import reverse
from django.utils.text import slugify
from transliterate import translit
from random import randint


class Product(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')
    image = models.ImageField(upload_to='images/', blank=False, verbose_name='Картинка')
    slug = models.SlugField(max_length=100, blank=True, unique=True,
                            help_text='Это поле не нужно заполнять, заполняется автоматически')
    date_creation = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def get_title_for_items(self):
        return self.title_for_product.all()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

def pre_save_product_slug(sender, instance, *args, **kwargs):
    if not instance.slug:
        slug = slugify(translit(str(instance.name), 'ru', reversed=True))
        if Product.objects.filter(slug=slug).exclude(id=instance.id).exists():
            extra = str(randint(1, 10))
            slug = "-".join([slug, str(extra)])
        instance.slug = slug

pre_save.connect(pre_save_product_slug, sender=Product)


class TitleListForProduct(models.Model):
    name = models.CharField(max_length=50, verbose_name='Заголовок')
    list_title = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='title_for_product')

    def get_item(self):
        return self.list_items.all()

    class Meta:
        verbose_name = 'Заголовок'
        verbose_name_plural = 'Заголовоки'


class ListItem(models.Model):
    name = models.TextField(max_length=2000, verbose_name='Текст пункта')
    title = models.ForeignKey(TitleListForProduct, on_delete=models.CASCADE, related_name='list_items')

    class Meta:
        verbose_name = 'Параграф'
        verbose_name_plural = 'Параграфы'

