from django.db import models
from django.db.models.signals import post_delete, pre_save
from django.dispatch import receiver
from django.contrib.auth.models import User
import uuid
import os

# Create your models here.
def get_file_path(instance, filename):
    """
    Renames the file to a unique UUID to prevent collisions.
    Example: profiles/a1b2-c3d4-e5f6.jpg
    """
    ext = filename.split('.')[-1]
    # Generate a unique filename using UUID
    filename = f"{uuid.uuid4()}.{ext}"
    return os.path.join('profiles/', filename)

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    createdAt = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_post")

    def __str__(self):
        return f"{self.title} created by {self.user}"

class Comment(models.Model):
    text = models.TextField()
    createdAt = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_comment")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="post_comment")

    def __str__(self):
        return f"Comment of {self.post}"
    
class Profile(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    createdAt = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to=get_file_path, null=True, blank=True)
    
    def __str__(self):
        return f"{self.user.username}'s profile"
    
@receiver(post_delete, sender=Profile)
def delete_profile_image(sender, instance, **kwargs):
    """
    Deletes the physical file from the storage 
    after the Profile record is deleted.
    """
    if instance.image:
        if os.path.isfile(instance.image.path):
            os.remove(instance.image.path)

@receiver(pre_save, sender=Profile)
def delete_old_image_on_change(sender, instance, **kwargs):
    """
    Deletes the old image file from the storage 
    when a user uploads a new one.
    """
    if not instance.pk:
        return False

    try:
        old_file = Profile.objects.get(pk=instance.pk).image
    except Profile.DoesNotExist:
        return False

    new_file = instance.image
    if not old_file == new_file:
        if old_file and os.path.isfile(old_file.path):
            os.remove(old_file.path)