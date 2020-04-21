from django.db import models


class Company(models.Model):
  name = models.CharField(max_length=400, default='some')
  description = models.TextField(default='')
  city = models.CharField(max_length=300, default='Something')
  address = models.TextField(default='')

  def to_json(self):
    return {
      'id': self.id,
      'name': self.name,
      'description': self.description,
      'city': self.city,
      'address': self.address
    }


class Vacancy(models.Model):
  name = models.CharField(max_length=300, default='name1')
  salary = models.FloatField(default=1000)
  description = models.TextField(default='')
  comp = models.ForeignKey(Company, on_delete=models.CASCADE,  default='')


  def to_json(self):
    return {
     'id': self.id,
     'name': self.name,
     'salary': self.salary,
     'description': self.description,
    }
