# coding=utf-8
__author__ = 'taksenov'

from django.db import models
from django.core.urlresolvers import reverse_lazy

# Таблица с преподавателями (основными)
class professors(models.Model):
    fio = models.CharField(max_length=150)
    standing = models.CharField(max_length=150)
    seniority = models.CharField(max_length=150)
    categoty =  models.CharField(max_length=150)
    dateofcategory = models.DateField(null=True)
    education = models.CharField(max_length=150)
    colledge =  models.CharField(max_length=2500)
    isdualjobholder = models.BooleanField(default=False)
    datetime = models.DateTimeField(auto_now=True, null=True)

    def __unicode__(self):
        return self.fio

# Таблица с преподавателями (дополнительными)
class professors2(models.Model):
    fio = models.CharField(max_length=150)
    standing = models.CharField(max_length=150)
    education = models.CharField(max_length=150)
    categoty =  models.CharField(max_length=150)
    dateofcategory = models.DateField(null=True)

    def __unicode__(self):
        return self.fio

# Таблица с внешними совместителями
class dual_job_holder(models.Model):
    fio = models.CharField(max_length=150)

    def __unicode__(self):
        return self.fio

