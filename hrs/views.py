from json import dumps

from django.core.exceptions import ObjectDoesNotExist
from django import forms
from django.http import HttpResponse
from django.shortcuts import render, redirect
import pymysql
# Create your views here.
from django.urls import reverse

from hrs.models import Dept, Emp


def index(request):
    ctx = {
        'greeting': '你好,世界!'
    }
    return render(request, 'index.html', context=ctx)


def del_dept(request, no='0'):
    # no = request.GET['no']
    try:
        Dept.objects.get(pk=no).delete()
        ctx = {'code': 200}
    except (ObjectDoesNotExist, ValueError):
        ctx = {'code': 404}
    return HttpResponse(dumps(ctx), content_type='application/json; charset=utf-8')
    # return redirect(reverse('depts'))


def emps(request, no='0'):
    # no = request.GET['no']
    emps_list = list(Emp.objects.filter(dept__no=no).select_related('dept'))
    ctx = {'emp_list': emps_list, 'dept_name': emps_list[0].dept.name} if len(emps_list) > 0 else {}
    return render(request, 'emp.html', context=ctx)


def depts(request):
    # 创建连接
    ctx = {'dept_list': Dept.objects.all()}
    return render(request, 'dept.html', context=ctx)


class DeptForm(forms.Form):
    no = forms.IntegerField(max_value=100, label='部门编号', error_messages={'errors': '请输入有效的部门编号'})
    name = forms.CharField(max_length=20, label='部门名称', error_messages={'errors': '请输入有效的信息'})
    location = forms.CharField(max_length=30, label='所在位置', error_messages={'errors': '请输入有效的位置'})
    excellent = forms.BooleanField(label='是否优秀', required=False)

    """
    执行额外的表单数据验证: 
    这个方法不用调用, 自动执行
    
    def clean_no(self):
        _no = self.cleaned_data['no']
        if not condition:
            raise forms.ValidationError('...')
        return _no
    """


def add(request):
    errors = []
    if request.method == 'GET':
        f = DeptForm
    else:
        f = DeptForm(request.POST)
        if f.is_valid():
            Dept(**f.cleaned_data).save()
            # f = DeptForm
            # errors = ['添加成功']
            return render(request, 'index.html')
            # return redirect('/hrs/depts')
            # redirect 重定向  参数写路径 可以返回到指定的页面
        else:
            errors = f.errors.values()
    return render(request, 'add.html', {'f': f, 'errors': errors})
