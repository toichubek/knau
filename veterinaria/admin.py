from django.contrib import admin
from .models import Vet, Sylka_vet, GalleryVideo, Videos
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from ckeditor.widgets import CKEditorWidget
from django.forms import ModelForm, Textarea
# Register your models here.

# class DocAdmin(admin.ModelAdmin):
#     list_display = ["name"]
#     list_display_links=["name"]
#     list_filter = ["name"]
#     class Meta:
#         model = Doc
#         verbose_name = "Документ"
#         verbose_plural_name = "Документы"


class VetForm(ModelForm):
    class Meta:
        model=Vet
        fields = ['title', 'title_kg', 'order', 'text', 'text_kg']
        widgets = {
                'text': CKEditorUploadingWidget(),
                }

class MyVet(admin.ModelAdmin):
    form = VetForm
    list_display=["title" , "order"]
    list_filter=["title", "order"]
    search_fields = ["title", "text", "title_kg", "text_kg"]

    class Meta:
        model = Vet
        verbose_name = "Список ветеринарии"
        verbose_plural_name = "Список ветеринарии"

class SylkaAdmin(admin.ModelAdmin):
    list_display = ["title", "order"]
    list_display_links=["title"]
    list_filter = ["title", "order"]
    class Meta:
        model = Sylka_vet
        verbose_name = "Ccылка"
        verbose_plural_name = "Ссылки"


class VideoAdmin(admin.ModelAdmin):
    list_display=["name","album"]
    list_display_links=["name", "album"]
    list_filter=["album"]
    search_fields = ('album', 'name', 'alt')

    class Meta:
        model = GalleryVideo
        verbose_name = "Видео"
        verbose_plural_name = "Видео"

admin.site.register(GalleryVideo)
admin.site.register(Videos, VideoAdmin)


admin.site.register(Sylka_vet, SylkaAdmin)
admin.site.register(Vet, MyVet)
