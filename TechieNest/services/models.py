from django.db import models


class Commercial_products(models.Model):
    title=models.CharField(max_length=35)
    slug = models.SlugField(
        max_length=31,
        unique=True)

    def __str__(self):
        return self.title

class Educational_products(models.Model):
    title=model.CharField(max_length=35)
    slug = models.SlugField(
        max_length=31,
        unique=True)

    def __str__(self):
        return self.title

class Products(models.Model):
    commercial_products=models.OneToMany(Commercial_products)
    educational_products=models.OneToMany(Educational_products)

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
    online_classroom=models.OneToMany(Online_classroom)
    offline_classroom=models.OneToMany(Offline_classroom)

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
    trending_now=models.OneToMany(Trending_now)
    embedded_systems=models.OneToMany(Embedded_systems)
    robotics=models.OneToMany(Robotics)
    matlab=models.OneToMany(Matlab)
    automation=models.OneToMany(Automation)
    labs=models.OneToMany(Labs)


# Create your models here.
