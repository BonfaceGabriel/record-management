from django.contrib import admin
from .models import DigitalRoad


class DigitalRoadAdmin(admin.ModelAdmin):
    def get_list_display(self, request):
        list_display = []
        for field in self.model._meta.get_fields():
            if field.choices:
                list_display.append(field.name)
            else:
                list_display.append(field.name)
        return list_display
    list_filter = ('county',)
    search_fields = ('name_of_site',)

admin.site.register(DigitalRoad, DigitalRoadAdmin)


