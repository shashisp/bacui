from django.db import models

class CoulumA(models.Model):
	dataa = models.CharField(max_length=100)


	def __uniocode__(self):
		return self.dataa


class CoulumB(models.Model):
	datab = models.CharField(max_length=100)


	def __unicode__(self):
		return self.datab


class CoulumC(models.Model):
	datac = models.CharField(max_length=100)


	def __unicode__(self):
		return self.datac




class CoulmD(models.Model):
	datad = models.CharField(max_length=100)


	def __unicode__(self):
		return self.datad


class CoulumE(models.Model):
	datae = models.CharField(max_length=100)


	def __unicode__(self):
		return self.datae



