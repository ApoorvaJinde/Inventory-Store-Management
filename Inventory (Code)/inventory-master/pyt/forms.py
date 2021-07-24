from django import forms
from .models import Supplier_detail,Supplier_transaction,Supplies,Purchase, Employee_Details ,Customer,Bill,Shop,Product,AMC
from django.forms import ModelForm

class Employee_DetailsForm(forms.ModelForm):
    class Meta:
       model = Employee_Details
       fields = ('Empid','E_FName','E_LName','AadharNo','JoinDate','Qualification','PhoneNo','Salary','Address')
       
class ShopForm(forms.ModelForm):
     class Meta:
       model = Shop
       fields = ('GSTNo','S_Name','PhoneN','Location')
        

class BillForm(forms.ModelForm):
     class Meta:
       model = Bill
       fields = ('B_Id','BDate','TotalAmt','PaidAmt','PaymentMode','Cust_Id')
       
class ProductForm(forms.ModelForm):
     class Meta:
       model = Product
       fields = ('ProductId','Brand','P_Name','Features','GSTAmt','TotalPrice')
       
class AMCForm(forms.ModelForm):
      class Meta:
        model = AMC
        fields = ('RecNo','MaintenanceYears','TotalServices','LastServiceDate','NoOfSrvcsDone','AMCQuantity')
       
class CustomerForm(forms.ModelForm):
      class Meta:
        model = Customer
        fields = ('C_Id','C_Fname','C_Lname','PhoneNumber','CustAddress')
      
       

class Supplier_detailForm(forms.ModelForm):
     class Meta:
       model = Supplier_detail
       fields = ('GSTSupplier','S_Name','ContactNo')
       

class Supplier_transactionForm(forms.ModelForm):
      class Meta:
        model = Supplier_transaction
        fields = ('GST_No','DateOfSale','TotalAmt','Paid_Amt')
     
      #def clean(self):
       # data=super(Bill,self).clean()
        #if self.PaidAmt > self.TotalAmt:
         # raise forms.ValidationError('Amount paid is more than generated')


class SuppliesForm(forms.ModelForm):
     class Meta:
       model = Supplies
       fields  = ('supp_info','pro_info','Quantity')
       

class PurchaseForm(forms.ModelForm):
     class Meta:
       model = Purchase
       fields  = ('bill_info','prod_info','Quantity_purchase','Rec_no')
       
class print_billForm(forms.Form):
  bill_no=forms.IntegerField()