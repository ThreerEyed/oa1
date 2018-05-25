from django.contrib import admin

# Register your models here.
from hrs.models import Dept, Emp


class DeptAdmin(admin.ModelAdmin):     # 定义一个部门类管理

    list_display = ('no', 'name', 'location', 'excellent')    # 展示信息
    ordering = ('no', )  # must be a list or tuple


class EmpAdmin(admin.ModelAdmin):     # 定义一个员工类管理
    list_display = ('no', 'name', 'job', 'mgr', 'sal', 'comm', 'dept')  # 展示信息
    search_fields = ('name', 'job')   # 做一个搜索框


admin.site.register(Dept, DeptAdmin)    # 管理
admin.site.register(Emp, EmpAdmin)
