from django.db import models
from django.urls import reverse


class OrderNew(models.Model):
    order_main_img = models.ImageField(upload_to='car_img_order/%Y/%m/%d/', verbose_name='Главная картинка')
    order_main_img_mini = models.ImageField(upload_to='car_img_order/%Y/%m/%d/', verbose_name='Картинка брэнда',
                                            null=True, blank=True)
    order_slug = models.SlugField(max_length=250, unique=True, db_index=True)
    order_main_title = models.CharField(max_length=250, verbose_name='Название товара')
    order_dop_title1 = models.CharField(max_length=400, verbose_name='Доп-характеристика1', blank=True)
    order_dop_title2 = models.CharField(max_length=400, verbose_name='Доп-характеристика2', blank=True)
    order_dop_title3 = models.CharField(max_length=400, verbose_name='Доп-характеристика3', blank=True)
    order_dop_title4 = models.CharField(max_length=400, verbose_name='Доп-характеристика4', blank=True)
    order_dop_title5 = models.CharField(max_length=400, verbose_name='Доп-характеристика5', blank=True)
    order_dop_title6 = models.CharField(max_length=400, verbose_name='Доп-характеристика6', blank=True)
    order_category = models.ForeignKey('NewCategoryOrder', on_delete=models.PROTECT)
    order_price = models.CharField(max_length=50, verbose_name='Цена товара')
    order_text = models.TextField(verbose_name='Описание')
    order_maim_date_add = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    order_maim_date = models.DateTimeField(auto_now=True, verbose_name='Время изменения')
    order_is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.order_main_title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.order_slug})

    class Meta:
        verbose_name = "Карточка товара"
        verbose_name_plural = "Карточка товара"
        ordering = ['-order_maim_date_add']

class NewCategoryOrder(models.Model):
    cat_order_title = models.CharField(max_length=200, verbose_name='Название категории')
    cat_order_fk = models.ForeignKey('NewCategory', on_delete=models.PROTECT)
    cat_order_slug = models.SlugField(max_length=200, unique=True, db_index=True)

    def __str__(self):
        return self.cat_order_title

    class Meta:
        verbose_name = "Подкатегория"
        verbose_name_plural = "Подкатегории"



class NewCategory(models.Model):
    cat_title = models.CharField(max_length=200, verbose_name='Название главной категории')
    cat_slug = models.SlugField(max_length=200, unique=True, db_index=True)

    def __str__(self):
        return self.cat_title

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class NewGallery(models.Model):
    image = models.ImageField(upload_to='gallery/%Y/%m/%d/', blank=True, verbose_name="Дополнительные фотографии")
    product = models.ForeignKey(OrderNew, on_delete=models.CASCADE, related_name='images')


a = OrderNew()

