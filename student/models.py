from django.db import models
from django.urls import reverse
from django.core.validators import MinValueValidator
from subject.models import Subject
from course.models import Course
# from PIL import Image


def sem():
    _1 = 'year 1 sem 1'
    _2 = 'year 1 sem 2'
    _3 = 'year 2 sem 1'
    _4 = 'year 2 sem 2'
    _5 = 'year 3 sem 1'
    _6 = 'year 3 sem 2'
    _7 = 'year 4 sem 1'
    _8 = 'year 4 sem 2'
    
    semester_choices = ((_1, 'year 1 sem 1'), (_2, 'year 1 sem 2'), (_3, 'year 2 sem 1'), (_4, 'year 2 sem 2'), (_5, 'year 3 sem 1'),
                        (_6, 'year 3 sem 2'), (_7, 'year 4 sem 1'), (_8, 'year 4 sem 2'), 
                        )
    return semester_choices


class Student(models.Model):

    roll_no = models.PositiveIntegerField(validators=[MinValueValidator(1)], unique=True)
    name = models.CharField(max_length=250)
    course = models.ForeignKey(Course, on_delete=models.PROTECT)
    sem = models.CharField(max_length=12, choices=sem())
    subject = models.ManyToManyField(Subject)
    image = models.ImageField(upload_to='student_pics/', default='student_pics/default.png', max_length=500)

    def __str__(self):
        return self.name

    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)
    #     img = Image.open(self.image.path)
    #     if img.height > 300 or img.width > 300:
    #         outputSize = (300, 300)
    #         img.thumbnail(outputSize)
    #         img.save(self.image.path)

    def get_absolute_url(self, **kwargs):
        return reverse('student-detail', kwargs={'pk': self.pk})
