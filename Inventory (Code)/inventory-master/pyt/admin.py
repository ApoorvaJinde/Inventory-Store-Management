from django.contrib import admin
from totalsum.admin import TotalsumAdmin
from .models import Supplier_detail,Supplier_transaction,Supplies,Purchase, Employee_Details ,Customer,Bill,Shop,Product,AMC
from django.db import IntegrityError
from django.db.models import Sum, F

class PurchaseAdmin(admin.ModelAdmin):
    list_display=('bill_info','prod_info','Quantity_purchase','Rec_no','subtotal')

class PurchaseInline(admin.TabularInline):
     model=Purchase
     extra=0
     readonly_fields = ['get_subtotal']
    # exclude redundant field being replaced by helper method
     exclude = ['subtotal']


    # gets subtotal of each entry
     def get_subtotal(self,objects ):
        # for a given entry, find that id
        entry = Purchase.objects.get(id=objects.id)
        # subtotal the entry quantity * its related price
        #entry_subtotal = obj.Quantity_purchase * 10
        entry_subtotal = (objects.Quantity_purchase * objects.prod_info.TotalPrice)+objects.Quantity_purchase * objects.prod_info.TotalPrice*objects.prod_info.GSTAmt/100
        # check if entry obj has a subtotal and try to save to db
        try:
                entry.subtotal = entry_subtotal
                entry.save()
        except DecimalException as e:
                print(e)
        # return a str representation of entry subtotal
        return str(entry_subtotal)
    # set helper method's description display
     get_subtotal.short_description = 'subtotal'
    


# initialization of variable DecimalException
TotalAmt = 0

class BillAdmin(admin.ModelAdmin):
    inlines=(PurchaseInline,)
    list_filter=('PaymentMode','Cust_Id','BDate')
    search_fields=('C_Fname','BDate','PaymentMode','Cust_Id')
    list_display=('B_Id','BDate','TotalAmt','PaidAmt','PaymentMode','Cust_Id')
    totalsum_list = ('TotalAmt', 'PaidAmt')
    unit_of_measure = '₹'
   # change_list_template = 'inv/change_list_graph.html'
    readonly_fields = ['get_total']
    
    def get_total(self, objects):
        # extend scope of variable
        global TotalAmt
        # get all entries for the given cart
        entries = Purchase.objects.filter(bill=Bill.objects.get(id=objects.id))
        # iterate through entries
        for entry in entries:
            # if entry obj has a subtotal add it to total_price var
            if entry.subtotal:
                TotalAmt += entry.subtotal
        print(objects.TotalAmt)
        # assign cart obj's total_price field to total_price var
        objects.TotalAmt = TotalAmt
        # save to db
        objects.save()
        # reset total_price var
        TotalAmt = 0
        # return cart's total price to be displayed
        return objects.TotalAmt
        
    # give the helper method a description to be displayed
   

    class Media:
      js = ('js/bill.js',)

class SuppliesInline(admin.TabularInline):
     model=Supplies
     extra=0

class Supplier_transactionAdmin(admin.ModelAdmin):
    inlines=(SuppliesInline,)
    search_fields=('GST_No','DateOfSale',)
    list_filter=('GST_No','DateOfSale')
    list_display=('GST_No','DateOfSale','TotalAmt','Paid_Amt')
    totalsum_list = ('TotalAmt', 'Paid_Amt')
    unit_of_measure = '₹'


class SuppliesAdmin(admin.ModelAdmin):
    list_display=('supp_info','pro_info','Quantity')

class Employee_DetailsAdmin(admin.ModelAdmin):
    list_display=('Empid','E_FName','E_LName','AadharNo','JoinDate','Qualification','PhoneNo','Salary','Address')

class ShopAdmin(admin.ModelAdmin):
    list_display=('GSTNo','S_Name','PhoneN','Location')

class ProductAdmin(admin.ModelAdmin):
    search_fields=('ProductId','Brand','P_Name','Features',)
    list_filter=('ProductId','Brand','P_Name','Features')
    list_display=('ProductId','Brand','P_Name','Features','GSTAmt','TotalPrice')

class AMCAdmin(admin.ModelAdmin):
    search_fields=('RecNo',)
    list_display=('RecNo','MaintenanceYears','TotalServices','LastServiceDate','NoOfSrvcsDone','AMCQuantity')

class CustomerAdmin(admin.ModelAdmin):
    list_filter=('C_Id','C_Fname','PhoneNumber')
    search_fields=('C_Id','C_Fname','PhoneNumber',)
    list_display=('C_Id','C_Fname','C_Lname','PhoneNumber','CustAddress')

class Supplier_detailAdmin(admin.ModelAdmin):
    list_filter=('GSTSupplier','S_Name','ContactNo')
    search_fields=('GSTSupplier','S_Name','ContactNo',)
    list_display=('GSTSupplier','S_Name','ContactNo')



admin.site.register(Employee_Details,Employee_DetailsAdmin)
admin.site.register(Customer,CustomerAdmin)
admin.site.register(Bill,BillAdmin)
admin.site.register(Shop,ShopAdmin)
admin.site.register(Product,ProductAdmin)
admin.site.register(AMC,AMCAdmin)
admin.site.register(Supplier_detail,Supplier_detailAdmin)
admin.site.register(Supplier_transaction,Supplier_transactionAdmin)
admin.site.register(Supplies,SuppliesAdmin)
admin.site.register(Purchase,PurchaseAdmin)
