from django.db import models
#from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class ItemList(models.Model):
    Category_name=models.CharField(max_length=20)
    
    def __str__(self):
        return self.Category_name
    
    
class Item(models.Model):
    Item_Name=models.CharField(max_length=100,blank=False)
    description=models.TextField(blank=False)
    Price=models.IntegerField()
    Category = models.ForeignKey(ItemList,related_name='Name',on_delete=models.CASCADE)
    Image=models.ImageField(upload_to='items/')

    def __str__(self): # shows item name instead of item object
        return self.Item_Name
  
class AboutUs(models.Model):
    Description=models.TextField(blank=False)
    
class Feedback(models.Model):
    User_name=models.CharField(max_length=50)
    Rating_Choices= [(i, str(i)) for i in range(1,6)]
    Rating=models.IntegerField(choices=Rating_Choices)
    Review=models.TextField(blank=False)
    Image=models.ImageField(upload_to='items/',blank=True)
    
    def __str__(self):
        return self.User_name
    
    def get_star_rating(self):
    
        return "★" * self.Rating + "☆" * (5 - self.Rating)
    
    
class BookTable(models.Model):
    Name=models.CharField(max_length=50)
    Phone_number=models.IntegerField()
    Email=models.EmailField()
    Total_person=models.IntegerField()
    Booking_date=models.DateField()

    def __str__(self):
        return self.Name