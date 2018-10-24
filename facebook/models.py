from django.db import models

# Create your models here.
class article(models.Model):
  author = models.CharField (max_length=120)
  title = models.CharField(max_length=120)
  text=models.TextField()
  password =models.CharField(max_length=120)
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
      return self.text[:10]

class Comment(models.Model):
    article = models.ForeignKey(article, on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=120)
    title = models.CharField(max_length=120)
    text = models.TextField()
    password = models.CharField(max_length=120)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text[:10]


class page(models.Model):
   master = models.CharField(max_length=120)
   name = models.CharField(max_length=120, default='홍길동')
   text = models.TextField()
   category = models.CharField(max_length=120)
   created_at = models.DateTimeField(auto_now_add=True)


class good(models.Model):
   master = models.CharField(max_length=120)
   name = models.CharField(max_length=120)
   text = models.TextField()
   category = models.CharField(max_length=120)
   created_at = models.DateTimeField(auto_now_add=True)

