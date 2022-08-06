from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=20, verbose_name='name')
    phone = models.CharField(max_length=20, verbose_name='phone number')
    email = models.EmailField(blank=True, null=True, verbose_name='email')

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'
        db_table = 'customers'

    def __str__(self):
        return f' {self.name}; {self.email}'


class Work(models.Model):
    address = models.CharField(max_length=20, verbose_name='address')
    city = models.CharField(max_length=20, verbose_name='city')
    company = models.CharField(max_length=20, verbose_name='company')
    postalZip = models.IntegerField(blank=True, null=True, verbose_name='postal zip code')
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, verbose_name='customer')

    class Meta:
        verbose_name = 'Место работы'
        db_table = 'work_place'

    def __str__(self):
        return f' {self.company}; {self.postalZip}'


class Account(models.Model):
    pin = models.IntegerField(blank=True, null=True, verbose_name='pin code')
    acc_num = models.CharField(max_length=20, verbose_name='account number')
    pan = models.CharField(max_length=20, verbose_name='permanent account number')
    cvv = models.IntegerField(verbose_name='card verification number')
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, verbose_name='customer')

    class Meta:
        verbose_name = 'Аккаунт'
        verbose_name_plural = 'Аккаунты'
        db_table = 'accounts'

    def __str__(self):
        return f' {self.cvv}'