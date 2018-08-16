from django.contrib import admin
from .models import New, Faq, Address, Sylka
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from ckeditor.widgets import CKEditorWidget
from django.forms import ModelForm, Textarea


class NewsAdmin(admin.ModelAdmin):
    list_display=["title","published"]
    list_display_links=["title"]
    list_filter=["published"]
    class Meta:
        model=New

class AddressAdmin(admin.ModelAdmin):
    list_display=["gorod", "ulitsa"]
    list_display_links=["gorod", "ulitsa"]
    list_filter=["ulitsa"]
    class Meta:
        model = Address
        verbose_name = "Адрес"
        verbose_plural_name = "Адресы"

class SylkaAdmin(admin.ModelAdmin):
    list_display = ["title", "order"]
    list_display_links=["title"]
    list_filter = ["title", "order"]
    class Meta:
        model = Sylka
        verbose_name = "Ccылка"
        verbose_plural_name = "Ссылки"

admin.site.register(Sylka, SylkaAdmin)
admin.site.register(Address, AddressAdmin)
admin.site.register(New, NewsAdmin)
admin.site.register(Faq)
