from django.db import models


# Create your models here. то есть для моделей (классов-таблиц)

class product (models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(null=True, blank=True)
    price = models.FloatField(null=True, blank=True)
    published = models.DateTimeField(auto_now_add=True, db_index=True)

class FirstModule(models.Model):
    field_1=models .CharField(max_length=50, help_text="name")
    field_2=models .IntegerField(default=10) #по дефолту
    field_3=models .FloatField(null=True) #может быть путсым
    field_4=models .ForeignKey('product', on_delete=models.CASCADE) #внешний ключ на таблицу (указывается первым аргументом), on_delete описывает поведение после удаления строки
    field_5 = models.DateTimeField(auto_now_add=True) #автоматическое заполнение ячейки таблицы датой создания строки (при создании)

    def __str__(self):                      #Можно сделать вывод инфы о строке
        return f"{self.id} -- {self.field_1} -- {self.field_5}"



class Book(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name='book name', # переименование поля в поле админа
        help_text='Book name', #текст, который описывает поле снизу поля в админке
        #default="Unknown book" #параметр по умолчанию
        #unique=True #уникальность
        #unique_for_date = 'published_date' #то есть работает как валидация, что нельзя вводить одно и то же поля в заданный период
        #null=True #разрешает не заполнять поле, конфликтует с default
        blank=True, #разрешает хранить пустые значения (не null)
        db_index=True, #сокращает поиск, ПРОЧИТАТЬ
        db_column='change_name' #просто переименовать поле

    )

    published_date = models.DateTimeField(
        null=True,
        editable=False #запрещаем изменять поле через админ панель

    )

    key=models.IntegerField(
        primary_key=True
    )

    #slug = models.slugField(null=True, editable=False)

   # def save(self, *a, )

