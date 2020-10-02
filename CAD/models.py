from django.db import models


# Create your models here.


class Shaft(models.Model):
    dia_min = models.SmallIntegerField()
    dia_max = models.SmallIntegerField()
    a = models.SmallIntegerField()
    c = models.SmallIntegerField()
    d = models.SmallIntegerField()
    e = models.SmallIntegerField()
    f = models.SmallIntegerField()
    g = models.SmallIntegerField()
    h = models.SmallIntegerField()
    j = models.SmallIntegerField()
    k_under_IT7 = models.SmallIntegerField()
    k_above_IT7 = models.SmallIntegerField()
    m = models.SmallIntegerField()
    n = models.SmallIntegerField()
    p = models.SmallIntegerField()
    r = models.SmallIntegerField()
    s = models.SmallIntegerField()

    def __str__(self):
        self.name = f'>{self.dia_min} <={self.dia_max} '
        return self.name


class Hole(models.Model):
    dia_min = models.SmallIntegerField()
    dia_max = models.SmallIntegerField()
    a = models.SmallIntegerField()
    c = models.SmallIntegerField()
    d = models.SmallIntegerField()
    e = models.SmallIntegerField()
    f = models.SmallIntegerField()
    g = models.SmallIntegerField()
    h = models.SmallIntegerField()
    j = models.SmallIntegerField()
    k = models.SmallIntegerField()
    m = models.SmallIntegerField()
    n = models.SmallIntegerField()
    p = models.SmallIntegerField()
    r = models.SmallIntegerField()
    s = models.SmallIntegerField()

    def __str__(self):
        self.name = f'>{self.dia_min} <={self.dia_max} '
        return self.name


class Lambda(models.Model):
    dia_min = models.SmallIntegerField()
    dia_max = models.SmallIntegerField()
    IT3 = models.SmallIntegerField()
    IT4 = models.SmallIntegerField()
    IT5 = models.SmallIntegerField()
    IT6 = models.SmallIntegerField()
    IT7 = models.SmallIntegerField()
    IT8 = models.SmallIntegerField()

    def __str__(self):
        self.name = f'>{self.dia_min} <={self.dia_max} '
        return self.name


class IT(models.Model):
    dia_min = models.SmallIntegerField()
    dia_max = models.SmallIntegerField()
    IT1 = models.SmallIntegerField()
    IT2 = models.SmallIntegerField()
    IT3 = models.SmallIntegerField()
    IT4 = models.SmallIntegerField()
    IT5 = models.SmallIntegerField()
    IT6 = models.SmallIntegerField()
    IT7 = models.SmallIntegerField()
    IT8 = models.SmallIntegerField()
    IT9 = models.SmallIntegerField()
    IT10 = models.SmallIntegerField()
    IT11 = models.SmallIntegerField()
    IT12 = models.SmallIntegerField()
    IT13 = models.SmallIntegerField()
    IT14 = models.SmallIntegerField()
    IT15 = models.SmallIntegerField()
    IT16 = models.SmallIntegerField()
    IT17 = models.SmallIntegerField()
    IT18 = models.SmallIntegerField()

    def __str__(self):
        self.name = f'>{self.dia_min} <={self.dia_max} '
        return self.name