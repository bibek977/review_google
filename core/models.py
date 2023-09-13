from django.db import models
import uuid

class BaseModel(models.Model):

    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        abstract = True

    
class Company(BaseModel):

    title = models.CharField(max_length=250)
    rate = models.IntegerField()
    person = models.IntegerField()

    link = models.URLField(max_length=700,blank=True,null=True)
    show = models.URLField(max_length=700,blank=True,null=True)
    post = models.URLField(max_length=700,blank=True,null=True)

    def __str__(self):
        return self.title

class Reviewer(BaseModel):

    name = models.CharField(max_length=200)
    star = models.IntegerField()
    description = models.TextField()
    date = models.DateField()
    imageLink = models.URLField(max_length=400)
    profileLink = models.URLField(max_length=400)
    comapany = models.ForeignKey(Company,on_delete=models.CASCADE, related_name='reviews')

    def __str__(self):
        return self.name
