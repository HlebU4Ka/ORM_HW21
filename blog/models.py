from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from autoslug import AutoSlugField


class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from="title", unique=True)
    content = models.TextField()
    preview = models.ImageField(upload_to='blog_previews/')
    created_date = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=False)
    views = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

    def save_info(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(BlogPost, self).save_info(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('blog_post_detail', args=[str(self.slug)])

