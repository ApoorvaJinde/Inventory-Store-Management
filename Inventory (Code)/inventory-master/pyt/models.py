from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator
from django.core.exceptions import ValidationError
from django.core.validators import MaxLengthValidator, MinLengthValidator
from .validators import nonneg, alphanumeric, datevalid


class Shop(models.Model):
    GSTNo=models.CharField(verbose_name='GSTNo',max_length=17,primary_key=True)
    S_Name=models.CharField(verbose_name='S_Name',max_length=30)
    PhoneN=models.PositiveIntegerField(verbose_name='PhoneN',default=None)
    Location=models.CharField(verbose_name='Location',max_length=100)
    objects = models.Manager()

    class Meta: 
        verbose_name_plural='Shop'
        db_table='Shop'

class Employee_Details(models.Model):
    Empid=models.AutoField(verbose_name='Empid',primary_key=True)
    E_FName=models.CharField(verbose_name='E_FName',max_length=15)
    E_LName=models.CharField(verbose_name='E_LName',max_length=15)
    AadharNo=models.PositiveIntegerField(verbose_name='AadharNo')
    JoinDate=models.DateField(verbose_name='JoinDate',validators=[datevalid])
    Qualification=models.CharField(verbose_name='Qualification',max_length=20)
    PhoneNo=models.PositiveIntegerField (verbose_name='PhoneNo',validators=[nonneg,MaxValueValidator(9999999999,'Invalid Phone Number'),MinValueValidator(1000000000,'Invalid Phone Number')])
    Salary=models.FloatField(verbose_name='Salary',validators=[nonneg])
    Address=models.CharField(verbose_name='Address',max_length=100)
    objects = models.Manager()


    class Meta: 
        verbose_name_plural='Employee_Details'
        db_table='Employee_Details'
   
class Supplier_detail(models.Model):
    GSTSupplier=models.CharField(verbose_name='GSTSupplier',max_length=20,primary_key=True)
    S_Name=models.CharField(verbose_name='S_Name',max_length=20)
    ContactNo=models.PositiveIntegerField(verbose_name='ContactNo',validators=[nonneg,MaxValueValidator(9999999999,'Invalid Phone Number'),MinValueValidator(1000000000,'Invalid Phone Number')])
    objects = models.Manager()
    def __str__(self):
        return str('%s %s' %(self.GSTSupplier,self.S_Name))

    class Meta: 
        verbose_name_plural='Supplier_detail'
        db_table='Supplier_detail'
    
class Supplier_transaction(models.Model):
    GST_No=models.ForeignKey(Supplier_detail,on_delete=models.CASCADE,verbose_name='GST_No')
    DateOfSale=models.DateField(verbose_name='DateOfSale',validators=[datevalid])
    TotalAmt=models.FloatField(verbose_name='TotalAmt',validators=[nonneg])
    Paid_Amt=models.FloatField(verbose_name='Paid_Amt',validators=[nonneg])
    objects=models.Manager()
    
    def clean(self):
        if self.TotalAmt< self.Paid_Amt:
            raise ValidationError({'Paid_Amt': ('Paid cannot be greater than total amount')})   


    def __str__(self):
        return str('%s  %s'  %(self.GST_No,self.DateOfSale)) 

    class Meta:
        unique_together=(('GST_No'),('DateOfSale'),)
        verbose_name_plural='Supplier_transaction'
        db_table='Supplier_transaction'

class Product(models.Model):
    ProductId=models.CharField(verbose_name='ProductId',max_length=10)
    Brand=models.CharField(verbose_name='Brand',max_length=10)
    P_Name=models.CharField(verbose_name='P_Name',max_length=50)
    Features=models.CharField(verbose_name='Features',max_length=100)
    GSTAmt=models.FloatField(verbose_name='GSTAmt',validators=[nonneg])
    TotalPrice=models.FloatField(verbose_name='TotalPrice',validators=[nonneg])
    objects = models.Manager()

    def clean(self):
        if self.TotalPrice < self.GSTAmt:
            raise ValidationError({'GSTAmt': ('GST Amount cannot be greater than Total Price')})  
    
    def __str__(self):
        return str(self.ProductId) 

    class Meta:
        unique_together=(('ProductId'),('Brand'),)
        verbose_name_plural='Product'
        db_table='Product'

class Supplies(models.Model):
    supp_info=models.ForeignKey(Supplier_transaction,on_delete=models.CASCADE,verbose_name='supp_info')
    pro_info=models.ForeignKey(Product,on_delete=models.CASCADE,verbose_name='pro_info')
    Quantity=models.PositiveIntegerField(verbose_name='Quantity')
    objects = models.Manager()
    class Meta:
       unique_together=(('supp_info'),('pro_info'),)
       verbose_name_plural='Supplies'
       db_table='Supplies'

class Customer(models.Model):
    C_Id=models.AutoField(verbose_name='C_Id',primary_key=True)
    C_Fname=models.CharField(verbose_name='C_Fname',max_length=20)
    C_Lname=models.CharField(verbose_name='C_Lname',max_length=20)
    PhoneNumber=models.PositiveIntegerField(verbose_name='PhoneNumber',validators=[nonneg,MaxValueValidator(9999999999,'Invalid Phone Number'),MinValueValidator(1000000000,'Invalid Phone Number')])
    CustAddress=models.CharField(verbose_name='CustAddress',max_length=50,default="")
    objects = models.Manager()
    def __str__(self):
        return str(self.C_Id) 

    class Meta:
      unique_together=(('C_Id'),('C_Fname'),)
      verbose_name_plural='Customer'
      db_table='Customer'

PAYMENT_CHOICE=(
         ("Cash","Cash"),
         ("CreditCard","CreditCard"),
         ("BHIM","BHIM"),
     )

class Bill(models.Model):
    B_Id=models.AutoField(verbose_name='B_Id',primary_key=True)
    BDate=models.DateField(verbose_name='BDate',validators=[datevalid])
    TotalAmt=models.FloatField(verbose_name='TotalAmt',validators=[nonneg])
    PaidAmt=models.FloatField(verbose_name='PaidAmt',validators=[nonneg])
    PaymentMode=models.CharField(verbose_name='PaymentMode',max_length=10,choices=PAYMENT_CHOICE,default="Cash")
    Cust_Id=models.ForeignKey(Customer,on_delete=models.CASCADE,verbose_name='Cust_Id')
    objects = models.Manager()

    def clean(self):
        if self.TotalAmt< self.PaidAmt:
            raise ValidationError({'PaidAmt': ('Paid Amount cannot be greater than total amount')})   



    def __str__(self):
        return str(self.B_Id)
        
    class Meta: 
        verbose_name_plural='Bill'
        db_table='Bill'
    

class AMC(models.Model):
    RecNo=models.AutoField(verbose_name='RecNo',primary_key=True)
    MaintenanceYears=models.FloatField(verbose_name='MaintenanceYears',validators=[nonneg])
    TotalServices=models.PositiveIntegerField(verbose_name='TotalServices')
    LastServiceDate=models.DateField(verbose_name='LastServiceDate',validators=[datevalid])
    NoOfSrvcsDone=models.PositiveIntegerField(verbose_name='NoOfSrvcsDone')
    AMCQuantity=models.PositiveIntegerField(verbose_name='AMCQuantity')
    objects = models.Manager()

    def clean(self):
        if self.TotalServices< self.NoOfSrvcsDone:
            raise ValidationError({'NoOfSrvcsDone': ('No Of Services Done cannot be greater than TotalServices')})   

    def __str__(self):
        return str(self.RecNo)
    class Meta: 
        verbose_name_plural='AMC'
        db_table='AMC'

class Purchase(models.Model):
    bill_info=models.ForeignKey(Bill,on_delete=models.CASCADE,verbose_name='bill_info')
    prod_info=models.ForeignKey(Product,on_delete=models.CASCADE,verbose_name='prod_info')
    Quantity_purchase=models.PositiveIntegerField(verbose_name='Quantity_purchase')
    Rec_no=models.ForeignKey(AMC,on_delete=models.CASCADE,default=None,verbose_name='Rec_no')
    subtotal = models.FloatField(blank=True, null=True)
    objects = models.Manager()
    
    def clean(self):
        if self.Quantity_purchase<self.Rec_no.AMCQuantity:
            raise ValidationError({'Quantity_purchase':('Quantity purchase cannot be less than the AMC Quantities')})

    class Meta:
       unique_together=(('bill_info'),('prod_info'))
       verbose_name_plural='Purchase'
       db_table='Purchase'