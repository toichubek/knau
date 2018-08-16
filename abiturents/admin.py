from django.contrib import admin
from .models import Documents, Abiturents, Abit, Sylka_abit
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from ckeditor.widgets import CKEditorWidget
from django.forms import ModelForm, Textarea

class AbitForm(ModelForm):
    class Meta:
        model = Abiturents
        fields = ['text', 'text_kg']
        widgets = {
            'text': CKEditorUploadingWidget(),
        }


class MyAbit(admin.ModelAdmin):
    form = AbitForm

class DocumentsAdmin(admin.ModelAdmin):
    list_display = ["name"]
    list_display_links=["name"]
    list_filter = ["name"]
    class Meta:
        model = Documents
        verbose_name = "Документ"
        verbose_plural_name = "Документы"




class AbitItemForm(ModelForm):
    class Meta:
        model=Abit
        fields = ['title', 'title_kg', 'order', 'text', 'text_kg']
        widgets = {
                'text': CKEditorUploadingWidget(),
                }

class MyAbitItem(admin.ModelAdmin):
    form = AbitItemForm
    list_display=["title", "order"]
    list_filter=["title", "order"]
    search_fields = ["title", "text", "title_kg", "text_kg"]

    class Meta:
        model = Abit
        verbose_name = "Список ветеринарии"
        verbose_plural_name = "Список ветеринарии"


class SylkaAdmin(admin.ModelAdmin):
    list_display = ["title", "order"]
    list_display_links=["title"]
    list_filter = ["title", "order"]
    class Meta:
        model = Sylka_abit
        verbose_name = "Ccылка"
        verbose_plural_name = "Ссылки"

admin.site.register(Sylka_abit, SylkaAdmin)
admin.site.register(Abit, MyAbitItem)
admin.site.register(Abiturents, MyAbit)
admin.site.register(Documents, DocumentsAdmin)
