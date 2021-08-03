from django.db import models

# my api models 

class Category(models.Model):
    title = models.CharField(max_length=200)
    
    class Meta:
        verbose_name_plural: "Categories"
    def __str__(self):
        return self.title


class Product(models.Model):
    product_tag = models.IntegerField()
    title = models.CharField(max_length=200)
    price = models.IntegerField()
    imageUrl = models.URLField()
    category = models.ForeignKey(Category, related_name='product', default=None, on_delete=models.CASCADE)
    in_stock = models.IntegerField()
    status = models.BooleanField(default=True)
    description = models.TextField()
    date_created = models.DateField(auto_now_add=True)

    class Meta:
        ordering: ('-date_created')

    def __str__(self):
        return(f'{self.product_tag}  {self.title}')
