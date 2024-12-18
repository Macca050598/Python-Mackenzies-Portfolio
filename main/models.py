from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.name
    
# Create your models here.
#Inherit from base model
class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    tags = models.ManyToManyField(Tag, related_name="projects")
    link = models.URLField(max_length=200, blank=True)
    
    def __str__(self):
        return self.title

#We don't add the main image line to the Project above, due to us wanting to have multiple 
#So this model will store all images
class ProjectImage(models.Model):
    #ForeignKey - we only have a single image per project, image doesnt apply to multiple projects 
    #Cascade on delete means we delete all the images associated with the project if the main project is deleted.
    project = models.ForeignKey(Project, related_name="images", on_delete=models.CASCADE)
    #Specific where we want to store the images. 
    image = models.ImageField(upload_to="project_images/")
    
    def __str__(self):
        return f"{self.project.title} Image"