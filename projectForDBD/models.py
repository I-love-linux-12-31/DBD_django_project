from django.db import models

class Category(models.Model):
    title = models.CharField(
        max_length=64,
        null=False,

        verbose_name='Название'
    )
    description = models.TextField(
        max_length=128,

        verbose_name='Описание'
    )

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'

    def __str__(self):
        return self.title


class Supplier(models.Model):
    name = models.CharField(
        max_length=64,
        null=False,

        verbose_name='Название'
    )
    contact_info = models.TextField(
        max_length=128,
        null=False,

        verbose_name='Контакты:'
    )

    image = models.ImageField(
        "Картинка",
        upload_to="supplier_images",

        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = 'поставщик'
        verbose_name_plural = 'поставщики'

    def __str__(self):
        return str(self.name)

class Customer(models.Model):
    full_name = models.CharField(
        max_length=64,
        null=False,

        verbose_name='ФИО'
    )
    contact_info = models.TextField(
        max_length=128,
        null=False,

        verbose_name='Контакты'
    )

    class Meta:
        verbose_name = 'клиент'
        verbose_name_plural = 'клиенты'

    def __str__(self):
        return F"{self.full_name}"

class Product(models.Model):
    title = models.CharField(
        max_length=64,
        null=False,

        verbose_name='Название'
    )

    description = models.TextField(
        max_length=256,

        verbose_name='Описание'
    )

    price = models.DecimalField(
        null=False,

        max_digits=9,
        decimal_places=2,
        verbose_name='Стоимость'
    )

    quantity = models.PositiveIntegerField(
        null=False,
        default=0,

        verbose_name='Количество в наличии'
    )

    supplier = models.ManyToManyField(
        Supplier,
        null=False,

        verbose_name='Поставщик'
    )

    image = models.ImageField(
        "Картинка",
        upload_to="product_images",

        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'

    def __str__(self):
        return F"{self.title}"

class Order(models.Model):
    customer = models.ManyToManyField(
        Customer,
        null = False,

        verbose_name = 'Заказчик/покупатель'
    )

    order_date = models.DateTimeField(
        verbose_name='Время заказа'
    )

    order_amount = models.DecimalField(
        max_digits=4,
        decimal_places=1,

        verbose_name='Множитель заказа'
    )

    products = models.ManyToManyField(
        Product,
        null = True,

        verbose_name="Товары"
    )

    class Meta:
        verbose_name = 'заказ'
        verbose_name_plural = 'заказы'

    def __str__(self):
        return F"№{self.id} от {self.order_date}"
