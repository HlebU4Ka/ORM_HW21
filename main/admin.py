from django.contrib import admin

from main.models import Product, Category


# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'price')
    list_filter = ('category',)
    search_fields = ('name', 'description')

    def category_search(self, obj):
        return obj.category.name if obj.category else '-'

    category_search.short_description = 'Категория'


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category')
