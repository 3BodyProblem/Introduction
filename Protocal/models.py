from django.contrib import admin
from django.contrib.admin import SimpleListFilter
from django.db import models
from django.utils.html import format_html


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
	MarketDesc = models.CharField( max_length = 128, blank = True, null = True )

	def __str__( self ):
		return self.MkName

	class Meta:
		verbose_name = '市场'
		verbose_name_plural = '市场列表'
		db_table = 'T_Markets'


class MarketsSupportAdmin( admin.ModelAdmin ):
	list_display = ( 'MkName', 'DataSourceID', 'MarketDesc' )


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
	list_filter = ( 'ID', )
	list_display = ( 'TypeName', 'TypeDefinition', 'TypeDesc' )
	fieldsets = [
			(None, {'fields':['TypeName']}),
			('Message Field Description:', {'fields':['TypeDesc', 'TypeDefinition']}),
		]


#######################################################################################


class Message( models.Model ):
	FrequencyLevel = (
				(0, '低频数据'),
				(1, '高频数据'),
			)

	ID = models.AutoField( primary_key = True )
	MessageID = models.IntegerField( null = True, blank = False, unique=True )
	MessageName = models.CharField( max_length = 32 )
	StructureName = models.CharField( max_length = 32, null = True )
	MessageDesc = models.CharField( max_length = 64 )
	MarketID = models.ForeignKey( MarketsSupport, null = True, db_index = True )
	FrequencyLv = models.IntegerField( choices = FrequencyLevel )

	def MsgName( self ):
		return format_html( '<span style="font-weight:bold"><a href="../fielddefinition/?MessageID={0}&MarketID={1}">[ {2} ]</a></span>', self.MessageID, self.MarketID_id, self.MessageName )

	MsgName.allow_tags = True

	def __str__( self ):
		return self.MessageName

	class Meta:
		verbose_name = '消息描述'
		verbose_name_plural = '消息描述列表'
		db_table = 'T_Message'


class MessageAdmin( admin.ModelAdmin ):
	list_filter = ( 'MarketID', 'FrequencyLv' )
	list_display = ( 'MessageID', 'MsgName', 'StructureName', 'MessageDesc', 'MarketID', 'FrequencyLv' )
	fieldsets = [
			(None, {'fields':['MessageID', 'MessageName', 'FrequencyLv']}),
			('Message Definition: ', {'fields':['StructureName', 'MessageDesc', 'MarketID']})
		]


#############################################################################################


class FieldDefinition( models.Model ):
	ID = models.AutoField( primary_key = True )
	AttributeName = models.CharField( max_length = 20 )
	AttributeType = models.ForeignKey( DataType, null = True )
	AttributeDesc = models.CharField( max_length = 128 )
	MarketID = models.ForeignKey( MarketsSupport, null = True, db_index = True )
	MessageID = models.ForeignKey( Message, to_field = 'MessageID', null = True, related_name = "tags" )

	def __str__( self ):
		return self.AttributeName

	def AttrType( self ):
		return format_html( '<span style="font-weight:bold"><a href="../datatype/?ID={0}">[ {1} ]</a></span>', self.AttributeType_id, self.AttributeType )

	class Meta:
		db_table = 'T_Field_Definition'
		verbose_name = '消息字段'
		verbose_name_plural = '消息字段列表'


class MarketIDFilter( SimpleListFilter ):
	empty_value_display = '---'
	title = r'选择市场名称'
	parameter_name = 'MarketID'

	def lookups( self, request, model_admin ):
		qs = model_admin.get_queryset( request ).values( 'MarketID_id', 'MarketID__MkName' ).distinct()
		for item in qs:
			yield( item['MarketID_id'], item['MarketID__MkName'] )

	def queryset( self, request, queryset ):
		if 'MarketID' in request.GET:
			return queryset.filter( MarketID = request.GET['MarketID'] ).order_by('ID')
		else:
			return queryset


class MessageIDFilter( SimpleListFilter ):
	title = r'选择消息名称'
	parameter_name = 'MessageID'

	def lookups( self, request, model_admin ):
		qs = model_admin.get_queryset( request ).values( 'MessageID_id', 'MessageID__MessageName'  ).distinct()
		for item in qs:
			yield( item['MessageID_id'], item['MessageID__MessageName'] )

	def queryset( self, request, queryset ):
		if 'MessageID' in request.GET:
			return queryset.filter( MessageID = request.GET['MessageID'] ).order_by('ID')
		else:
			return queryset


class FieldDefinitionAdmin( admin.ModelAdmin ):
	empty_value_display = '---'
	list_filter = ( MarketIDFilter, MessageIDFilter )
	list_display = ( 'AttributeName', 'AttrType', 'AttributeDesc', 'MarketID', 'MessageID' )
	fieldsets = [
			(None, {'fields':['AttributeName', 'MarketID']}),
			('Message Description:', {'fields':['AttributeType','AttributeDesc','MessageID']})
		]











