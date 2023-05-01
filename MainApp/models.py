from django.db import models
from django.contrib.auth.models import User


class Display(models.Model):
    display = models.CharField(max_length=100)

    def __str__(self):
        return self.display


class DisplayType(models.Model):
    display_type = models.CharField(max_length=10)

    def __str__(self):
        return self.display_type


class Processor(models.Model):
    processor = models.CharField(max_length=20)

    def __str__(self):
        return self.processor


class Cores(models.Model):
    cores = models.PositiveSmallIntegerField()

    def __str__(self):
        return str(self.cores)


class Frequency(models.Model):
    frequency = models.CharField(max_length=10)

    def __str__(self):
        return self.frequency


class GraphicsCard(models.Model):
    graphics_card = models.CharField(max_length=100)

    def __str__(self):
        return self.graphics_card


class RAM(models.Model):
    ram = models.CharField(max_length=10)

    def __str__(self):
        return self.ram


class HardDisk(models.Model):
    hard_disk = models.CharField(max_length=10)

    def __str__(self):
        return self.hard_disk


class CacheMemory(models.Model):
    cache_memory = models.CharField(max_length=10)

    def __str__(self):
        return self.cache_memory


class OS(models.Model):
    os = models.CharField(max_length=100)

    def __str__(self):
        return self.os


class ProcessorModel(models.Model):
    processor_model = models.CharField(max_length=100)

    def __str__(self):
        return self.processor_model


class Notebook(models.Model):
    disp = models.ForeignKey(Display, on_delete=models.PROTECT, null=True, verbose_name='Экран')
    disp_type = models.ForeignKey(DisplayType, on_delete=models.PROTECT, null=True, verbose_name='Тип экрана')
    proc = models.ForeignKey(Processor, on_delete=models.PROTECT, null=True, verbose_name='Процессор')
    core = models.ForeignKey(Cores, on_delete=models.PROTECT, null=True, verbose_name='Количество ядер процессора')
    freq = models.ForeignKey(Frequency, on_delete=models.PROTECT, null=True,
                             verbose_name='Максимальная тактовая частота процессора')
    gc = models.ForeignKey(GraphicsCard, on_delete=models.PROTECT, null=True, verbose_name='Видеокарта')
    r_a_m = models.ForeignKey(RAM, on_delete=models.PROTECT, null=True, verbose_name='Объём оперативной памяти')
    hd = models.ForeignKey(HardDisk, on_delete=models.PROTECT, null=True, verbose_name='Объём памяти жёсткого диска')
    cm = models.ForeignKey(CacheMemory, on_delete=models.PROTECT, null=True, verbose_name='Объём кэш-памяти')
    o_s = models.ForeignKey(OS, on_delete=models.PROTECT, null=True, verbose_name='Операционная система')
    creation_date = models.DateTimeField(auto_now=True, verbose_name='Дата создания')
    price = models.PositiveIntegerField(blank=True, verbose_name='Цена')
    discount = models.BooleanField(default=0, verbose_name='Скидка')
    proc_mod = models.ForeignKey(ProcessorModel, on_delete=models.PROTECT, null=True, verbose_name='Модель процессора')

    class Meta:
        ordering = ('price',)
