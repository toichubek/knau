from django.contrib import admin
from .models import Doc, Stud, Sylka_stud
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from ckeditor.widgets import CKEditorWidget
from django.forms import ModelForm, Textarea
# Register your models here.

class DocAdmin(admin.ModelAdmin):
    list_display = ["name"]
    list_display_links=["name"]
    list_filter = ["name"]
    class Meta:
        model = Doc
        verbose_name = "Документ"
        verbose_plural_name = "Документы"

class StudItemForm(ModelForm):
    class Meta:
        model=Stud
        fields = ['title', 'title_kg', 'order', 'text', 'text_kg']
        widgets = {
                'text': CKEditorUploadingWidget(),
                }

class MyStudItem(admin.ModelAdmin):
    form = StudItemForm
    list_display=["title", "order"]
    list_filter=["title", "order"]
    search_fields = ["title", "text", "title_kg", "text_kg"]

    class Meta:
        model = Stud
        verbose_name = "Список ветеринарии"
        verbose_plural_name = "Список ветеринарии"


class SylkaAdmin(admin.ModelAdmin):
    list_display = ["title", "order"]
    list_display_links=["title"]
    list_filter = ["title", "order"]
    class Meta:
        model = Sylka_stud
        verbose_name = "Ccылка"
        verbose_plural_name = "Ссылки"

admin.site.register(Sylka_stud, SylkaAdmin)
admin.site.register(Stud, MyStudItem)
admin.site.register(Doc, DocAdmin)
