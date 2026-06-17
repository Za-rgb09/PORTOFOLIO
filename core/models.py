from django.db import models


class Hero(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    subtitle = models.TextField()

    photo = models.ImageField(
        upload_to='profile/'
    )

    cv = models.FileField(
        upload_to='cv/'
    )

    def __str__(self):
        return self.name


class Skill(models.Model):
    name = models.CharField(max_length=100)
    percentage = models.IntegerField()

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=200)

    image = models.ImageField(
        upload_to='projects/'
    )

    description = models.TextField()

    github = models.URLField(
        blank=True,
        null=True
    )

    demo = models.URLField(
        blank=True,
        null=True
    )

    def __str__(self):
        return self.title


class Certificate(models.Model):
    title = models.CharField(max_length=200)

    issuer = models.CharField(
        max_length=200
    )

    image = models.ImageField(
        upload_to='certificates/'
    )

    def __str__(self):
        return self.title


class Experience(models.Model):
    company = models.CharField(max_length=200)

    position = models.CharField(
        max_length=200
    )

    start_date = models.DateField()

    end_date = models.DateField(
        null=True,
        blank=True
    )

    description = models.TextField()

    def __str__(self):
        return self.company


class Contact(models.Model):
    name = models.CharField(max_length=100)

    email = models.EmailField()

    subject = models.CharField(
        max_length=200
    )

    message = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.name