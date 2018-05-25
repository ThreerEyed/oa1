from django.db import models

# Create your models here.


class Dept(models.Model):
    no = models.IntegerField(primary_key=True, verbose_name='部门编号')
    name = models.CharField(max_length=20, verbose_name='部门名称')
    location = models.CharField(max_length=10, verbose_name='部门所在地')
    excellent = models.BooleanField(default=0, verbose_name='是否优秀')
    # 增加描述, 这样数据库中的表名可以是我们指定的表名

    class Meta:
        db_table = 'tb_dept'

    def __str__(self):
        return self.name


class Emp(models.Model):
    no = models.IntegerField(primary_key=True, verbose_name='编号')
    name = models.CharField(max_length=20, verbose_name='姓名')
    job = models.CharField(max_length=10, verbose_name='职位')
    mgr = models.IntegerField(null=True, blank=True, verbose_name='主管')
    sal = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='薪水')
    comm = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True, verbose_name='补贴')
    dept = models.ForeignKey(Dept, on_delete=models.PROTECT)    # 实际开发中一对多是经常使用的

    class Meta:
        db_table = 'tb_emp'
