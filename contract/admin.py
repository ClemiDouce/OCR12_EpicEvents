from django.contrib import admin

# Register your models here.
from contract.models import Contract


@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    list_display = ('saleContact', 'client', 'status', 'amount', 'paymentDue')
