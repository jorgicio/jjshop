from django.db import models

# Create your models here.
#class Admin:
#	pass
class CommonInfo(models.Model):
	class Meta:
		abstract = True

import base64

class Base64Field(models.TextField):
	def contribute_to_class(self, cls, name):
    		if self.db_column is None:
			self.db_column = name
		self.field_name = name + '_base64'
		super(Base64Field, self).contribute_to_class(cls, self.field_name)
		setattr(cls, name, property(self.get_data, self.set_data))
	def get_data(self, obj):
		return base64.decodestring(getattr(obj, self.field_name))

	def set_data(self, obj, data):
	        setattr(obj, self.field_name, base64.encodestring(data))

class Productos(models.Model):
	ID = models.IntegerField(primary_key=True)
	Codigo = models.CharField(max_length=12)
	Nombre = models.CharField(max_length=40)
	Descripcion = models.TextField()
	Plataforma = models.CharField(max_length=25)
	Precio = models.IntegerField()
	Img = Base64Field()


	def __unicode__(self):
		return self.Nombre
	
	def __unicode__(self):
		return self.Plataforma
	
	def __unicode__(self):
		return self.Descripcion
	class Meta(CommonInfo.Meta):
		db_table = 'Productos'
