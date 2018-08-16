from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill, ResizeToFit


class Sotrudnik(models.Model):
    name = models.CharField(max_length=150, verbose_name="Ф.И.О")
    place = models.TextField(default=' ', verbose_name="Должность")
    place_kg = models.TextField(default=' ', verbose_name="Должность KG")

    #image = models.ImageField(upload_to='static/', blank=True, null=True, verbose_name="ФОТО")
    image = ProcessedImageField(upload_to='static/',
                                    processors=[ResizeToFill(150, 210)],
                                    format='JPEG',
                                    options={'quality': 60},
                                blank=True, null=True, verbose_name="ФОТО", default="./media/static/kaf_ii_b_j.jpg", help_text="обязательно")
    kafedra = models.ForeignKey(
        'Kafedra',
        on_delete=models.CASCADE, verbose_name="Кафедра", default="NULL",
    )

    class Meta:
        verbose_name = "Сотрудник кафедры"
        verbose_name_plural = "Сотрудники кафедры"

    def __str__(self):
        return f" {self.name}"

class Sotrudnik_dekanat(models.Model):
    name = models.CharField(max_length=150, verbose_name="Ф.И.О")
    place = models.TextField(default=' ', verbose_name="Должность")
    place_kg = models.TextField(default=' ', verbose_name="Должность KG")
    #image = models.ImageField(upload_to='static/', blank=True, null=True, verbose_name="ФОТО")
    image = ProcessedImageField(upload_to='static/',
                                processors=[ResizeToFill(150, 210)],
                                format='JPEG',
                                options={'quality': 60},
                                blank=True, null=True, verbose_name="ФОТО")
    class Meta:
        verbose_name = "Сотрудник факультета"
        verbose_name_plural = "Сотрудники факультета"

    def __str__(self):
        return f" {self.name}"

class Kafedra(models.Model):
    name = models.CharField(max_length=150, verbose_name="Название", null=True, blank=True)
    name_kg = models.CharField(max_length=150, verbose_name="Название KG", null=True, blank=True)
    about = RichTextUploadingField(null=True, blank=True, verbose_name="О кафедре")
    about_kg = RichTextUploadingField(null=True, blank=True, verbose_name="Кафедра жонундо")

    #image = models.ImageField(upload_to='media/', blank=True, null=True)
    image = ProcessedImageField(upload_to='media/',
                                processors=[ResizeToFill(width=460, height=300)],
                                format='JPEG',
                                options={'quality': 60},
                                blank=True, null=True, verbose_name="ФОТО")
    # prepod = models.ForeignKey(Sotrudnik, null=True, on_delete=models.CASCADE,)

    class Meta:
        verbose_name = "Кафедра"
        verbose_name_plural = "Кафедры"

    def __str__(self):
        return f" {self.name}"

class History(models.Model):
    text_ru = RichTextUploadingField(null=True, blank=True, verbose_name="ru")
    text_kg = RichTextUploadingField(null=True, blank=True, verbose_name="kg")

    def __str__(self):
        return f" История:{self.id}"

    class Meta:
        verbose_name = "История"
        verbose_name_plural = "История"

class Manager(models.Model):
    name = models.CharField(max_length=150, verbose_name="Ф.И.О")
    place = models.TextField(default=' ', verbose_name="Должность")
    place_kg = models.TextField(default=' ', verbose_name="Должность KG")

   # image = models.ImageField(upload_to='static/', blank=True, null=True, verbose_name="ФОТО")
    image = ProcessedImageField(upload_to='static/',
                                processors=[ResizeToFill(width=150, height=210)],
                                format='JPEG',
                                options={'quality': 60},
                                blank=True, null=True, verbose_name="ФОТО")
    class Meta:
        verbose_name = "Руководство"
        verbose_name_plural = "Руководство"

    def __str__(self):
        return f" {self.name}"

class Gallery(models.Model):
    name = models.CharField(verbose_name="Название", max_length=250, null=True, blank=True)
    name_kg = models.CharField(verbose_name="Название KG", max_length=250, null=True, blank=True)

    is_visible = models.BooleanField(default=True, verbose_name="Показать")
    # slug = models.SlugField(max_length=50, unique=True, default='slug', verbose_name="имя ссылки")

    def __str__(self):
        return f" Каталог фото:{self.name}"

    class Meta:
        verbose_name = "Каталог фото"
        verbose_name_plural = "каталоги фото"

class GalleryImage(models.Model):
    image = ProcessedImageField(upload_to='media/images', processors=[ResizeToFit(1280)], format='JPEG', options={'quality': 70}, verbose_name="Фото")
    album = models.ForeignKey('Gallery', on_delete=models.PROTECT, verbose_name="Каталог")
    alt = models.CharField(max_length=255, verbose_name="описание")
    # slug = models.SlugField(max_length=70, default='slug', verbose_name="имя ссылки")

    def __str__(self):
        return f" Фото:{self.album}"

    def display_name(self):
        return "%s" % (self.album)

    class Meta:
        verbose_name = "Фотография"
        verbose_name_plural = "Фотографии"
