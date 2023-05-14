from django.db import models

# Create your models here.



class RegisterEmployee(models.Model):
    
    symbols_CHOICES = (
        ('DOLLAR', "$"),
        ('EURO', "€"),
        ('RON', "ron"),
       
    )
    id   = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    first_name = models.CharField(max_length=20)
    position_occupied = models.CharField(max_length=80)
    salary = models.IntegerField(default=False)
    symbols_money = models.CharField(max_length=200, choices=symbols_CHOICES)
    
    
    class Meta:
        verbose_name_plural = 'Register members'
        
    def __str__(self):
        return f""" ID {self.id}  
    +Name: {self.name} 
    +Prenume: {self.first_name} 
    +Position-occupied: {self.position_occupied} 
    +Salary: {self.salary} 
    +Symbols_Money: {self.symbols_money}"""
    