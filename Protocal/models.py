from django.contrib import admin
from django.db import models


class DataSourceType( models.Model ):
	ID = models.AutoField( primary_key = True )
	DataSourceName = models.CharField( max_length = 32 )
	DataSourceDesc = models.CharField( max_length = 128 )

	def __str__( self ):
		return self.DataSourceName

	class Meta:
		verbose_name = '数据源'
		verbose_name_plural = '数据源类型'
		db_table = 'T_DataSource'


class DataSourceTypeAdmin( admin.ModelAdmin ):
	list_display = ( 'DataSourceName', 'DataSourceDesc' )


class MarketsSupport( models.Model ):
	ID = models.AutoField( primary_key = True )
	MkName = models.CharField( max_length = 32 )
	DataSourceID = models.ForeignKey( DataSourceType )

	def __str__( self ):
		return self.MkName

	class Meta:
		verbose_name = '市场'
		verbose_name_plural = '市场列表'
		db_table = 'T_Markets'


class MarketsSupportAdmin( admin.ModelAdmin ):
	list_display = ( 'MkName', 'DataSourceID' )


class DataType( models.Model ):
	ID = models.AutoField( primary_key = True )
	TypeName = models.CharField( max_length = 32 )
	TypeDesc = models.CharField( max_length = 128 )
	TypeDefinition = models.CharField( max_length = 64 )

	def __str__( self ):
		return self.TypeName

	class Meta:
		verbose_name = '字段类型'
		verbose_name_plural = '字段类型定义'
		db_table = 'T_DataType'


class DataTypeAdmin( admin.ModelAdmin ):
	list_display = ( 'TypeName', 'TypeDesc', 'TypeDefinition' )
	fieldsets = [
			(None, {'fields':['TypeName']}),
			('Message Field Description:', {'fields':['TypeDesc', 'TypeDefinition']}),
		]


class Message( models.Model ):
	ID = models.AutoField( primary_key = True )
	MessageID = models.IntegerField( null = True, blank = False )
	MessageName = models.CharField( max_length = 32 )
	MessageDesc = models.CharField( max_length = 64 )
	MarketID = models.ForeignKey( MarketsSupport, null = True )

	def __str__( self ):
		return self.MessageName

	class Meta:
		verbose_name = '消息描述'
		verbose_name_plural = '消息描述列表'
		db_table = 'T_Message'


class MessageAdmin( admin.ModelAdmin ):
	list_display = ( 'MessageID', 'MessageName', 'MessageDesc', 'MarketID' )
	fieldsets = [
			(None, {'fields':['MessageID', 'MessageName']}),
			('Message Definition: ', {'fields':['MessageDesc', 'MarketID']})
		]


class FieldDefinition( models.Model ):
	ID = models.AutoField( primary_key = True )
	AttributeName = models.CharField( max_length = 20 )
	AttributeType = models.ForeignKey( DataType, null = True )
	AttributeDesc = models.CharField( max_length = 128 )
	MessageID = models.ForeignKey( Message, null = True )

	def __str__( self ):
		return self.AttributeName

	class Meta:
		verbose_name = '消息字段'
		verbose_name_plural = '消息字段列表'
		db_table = 'T_Field_Definition'
		ordering=['ID']


class FieldDefinitionAdmin( admin.ModelAdmin ):
	list_display = ( 'AttributeName', 'AttributeType', 'AttributeDesc', 'MessageID' )
	search_fields = ( 'MessageID', )
	fieldsets = [
			(None, {'fields':['AttributeName']}),
			('Message Description:', {'fields':['AttributeType','AttributeDesc','MessageID']})
		]












