from django.contrib import admin
from django.db import models


class DataType( models.Model ):
	ID = models.AutoField( primary_key = True )
	TypeName = models.CharField( max_length = 32 )
	TypeDesc = models.CharField( max_length = 128 )
	TypeDefinition = models.CharField( max_length = 64 )

	class Meta:
		db_table = 'T_DataType'


class DataTypeAdmin( admin.ModelAdmin ):
	list_display = ( 'TypeName', 'TypeDesc', 'TypeDefinition' )
	fieldsets = [
			(None, {'fields':['TypeName']}),
			('Message Field Description:', {'fields':['TypeDesc', 'TypeDefinition']}),
		]


class Quotation( models.Model ):
	ID = models.AutoField( primary_key = True )
	AttributeName = models.CharField( max_length = 20 )
	AttributeType = models.ForeignKey( DataType )
	AttributeDesc = models.CharField( max_length = 128 )

	class Meta:
		db_table = 'T_Quotation'


class QuotationAdmin( admin.ModelAdmin ):
	pass





