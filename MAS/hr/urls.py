from django.urls import path
from . import views


urlpatterns = [
    path("Add_Employee_Skill/", views.AddEmployeeSkillScoreView.as_view(), name="add_employee_skill"),
    path("trial/", views.generate_skill_chart, name='trial'),
]