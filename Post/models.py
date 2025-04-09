from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Post(models.Model):
    
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.CharField(max_length=200)
    description = models.TextField()
    image= models.ImageField(upload_to='Post_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
    
    
class Answer(models.Model):
    
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    post=models.ForeignKey(Post, on_delete=models.CASCADE)
    image= models.ImageField(upload_to='Answer_images/', blank=True, null=True)
    answer = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.post.question    