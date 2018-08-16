from django.db import models
from django.utils import timezone
import datetime
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField


class New(models.Model):
    title = models.CharField(max_length=150, verbose_name="Название", null=True, blank=True)
    title_kg = models.CharField(max_length=150, verbose_name="Аталышы KG", null=True, blank=True)
    text = RichTextUploadingField(verbose_name="Текст", null=True, blank=True)
    text_kg = RichTextUploadingField(verbose_name="Текст KG", null=True, blank=True)
    image = models.ImageField(upload_to='media/news', blank=True, null=True, verbose_name="Фото")
    preview=models.TextField(max_length=200, verbose_name="Описание", null=True, blank=True)
    preview_kg=models.TextField(max_length=200, verbose_name="Кыскача KG", null=True, blank=True)
    published=models.DateTimeField(blank=True, null=True, verbose_name="Опубликовано")

    def publish_now(self):
        now=self.published.date()
        return now.strftime('%d.%m.%Y')

    def __str__(self):
        return f" id-{self.id}_{self.title}"
    class Meta:
        verbose_name = "Новости"
        verbose_name_plural = "Новости"

class  Faq(models.Model):
    question = models.TextField(max_length=500,  verbose_name="Вопрос", null=True, blank=True)
    answer = RichTextUploadingField(verbose_name="Ответ", null=True, blank=True)
    question_kg = models.TextField(max_length=500, verbose_name="Суроо KG", null=True, blank=True)
    answer_kg = RichTextUploadingField(verbose_name="Жооп KG", null=True, blank=True)

    def __str__(self):
        return f" {self.question}"
    class Meta:
        verbose_name = "Вопросы"
        verbose_name_plural = "Вопрос-Ответ"

class Sylka(models.Model):
    url = models.URLField(blank=True, null=True, help_text="обязательно", verbose_name="Адрес (Ссылка в меню: 'Вопрос-Ответ' и 'Контакты')")
    title = models.CharField(max_length=150, verbose_name="Название RU", null=True, blank=True)
    title_kg = models.CharField(max_length=150, verbose_name="Аталышы KG", null=True, blank=True)
    order = models.PositiveSmallIntegerField(null=True, blank=True, verbose_name="Порядок в списке")
    new_tab = models.NullBooleanField(null=True, blank=True, verbose_name="Открыть в новом окне")

    def __str__(self):
        return f" {self.title}"

    class Meta:
        verbose_name = "(Ссылка в меню: 'Вопрос-Ответ' и 'Контакты')"
        verbose_name_plural = "Ссылки в меню: 'Вопрос-Ответ' и 'Контакты' "

class Address(models.Model):
    strana = models.CharField(max_length=30, verbose_name="Страна", null=True, blank=True)
    gorod = models.CharField(max_length=150, verbose_name="Город", null=True, blank=True)
    ulitsa = models.TextField(max_length=150, verbose_name="Улица", null=True, blank=True)
    strana_kg = models.CharField(max_length=30, verbose_name="Олко", null=True, blank=True)
    gorod_kg = models.CharField(max_length=150, verbose_name="Шаары", null=True, blank=True)
    ulitsa_kg= models.TextField(max_length=150, verbose_name="Кочосу", null=True, blank=True)

    telephone = models.CharField(max_length=70, blank=True)
    email = models.EmailField(max_length=70,blank=True, null= True, unique= True)
    api = models.TextField( verbose_name="Ссылка для карты (API script)",blank=True, null= True)

    class Meta:
        verbose_name = "Адрес"
        verbose_name_plural = "Адрес"

    def __str__(self):
        return f" Адрес:{self.ulitsa}"



#class Foto(models.Model):
#    image = StdImageField(upload_to=UploadToClassNameDirUUID())
#    place = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='photos')
#
#    def __str__(self):
#        return SafeText('<img src="{0}" />'.format(self.image.thumbnail.url))
#
#    class Meta:
#        ordering = ('id',)
#        verbose_name = 'Fotka'
#        verbose_name_plural = 'Fotky'



# class  Team(models.Model):
#     KAFEDRA1 = 'Кафедра акушерства и хирургии'
#     KAFEDRA2= 'Кафедра анатомии и физиологии'
#     KAFEDRA3 = 'Кафедра инфекционных и инвазионных болезней животных'
#     KAFEDRA4 = 'Кафедра ВСЭ, гистологии и патологии'
#     KAFEDRA5 = 'Кафедра внутренние болезни животных'
#     KAFEDRA6 = 'Кафедра биотехнологии и биологии'
#     SOTRUDNIK = 'Сотрудник'
#     STATUS = ((KAFEDRA1, 'Кафедра акушерства и хирургии'), (KAFEDRA2, 'Кафедра анатомии и физиологии'),
#               (KAFEDRA3, 'Кафедра инфекционных и инвазионных болезней животных'), (KAFEDRA4, 'Кафедра ВСЭ, гистологии и патологии'),
#               (KAFEDRA5, 'Кафедра внутренние болезни животных'), (KAFEDRA6, 'Кафедра биотехнологии и биологии'),
#               (SOTRUDNIK, 'Сотрудник'), )
#     status = models.CharField(
#         max_length=150,
#         choices=STATUS,
#         default="Сотрудник", verbose_name="Кафедра")
#
#     name = models.CharField(max_length=150,  verbose_name="Ф.И.О")
#     place = models.TextField(default=' ')
#     image = models.ImageField(upload_to='static/', blank=True, null=True)
#
#     class Meta:
#         verbose_name = "Сотрудник"
#         verbose_name_plural = "Сотрудник"
#
#     def __str__(self):
#         return f" {self.name}"
