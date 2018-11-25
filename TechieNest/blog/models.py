from django.db import models
from django.utils import timezone

class Post(models.Model):
    title=models.CharField(max_length=20)
    image=models.ImageField(null=False)
    Text_Field=models.CharField(max_length = 500)
    Slug = models.SlugField(max_length=63,help_text='A Unique Label',unique_for_month='pub_date')
    pub_date = models.DateField('date published',auto_now_add=True)
    creator=models.CharField(max_length=15)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=26,null=False)
    email=models.EmailField(max_length=30,null=False)
    website=models.URLField(max_length=200,null=True)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text
