from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.db import models
from colorfield.fields import ColorField
from django.db.models import SET_NULL


# import slugify


# Create your models here. то есть для моделей (классов-таблиц)

class Book(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name='Book name',
        help_text='Enter book name',
        unique_for_date='publish_date',
        null=True,
        blank=True
    )

    image_color = ColorField(format="hexa")
    publish_date = models.DateTimeField(null=True)
    created_date = models.DateTimeField(auto_now_add=True, editable=False)
    updated_date = models.DateTimeField(auto_now=True, editable=False)
    slug = models.SlugField(null=True, editable=False)
    content = RichTextField(null=True, blank=True)
    category = models.ForeignKey('Category', on_delete=SET_NULL, null=True, blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='books')
    author = models.ManyToManyField('Author', related_name='books')


    def __str__(self):
        return self.title
    # def save(self, *a, **kw):
    #     self.slug = slugify


class Author(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='authors')
    name = models.CharField(max_length=200, verbose_name='Authors name')
    description = models.CharField(max_length=200, verbose_name='Authors description')

    def __str__(self):
        return self.name


class Category(models.Model):
    title = models.CharField(max_length=200, verbose_name='Category name')

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title


class Employer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    boss=models.ManyToManyField('self', blank=True,  null=True, default=None, related_name='slaves',)

    changed_count = models.IntegerField(default=0, editable=False)

    # def save(self, *a, **kw):                           #способ увелеения с перегрузкой
    #     self.changed_count=self.slaves.count()
    #     return super(Employer, self).save(*a, **kw)

    @property
    def boss_count(self):
        return self.boss.count()

    @property
    def boss_name(self):
        return [self.boss.all()[i].user.username for i in range(self.boss.count())]

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name_plural = 'Employers'
        verbose_name = 'Employer'
        ordering=['-user']
        default_related_name = 'employer_set'


