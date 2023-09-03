from django.utils import timezone
from django.utils.text import slugify
from django.db import models
from django.urls import reverse
from autoslug import AutoSlugField
# Create your models here.
NULLABLE = {'null': True, 'blank': True}


class Product(models.Model):
    name = models.CharField(max_length=150, name='name')
    description = models.TextField(verbose_name='описание')
    preview = models.ImageField(upload_to='products/', verbose_name='Изображение', **NULLABLE)
    category = models.CharField(max_length=50, verbose_name='категория')
    price = models.CharField(verbose_name='цена', **NULLABLE)
    create_date = models.DateField(verbose_name='дата создания')
    date_update = models.DateField(verbose_name='дата последнего изменения')

    def __str__(self):
        return f'{self.name} - {self.category} - {self.price} - {self.create_date} - {self.date_update}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'


class Category(models.Model):
    name = models.CharField(max_length=150, name='name')
    description = models.TextField(max_length=300, verbose_name='описание')
    create_date = models.DateField(default=timezone.now, verbose_name='дата создания')

    def __str__(self):
        return f'{self.name} - {self.description}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, max_length=200)
    content = models.TextField()
    preview = models.ImageField(upload_to='blog_previews/')
    created_date = models.DateTimeField(auto_now_add=True)
    published = models.BooleanField(default=False)
    views = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(BlogPost, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('blog_post_detail', args=[str(self.slug)])
