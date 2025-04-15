from django.db import models

class Courses(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to = 'course')
    icon = models.ImageField(upload_to = 'course')
    description = models.CharField(max_length=500)
    syllabus = models.FileField(upload_to='course')
    def __str__(self):
       return self.name

class Placement(models.Model):
    # name = models.CharField(max_length=20)
    image = models.ImageField(upload_to = 'placement')
    # qualification = models.CharField(max_length=20)
    # role = models.CharField(max_length=20)
    # placed_at = models.CharField(max_length=20)

    def __str__(self):
        return self.image.url

class Hire(models.Model):
    image = models.ImageField(upload_to = 'hire')
    position = models.CharField(max_length=50)
    def __str__(self):
        return self.image.url

class News(models.Model):
    header = models.CharField(max_length=100)
    description = models.TextField()
    def __str__(self):
        return self.header

class Stories(models.Model):
    thumbnail = models.ImageField(upload_to = 'story')
    link = models.URLField(max_length=200)
    def __str__(self):
        return self.link

class Career(models.Model):
    position = models.CharField(max_length=20)
    experiance = models.CharField(max_length=20)
    def __str__(self):
        return self.position

class Application(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    position = models.CharField(max_length=20)
    resume = models.FileField(upload_to='resumes')
    def __str__(self):
        return self.name

class Games(models.Model):
    image = models.ImageField(upload_to='games')
    link = models.URLField(max_length=200)
    category = models.CharField(max_length=30)
    def __str__(self):
        return self.category

class Contact(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    place = models.CharField(max_length=50)
    message = models.TextField()
    def __str__(self):
        return self.name

class Form(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    place = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Leads(models.Model):
    file = models.FileField(upload_to="leads", max_length=100)
   #created_at = models.DateTimeField(auto_now_add=True)

class Team(models.Model):
    name = models.CharField(max_length=20)
    image = models.ImageField(upload_to = 'team')
    position = models.CharField(max_length=20)
