from django.contrib import admin
from .models import Kafedra, Sotrudnik, Sotrudnik_dekanat, History, Manager, Gallery, GalleryImage
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from ckeditor.widgets import CKEditorWidget
from django.forms import ModelForm, Textarea

class HistoryForm(ModelForm):
    class Meta:
        model=History
        fields = ['text_ru', 'text_kg']
        widgets = {
                'text': CKEditorUploadingWidget(),
                }

class MyHistory(admin.ModelAdmin):
    form = HistoryForm

class SotrudnikAdmin(admin.ModelAdmin):
    list_display=["name", "kafedra"]
    list_display_links=["name"]
    list_filter=["kafedra"]
    search_fields = ('name',)

    class Meta:
        model = Sotrudnik
        verbose_name = "Сотрудник кафедры"
        verbose_plural_name = "Сотрудники кафедры"

class Sotrudnik_dekanat_Admin(admin.ModelAdmin):
    list_display=["name", "place"]
    list_display_links=["name"]
    list_filter=["name"]
    search_fields = ('name',)

    class Meta:
        model = Sotrudnik
        verbose_name = "Сотрудник факультета"
        verbose_plural_name = "Сотрудники факультета"

class ManagerAdmin(admin.ModelAdmin):
    list_display = ["name", "place"]
    list_display_links = ["name"]
    list_filter = ["name"]
    search_fields = ('name', 'place',)

    class Meta:
        model = Manager
        verbose_name = "Руководство"
        verbose_plural_name = "Руководство"

class ImageAdmin(admin.ModelAdmin):
    list_display=["alt","album"]
    list_display_links=["alt", "album"]
    list_filter=["album"]
    search_fields = ('album', 'alt',)

    class Meta:
        model = GalleryImage
        verbose_name = "Фотография"
        verbose_plural_name = "Фотографии"

admin.site.register(Kafedra)
admin.site.register(Gallery)
admin.site.register(GalleryImage, ImageAdmin)
admin.site.register(Manager, ManagerAdmin)
admin.site.register(Sotrudnik_dekanat, Sotrudnik_dekanat_Admin)
admin.site.register(Sotrudnik, SotrudnikAdmin)
admin.site.register(History, MyHistory)

