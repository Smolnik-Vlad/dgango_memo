from django.contrib import admin    #задать вопрос по поводу для чего вообще админ нужен

from bboard.models import Book, Author, Category, Employer

# Register your models here.



admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Category)            #Для того чтобы таблицы отображались в окне админа
#admin.site.register(Employer)


@admin.register(Employer)
class EmployerAdmin(admin.ModelAdmin):
    list_display = ('user', 'boss_name', 'boss_count', 'changed_count')



# @admin.register(product)
# class productAdmin(admin.ModelAdmin):
#     list_display = [id, 'title', ]
