from django.db import models
from django.core.exceptions import ValidationError


def validate_name(value):
    if len(value) < 3:
        raise ValidationError(
            ('Name must be at least 3 characters.'),
            params={'value': value},
        )


class Student(models.Model):
    name = models.CharField(max_length=30, validators=[validate_name])
    college = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Faculty(models.Model):
    name = models.CharField(max_length=30, validators=[validate_name])
    college = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class FileModel(models.Model):
    file = models.FileField(upload_to='files/')
    description = models.TextField(null=True, max_length=300)
    title = models.CharField(null=True, max_length=20)
    tags = models.JSONField(null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=30)
    Types = [('Student', 'Student'), ('Faculty', 'Faculty')]
    by = models.CharField(max_length=10, choices=Types)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        try:
            this = FileModel.objects.get(id=self.id)
            if this.file != self.file:
                this.file.delete()
        except:
            pass
        super(FileModel, self).save(*args, **kwargs)
