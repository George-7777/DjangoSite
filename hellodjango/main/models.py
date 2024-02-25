from django.db import models



class Table(models.Model):
    '''
    Это таблица
    '''
    title = models.CharField("Название", max_length=20)
    text = models.TextField("Описание товара")
    prize = models.IntegerField("Цена")
    image = models.ImageField(upload_to='image')
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

