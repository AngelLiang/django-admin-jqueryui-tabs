from django.db import models
from django.db.models import Sum


class Customer(models.Model):
    name = models.CharField('姓名', max_length=255)
    phone = models.CharField('联系电话', max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '客户'
        verbose_name_plural = '客户'


class Product(models.Model):
    name = models.CharField('名称', max_length=255)
    price = models.DecimalField('单价', max_digits=11, decimal_places=2)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = '产品'
        verbose_name_plural = '产品'


class Order(models.Model):
    order_date = models.DateField('订单日期')
    title = models.CharField('标题', max_length=255, default='')
    amount = models.DecimalField('总金额', max_digits=11, decimal_places=2, blank=True, default=0)

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, verbose_name='客户')

    def __str__(self):
        return f'[{self.id}]{self.order_date}'

    class Meta:
        verbose_name = '订单'
        verbose_name_plural = '订单'

    def update_amount(self):
        self.amount = OrderItem.objects.filter(order=self).aggregate(Sum('amount'))['amount__sum']
        self.save(update_fields=['amount'])


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='订单')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='产品')

    quantity = models.PositiveSmallIntegerField('数量')
    price = models.DecimalField('单价', max_digits=11, decimal_places=2)
    amount = models.DecimalField('总价', max_digits=11, decimal_places=2, null=True, default=0)

    def save(self, *args, **kwargs):
        self.amount = self.quantity * self.price
        super().save(*args, **kwargs)
        self.order.update_amount()

    def delete(self, *args, **kwargs):
        super().delete(*args, **kwargs)
        self.order.update_amount()

    class Meta:
        verbose_name = '订单明细'
        verbose_name_plural = '订单明细'
        # default_permissions = ()
