from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

class Abiturents(models.Model):
    text = RichTextUploadingField(null=True, blank=True)
    text_kg = RichTextUploadingField(null=True, blank=True)

    def __str__(self):
        return "АБИТУРЕНТАМ"

    class Meta:
        verbose_name = "АБИТУРЕНТУ "
        verbose_name_plural = "АБИТУРЕНТАМ "

class Abit(models.Model):
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


class Sylka_abit(models.Model):
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

class Documents(models.Model):
    name = models.CharField(max_length=250, verbose_name="Название", blank=True)
    document = models.FileField(upload_to='uploads/abiturent_docs')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Документ для абитурента"
        verbose_name_plural = "Документы для абитурента"