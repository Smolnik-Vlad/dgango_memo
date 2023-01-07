from django.contrib import admin    #задать вопрос по поводу для чего вообще админ нужен

from bboard.models import product, FirstModule

# Register your models here.

admin.site.register(product)            #Для того чтобы таблицы отображались в окне админа
admin.site.register(FirstModule)


# @admin.register(product)
# class productAdmin(admin.ModelAdmin):
#     list_display = [id, 'title', ]
