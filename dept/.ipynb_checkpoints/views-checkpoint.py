from django.shortcuts import render
from .models import dept1, dept2, dept3

# Create your views here.
def index_dept1(request):
    dept1_list = dept1.objects.order_by('head_num')
    context = {'dept1_list' : dept1_list }
    return render(request, 'dept/dept1_list.html', context)

def index_dept2(request, head_num):
    dept2_list = dept2.objects.filter(head_num = head_num)
    context = {'dept2_list' : dept2_list }
    return render(request, 'dept/dept2_list.html', context)

def index_dept3(request, team_num_id):
    dept3_list = dept2.objects.filter('em_id', pk = team_num_id)
    context = {'dept3_list' : dept3_list }
    return render(request, 'dept/dept3_list.html', context)