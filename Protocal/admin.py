from django.contrib import admin
from .models import *


admin.site.register( DataType, DataTypeAdmin )
admin.site.register( Quotation, QuotationAdmin )




