from django.contrib import admin
from django.db import models



class DataSourceType( models.Model ):
	ID = models.AutoField( primary_key = True )
	DataSourceName = models.CharField( max_length = 32 )
	DataSourceDesc = models.CharField( max_length = 128 )

	class Meta:
		db_table = 'T_DataSource'


class DataSourceTypeAdmin( admin.ModelAdmin ):
	list_display = ( 'DataSourceName', 'DataSourceDesc' )


class MarketsSupport( models.Model ):
	ID = models.AutoField( primary_key = True )
	MkName = models.CharField( max_length = 32 )
	DataSourceID = models.ForeignKey( DataSourceType )

	class Meta:
		db_table = 'T_Markets'


class MarketsSupportAdmin( admin.ModelAdmin ):
	list_display = ( 'MkName', 'DataSourceID' )


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
	AttributeType = models.ForeignKey( DataType, null = True )
	AttributeDesc = models.CharField( max_length = 128 )
	MarketID = models.ForeignKey( MarketsSupport, null = True )

	class Meta:
		db_table = 'T_Quotation'


class QuotationAdmin( admin.ModelAdmin ):
	list_display = ( 'AttributeName', 'AttributeType', 'AttributeDesc' )
	fieldsets = [
			(None, {'fields':['AttributeName']}),
			('Message Description:', {'fields':['AttributeType','AttributeDesc']})
		]




