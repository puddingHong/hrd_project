from django.db import models

# Create your models here.
'''
dept1에는 본부 번호, 본부명, 관리자 성명
dept2에는 팀번호, 팀명, 본부 번호, 담당 업무, 위치
dept3(enp)에는 사번, 이름, 팀번호, 직급 을 입력
'''

class dept1(models.Model):
    head_num = models.CharField(max_length = 5, blank = True)
    headquarters = models.CharField(max_length = 10, blank = True)
    head_man = models.CharField(max_length = 10, blank = True)
    
    def __str__(self):
        return '{} {}'.format(self.pk, self.headquarters)
    
class dept2(models.Model):
    team_num = models.CharField(max_length = 10, blank = True)
    team_name = models.CharField(max_length = 20, blank = True)
    head_num = models.ForeignKey(dept1, on_delete = models.CASCADE)
    affairs = models.TextField(blank = True)
    loc = models.TextField(blank = True)
    
    def __str__(self):
        return '{} {}'.format(self.team_num, self.team_name)
    
class dept3(models.Model):
    em_id = models.CharField(max_length = 10)
    em_name = models.CharField(max_length = 5)
    team_num = models.ForeignKey(dept2, on_delete = models.CASCADE)
    position = models.CharField(max_length = 5)
    
    def __str__(self):
        return '{} {}'.format(self.em_id, self.em_name)