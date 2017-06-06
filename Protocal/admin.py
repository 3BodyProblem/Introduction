from django.contrib import admin
from .models import *


admin.site.register( DataSourceType, DataSourceTypeAdmin )
admin.site.register( MarketsSupport, MarketsSupportAdmin )
admin.site.register( DataType, DataTypeAdmin )
admin.site.register( Quotation, QuotationAdmin )




