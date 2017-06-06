from django.contrib import admin
from .models import *


admin.site.site_header = "研发接口文档(Barry)"
admin.site.register( DataSourceType, DataSourceTypeAdmin )
admin.site.register( MarketsSupport, MarketsSupportAdmin )
admin.site.register( DataType, DataTypeAdmin )
admin.site.register( Message, MessageAdmin )
admin.site.register( FieldDefinition, FieldDefinitionAdmin )




