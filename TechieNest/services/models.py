from django.db import models


class Commercial_products(models.Model):
    title=models.CharField(max_length=35)
    slug = models.SlugField(
        max_length=31,
        unique=True)

    def __str__(self):
        return self.title

class Educational_products(models.Model):
    title=models.CharField(max_length=35)
    slug = models.SlugField(
        max_length=31,
        unique=True)

    def __str__(self):
        return self.title

class Products(models.Model):
    commercial_products=models.ForeignKey(Commercial_products, on_delete = models.CASCADE)
    educational_products=models.ForeignKey(Educational_products, on_delete = models.CASCADE)

class Online_classroom(models.Model):
      title=models.CharField(max_length=35)
      slug = models.SlugField(
          max_length=31,
          unique=True)

      def __str__(self):
          return self.title

class Offline_classroom(models.Model):
      title=models.CharField(max_length=35)
      slug = models.SlugField(
          max_length=31,
          unique=True)

      def __str__(self):
          return self.title

class Trainings(models.Model):
    online_classroom=models.ForeignKey(Online_classroom, on_delete = models.CASCADE)
    offline_classroom=models.ForeignKey(Offline_classroom, on_delete = models.CASCADE)

class Trending_now(models.Model):
      title=models.CharField(max_length=35)
      slug = models.SlugField(
          max_length=31,
          unique=True)

      def __str__(self):
          return self.title

class Embedded_systems(models.Model):
      title=models.CharField(max_length=35)
      slug = models.SlugField(
          max_length=31,
          unique=True)

      def __str__(self):
          return self.title

class Robotics(models.Model):
      title=models.CharField(max_length=35)
      slug = models.SlugField(
          max_length=31,
          unique=True)

      def __str__(self):
          return self.title

class Matlab(models.Model):
      title=models.CharField(max_length=35)
      slug = models.SlugField(
          max_length=31,
          unique=True)

      def __str__(self):
          return self.title

class Automation(models.Model):
      title=models.CharField(max_length=35)
      slug = models.SlugField(
          max_length=31,
          unique=True)

      def __str__(self):
          return self.title

class Labs(models.Model):
      title=models.CharField(max_length=35)
      slug = models.SlugField(
          max_length=31,
          unique=True)

      def __str__(self):
          return self.title

class Workshops(models.Model):
    trending_now=models.ForeignKey(Trending_now, on_delete = models.CASCADE)
    embedded_systems=models.ForeignKey(Embedded_systems, on_delete = models.CASCADE)
    robotics=models.ForeignKey(Robotics, on_delete = models.CASCADE)
    matlab=models.ForeignKey(Matlab, on_delete = models.CASCADE)
    automation=models.ForeignKey(Automation, on_delete = models.CASCADE)
    labs=models.ForeignKey(Labs, on_delete = models.CASCADE)


# Create your models here.
