# Generated by Django 2.0.5 on 2018-05-22 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hrs', '0004_emp_mgr'),
    ]

    operations = [
        migrations.AddField(
            model_name='dept',
            name='excellent',
            field=models.BooleanField(default=0, verbose_name='是否优秀'),
        ),
        migrations.AlterField(
            model_name='dept',
            name='location',
            field=models.CharField(max_length=10, verbose_name='部门所在地'),
        ),
        migrations.AlterField(
            model_name='dept',
            name='name',
            field=models.CharField(max_length=20, verbose_name='部门名称'),
        ),
        migrations.AlterField(
            model_name='dept',
            name='no',
            field=models.IntegerField(primary_key=True, serialize=False, verbose_name='部门编号'),
        ),
        migrations.AlterField(
            model_name='emp',
            name='comm',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True, verbose_name='补贴'),
        ),
        migrations.AlterField(
            model_name='emp',
            name='job',
            field=models.CharField(max_length=10, verbose_name='职位'),
        ),
        migrations.AlterField(
            model_name='emp',
            name='mgr',
            field=models.IntegerField(blank=True, null=True, verbose_name='主管'),
        ),
        migrations.AlterField(
            model_name='emp',
            name='name',
            field=models.CharField(max_length=20, verbose_name='姓名'),
        ),
        migrations.AlterField(
            model_name='emp',
            name='no',
            field=models.IntegerField(primary_key=True, serialize=False, verbose_name='编号'),
        ),
        migrations.AlterField(
            model_name='emp',
            name='sal',
            field=models.DecimalField(decimal_places=2, max_digits=7, verbose_name='薪水'),
        ),
    ]
