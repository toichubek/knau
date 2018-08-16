from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.

#
# class Doc(models.Model):
#     name = models.CharField(max_length=150, verbose_name="название")
#     file = models.FileField(upload_to='uploads/docs/', verbose_name="Документ")
#
#
#     def __str__(self):
#         return f"{self.name}"
#     class Meta:
#         verbose_name = "Документ"
#         verbose_name_plural = "Документы"
#

# class Order(models.Model):
#     order = models.PositiveSmallIntegerField(null=True, blank=True, verbose_name="Порядок в списке")
#

class Vet(models.Model):
    title = models.TextField(null=True, blank=True, max_length=50, verbose_name="Название")
    title_kg = models.TextField(null=True, blank=True, max_length=50, verbose_name="Аталышы")
    text = RichTextUploadingField(null=True, blank=True, verbose_name="Текст на русском")
    text_kg = RichTextUploadingField(null=True, blank=True, verbose_name="Кыргызча текст")
    order = models.PositiveSmallIntegerField(null=True, blank=True, verbose_name="Порядок в списке")

    def __str__(self):
        return f" Страница {self.title} по списку {self.order}"
    class Meta:
        verbose_name = "Страница Ветеринарии"
        verbose_name_plural = "Список страниц Ветеринарии"


class Sylka_vet(models.Model):
    url = models.URLField(blank=True, null=True, help_text="обязательно", verbose_name="Адрес")
    title = models.CharField(max_length=150, verbose_name="Название RU", null=True, blank=True)
    title_kg = models.CharField(max_length=150, verbose_name="Аталышы KG", null=True, blank=True)
    order = models.PositiveSmallIntegerField(null=True, blank=True, verbose_name="Порядок в списке")
    new_tab = models.NullBooleanField(null=True, blank=True, verbose_name="Открыть в новом окне")

    def __str__(self):
        return f" {self.title}"

    class Meta:
        verbose_name = "Ссылка"
        verbose_name_plural = "Ссылки"


class GalleryVideo(models.Model):
    name = models.CharField(verbose_name="Название", max_length=250, null=True, blank=True)
    name_kg = models.CharField(verbose_name="Название KG", max_length=250, null=True, blank=True)

    is_visible = models.BooleanField(default=True, verbose_name="Показать")
    # slug = models.SlugField(max_length=50, unique=True, default='slug', verbose_name="имя ссылки")

    def __str__(self):
        return f" Каталог видео:{self.name}"

    class Meta:
        verbose_name = "Каталог видео"
        verbose_name_plural = "Каталоги видео"

class Videos(models.Model):
    video = models.FileField(verbose_name="Видео файл", upload_to='media/video')
    album = models.ForeignKey('GalleryVideo', on_delete=models.PROTECT, verbose_name="Каталог")
    name = models.TextField(max_length=55, verbose_name="название RU")
    name_kg = models.TextField(max_length=55, verbose_name="название KG")
    # slug = models.SlugField(max_length=70, default='slug', verbose_name="имя ссылки")

    def __str__(self):
        return f" Видео:{self.album}"

    def display_name(self):
        return "%s" % (self.album)

    class Meta:
        verbose_name = "Видео"
        verbose_name_plural = "Видео"
