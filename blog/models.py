from django.db import models
from django.contrib.auth.models import User
from PIL import Image
import os
from django.conf import settings


class Category(models.Model):
     name = models.CharField(max_length=255)

     def __str__(self):
          return self.name   


class Post(models.Model):
    image = models.ImageField(upload_to='blog/', default='blog/default.jpg')
    image_thumbnail = models.ImageField(upload_to='blog/')
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=255)
    content = models.TextField()
    #tags
    category = models.ManyToManyField(Category)
    counted_view = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    published_date = models.DateTimeField(null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

        

    def create_thumbnail(self):
        # Ensure the original image file exists
        if not self.image:
            return

        # Open the original image
        img = Image.open(self.image.path)

        # Get dimensions
        width, height = img.size
        
        # Determine the size of the square
        min_dim = min(width, height)

        # Calculate coordinates to crop the image to a square from the center
        left = (width - min_dim) // 2
        top = (height - min_dim) // 2
        right = (width + min_dim) // 2
        bottom = (height + min_dim) // 2

        # Crop the image to a square from the center
        img = img.crop((left, top, right, bottom))

        # Define thumbnail size
        size = (80, 80)
        img.thumbnail(size)


           
        # Generate thumbnail filename and path
        thumb_filename = f"{os.path.splitext(self.image.name)[0]}_thumb.jpg"
        thumb_path = os.path.join(thumb_filename)

        full_thumb_path = os.path.join(settings.MEDIA_ROOT, thumb_path)

        # Save the thumbnail to the filesystem
        img.save(full_thumb_path, 'JPEG', quality=95)
        
        # Save the thumbnail path relative to MEDIA_ROOT to the image_thumbnail field
        self.image_thumbnail = thumb_path
        self.save()


    class Meta:
        ordering = ('-created_date',)

    def __str__(self):
            return self.title