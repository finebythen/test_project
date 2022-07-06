from datetime import date
from django.db import models
from django.contrib.auth import get_user_model
from django.forms import ValidationError


USER = get_user_model()


class BaseModel(models.Model):
    """
    Model with all basic informations to abstract from in following models
    """
    id = models.BigAutoField(primary_key=True, unique=True, editable=False)
    created_from = models.ForeignKey(USER, null=False, blank=False, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Course(BaseModel):
    """
    Model that defines a tutorial course.
    """

    title = models.CharField(help_text="The title of the course.", max_length=100, null=False, blank=False, unique=True)
    start_date = models.DateField()
    end_date = models.DateField()

    class Meta:
        app_label = "app"
        verbose_name = "Course"
        verbose_name_plural = "Courses"
        ordering = ['id']

    def __str__(self) -> str:
        return self.title[:50]

    def get_absolute_url(self):
        return f"course/{self.id}/"
    
    def clean(self):
        if self.start_date > self.end_date:
            raise ValidationError('Starting date cannot be greater than ending date.')
    
    @property
    def has_started(self):
        now = date.today()
        return self.start_date <= now
    
    @property
    def has_ended(self):
        now = date.today()
        return self.end_date <= now