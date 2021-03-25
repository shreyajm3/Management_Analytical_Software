from django.forms import ModelForm
from .models import EmployeeSkillChart, Employee


class AddEmployeeSkillScore(ModelForm):
    class Meta:
        model = EmployeeSkillChart
        fields = ['Employee_id', 'technology', 'growth', 'ideas', 'skill', 'vision', 'problem_solving']

