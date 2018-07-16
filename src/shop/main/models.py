from django.db import models



# Models category.
class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='children', on_delete=models.CASCADE)

    class Meta:
        ordering = ['name']
        unique_together = ('slug', 'parent',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        full_path = [self.name]
        k = self.parent

        while k is not None:
            full_path.append(k.name)
            k = k.parent

        return ' -> '.join(full_path[::-1])



# Models product.
class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', verbose_name='Категория', on_delete=models.CASCADE,)
    name = models.CharField(max_length=200, db_index=True, verbose_name="Название")
    slug = models.SlugField(max_length=200, db_index=True)
    description = models.TextField(blank=True, verbose_name="Описание")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    stock = models.PositiveIntegerField(verbose_name="На складе")
    available = models.BooleanField(default=True, verbose_name="Доступен")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        index_together = [
            ['id', 'slug']
        ]


    def __str__(self):
        return self.name

    def get_cat_list(self):
        k = self.category
        breadcrumb = []
        while k is not None:
            breadcrumb.append(k.slug)
            k = k.parent
        return breadcrumb[-1:0:-1]