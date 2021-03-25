from django.db import models


class Project(models.Model):
    project_id = models.CharField(unique=True, default="", max_length=10)
    project_name = models.CharField(default="", max_length=30)
    number_of_days = models.IntegerField()
    number_of_employees = models.IntegerField()
    number_of_units = models.IntegerField()
    budget = models.FloatField()
    productivity = models.FloatField()

    def __str__(self):
        return self.project_id


Status = [("complete", "Complete"), ("incomplete", "Incomplete"), ("delayed", "Delayed"), ("cancelled", "Cancelled")]


class Job(models.Model):
    Project_id = models.ForeignKey(Project, on_delete=models.CASCADE, default="")
    job_name = models.CharField(max_length=30)
    job_desc = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=50, default="", choices=Status)


