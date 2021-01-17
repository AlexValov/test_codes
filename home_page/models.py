from django.contrib.auth.models import User
from django.db import models



class HomePage(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    head_title = models.CharField(max_length=200, verbose_name='Текст в теге title')
    meta_keywords = models.CharField(max_length=200, verbose_name='meta_keywords')
    meta_description = models.CharField(max_length=200, verbose_name='meta_description')
    data_longitude = models.CharField(max_length=200, verbose_name='На карте долгота(data-longitude)')
    data_latitude = models.CharField(max_length=200, verbose_name='На карте широта(data-latitude)')
    
    def __str__(self):
        return self.head_title

    def get_img_for_slider(self):
        return self.slide_for_slider.all()

    def get_paragraph_for_description(self):
        return self.paragraph_for_description.all()

    class Meta:
        verbose_name = 'Главная страница'
        verbose_name_plural = 'Главная страница'


class ImageForSlider(models.Model):
    image = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=100, verbose_name='Название изображения')
    home_page = models.ForeignKey(HomePage, on_delete=models.CASCADE, related_name='slide_for_slider')

    class Meta:
        verbose_name = 'Изображение для слайдера'
        verbose_name_plural = 'Изображения для слайдера'



class ParagraphForDescription(models.Model):
    text = models.TextField(max_length=2000, verbose_name='Текст')
    home_page = models.ForeignKey(HomePage, on_delete=models.CASCADE, related_name='paragraph_for_description')

    class Meta:
        verbose_name = 'Параграф для описания'
        verbose_name_plural = 'Параграфы для описания'

