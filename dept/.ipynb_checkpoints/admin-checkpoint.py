from django.contrib import admin

# Register your models here.
from .models import dept1, dept2, dept3

# dept1에 검색창 추가
class dept1_search(admin.ModelAdmin):
    search_fields = ['headquarters']

# dept2에 검색창 추가
class dept2_search(admin.ModelAdmin):
    search_fields = ['team_name']

class dept3_search(admin.ModelAdmin):
    search_fields = ['em_name']

admin.site.register(dept1, dept1_search)
admin.site.register(dept2, dept2_search)
admin.site.register(dept3, dept3_search)
