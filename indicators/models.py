from django.db import models


class GraduateAttribute(models.Model):
    GA_id = models.CharField(primary_key=True, max_length=8)
    title = models.CharField(max_length=50)

    def __str__(self):
        return '({}) {}'.format(self.GA_id, self.title)

    class Meta:
        verbose_name = 'Graduate Attribute'
        managed = True
        default_permissions = 'view'


class Program(models.Model):
    program_id = models.CharField(primary_key=True, max_length=4)
    name = models.CharField(default="DEFINE", max_length=50)

    # Change the way that the model displays its name
    def __str__(self):
        return self.program_id

    class Meta:
        verbose_name = 'Program'
        managed = True
        default_permissions = ('view')


class Indicator(models.Model):
    id = models.AutoField(primary_key=True)
    program = models.ForeignKey(Program, on_delete=models.DO_NOTHING)
    GA = models.ForeignKey(GraduateAttribute, on_delete=models.DO_NOTHING)
    tag = models.CharField(max_length=10)
    description = models.CharField(max_length=255)
    course_number = models.CharField(max_length=9)
    course_title = models.CharField(max_length=50)
    assessment_method = models.CharField(max_length=60)
    level = models.CharField(max_length=1,
        help_text="Enter I, D, or A: (I)ntroduced, (D)eveloped or (A)pplied")
    bins = models.CharField(max_length=20, help_text="Enter bin range tops in comma-separated values (i.e. 50, 60, 80, 100)")

    # Change the way that the model displays its name
    def __str__(self):
        return '{} Indicator: {}'.format(self.program.program_id, self.tag)

    class Meta:
        verbose_name = 'Indicator'
        managed = True
