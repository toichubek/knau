from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.


class Doc(models.Model):
    name = models.CharField(max_length=150, verbose_name="название")
    file = models.FileField(upload_to='uploads/student_docs/', verbose_name="Документ")


    def __str__(self):
        return f"{self.name}"
    class Meta:
        verbose_name = "Документ"
        verbose_name_plural = "Документы"


class Stud(models.Model):
    title = models.TextField(null=True, blank=True, max_length=50, verbose_name="Название")
    title_kg = models.TextField(null=True, blank=True, max_length=50, verbose_name="Аталышы")
    text = RichTextUploadingField(null=True, blank=True, verbose_name="Текст на русском")
    text_kg = RichTextUploadingField(null=True, blank=True, verbose_name="Кыргызча текст")
    order = models.PositiveSmallIntegerField(null=True, blank=True, verbose_name="Порядок в списке")

    def __str__(self):
        return f" Страница {self.title} по списку {self.order}"
    class Meta:
        verbose_name = "Страница Абитуриента"
        verbose_name_plural = "Список страниц Абитуриента"


class Sylka_stud(models.Model):
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
