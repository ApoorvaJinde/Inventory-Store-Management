from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.http import HttpResponse ,request
from io import BytesIO
from django.contrib.auth.models import User
from .forms import print_billForm,Supplier_detailForm,Supplier_transactionForm,SuppliesForm,PurchaseForm, Employee_DetailsForm ,CustomerForm ,BillForm ,ShopForm ,ProductForm ,AMCForm
from .models import Supplier_detail,Supplier_transaction,Supplies,Purchase, Employee_Details ,Customer,Bill,Shop,Product,AMC
from django.views.generic import TemplateView
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.views import View
from django.db import IntegrityError
from django.http import JsonResponse
import sqlite3

from .utils import render_to_pdf 
 
#Creating our view, it is a class based view
class GeneratePdf(View):
     def get(self, request, *args, **kwargs):
        
        #getting the template
        pdf = render_to_pdf('pdf_template.html')
         
         #rendering the template
        return HttpResponse(pdf, content_type='application/pdf')

items = Customer.objects.all()
hall = Bill.objects.all()
order = {
     'items': items,
     'hall':hall,
    }



#Opens up page as PDF
class ViewPDF(View):
	def get(self, request, *args, **kwargs):
        
		pdf = render_to_pdf('inv/pdf_template.html', order)
		return HttpResponse(pdf, content_type='application/pdf')


#Automaticly downloads to PDF file
class DownloadPDF(View):
	def get(self, request, *args, **kwargs):
		
		pdf = render_to_pdf('inv/pdf_template.html', order)

		response = HttpResponse(pdf, content_type='application/pdf')
		filename = "Invoice_%s.pdf" %("12341231")
		content = "attachment; filename='%s'" %(filename)
		response['Content-Disposition'] = content
		return response

def pyt(request):
    return HttpResponse("Django hello!")

def index(request):
    return render(request, 'inv/index.html')

def add(request):
    return render(request, 'inv/add.html')

def pie_chart(request):
    queryset=Supplier_transaction.objects.order_by('a_id')[:5]
    return render(request, 'inv/chart.html', {'data':queryset})

def graph(request):
    return render(request,'inv/hi.html')

def charts(request):
    return render(request, 'inv/salechart.html')


def chartj(request):
    return render(request, 'inv/purchasechart.html')

def analysis(request):
    return render(request, 'inv/analysis.html')

def print_bill(request):
    if request.method == "POST":
        form=print_billForm(request.POST)
        if form.is_valid():
            bill_no=form.cleaned_data.get('bill_no')
        q = Bill.objects.raw('SELECT * FROM Customer as C ,Bill as B  WHERE  C.C_Id=B.Cust_Id_id and B.B_Id=%s',[bill_no])
        #b=q
        b=Bill.objects.raw('SELECT * FROM Bill WHERE B_Id=%s',[bill_no])
        
        a = Product.objects.raw('SELECT * FROM Product as PR,Purchase as P  WHERE PR.id=P.prod_info_id and P.bill_info_id=%s' ,[bill_no])
        #a = Product.objects.raw('SELECT * FROM Purchase as P ,Product as PR WHERE P.bill_info_id=%s' ,[bill_no])
        
        #a = Purchase.objects.raw('SELECT * FROM Purchase WHERE bill_info_id=%s' ,[bill_no])
        

        context = {'flower':q,'product':a,'bill':b}
        return render(request, 'inv/pdf_template.html', context)
    else:    
        form = print_billForm()
    return render(request, 'inv/search.html', {'form': form})

    

def due_payments(request):
        a=Supplier_transaction.objects.raw('SELECT * FROM Supplier_transaction  WHERE Paid_Amt<TotalAmt')
        items = {'supplier':a,'header':"DUE PAYMENTS" }
        return render(request, 'inv/supplier_trans.html', items)

def due_amc(request):
        a=AMC.objects.raw('SELECT * FROM AMC  WHERE NoOfSrvcsDone<TotalServices')
        items = {'supplier':a,'header':"DUE AMC SERVICES" }
        return render(request, 'inv/amc.html', items)

def due_bill(request):
        a=Bill.objects.raw('SELECT * FROM Bill  WHERE PaidAmt<TotalAmt')
        items = {'supplier':a,'header':"DUE PAYMENTS" }
        return render(request, 'inv/bill.html', items)





    
def hello(request):
    return render(request, 'inv/hello.html')

def purchasechart(request):
    conn=sqlite3.connect('db.sqlite3')
    c=conn.cursor()
    
    c.execute('SELECT  substr(BDate,1,7) as "Month", sum(TotalAmt) as Amount, B_Id from Bill group by substr(BDate,1,7)')
    
    Month=[]
    Amount=[]
    for key in c.fetchall():
      Month.append(key[0])
      Amount.append(key[1])
    
    return JsonResponse(data={
        'labels': Month,

        'data': Amount,
    })

def salechart(request):
    conn=sqlite3.connect('db.sqlite3')
    c=conn.cursor()
    
    c.execute('SELECT  substr(DateOfSale,1,7) as "Month", sum(TotalAmt) as Amount from Supplier_transaction group by substr(DateOfSale,1,7)')
    
    Month=[]
    Amount=[]
    for key in c.fetchall():
      Month.append(key[0])
      Amount.append(key[1])
    
    return JsonResponse(data={
        'labels': Month,

        'data': Amount,
    })


def display_Supplier_detail(request):
    items = Supplier_detail.objects.all()
    context = {
        'items': items,
        'header': 'Supplier_detail',
    }
    return render(request, 'inv/supplier_detail.html', context)
def display_Supplier_transaction(request):
    items = Supplier_transaction.objects.all()
    context = {
        'items': items,
        'header': 'Supplier_transaction',
    }
    return render(request, 'inv/supplier_trans.html', context)
def display_Supplies(request):
    items = Supplies.objects.all()
    context = {
        'items': items,
        'header': 'Supplies',
    }
    return render(request, 'inv/supplies.html', context)
def display_Purchase(request):
    items = Purchase.objects.all()
    context = {
        'items': items,
        'header': 'Purchase',
    }
    return render(request, 'inv/purchase.html', context)
def display_Employee_Details(request):
    items = Employee_Details.objects.all()
    context = {
        'items': items,
        'header': 'Employee_Details',
    }
    return render(request, 'inv/employee.html', context)
def display_Customer(request):
    items = Customer.objects.all()
    context = {
        'items': items,
        'header': 'Customer',
    }
    return render(request, 'inv/customer.html', context)
def display_Bill(request):
    items = Bill.objects.all()
    context = {
        'items': items,
        'header': 'Bill',
    }
    return render(request, 'inv/bill.html', context)
def display_Shop(request):
    items = Shop.objects.all()
    context = {
        'items': items,
        'header': 'Shop',
    }
    return render(request, 'inv/shop.html', context)
def display_Product(request):
    items = Product.objects.all()
    context = {
        'items': items,
        'header': 'Product',
    }
    return render(request, 'inv/product.html', context)
def display_AMC(request):
    items = AMC.objects.all()
    context = {
        'items': items,
        'header': 'AMC',
    }
    return render(request, 'inv/amc.html', context)

def add_item(request, cls):
    if request.method == "POST":
        form = cls(request.POST)

        if form.is_valid():
            form.save()
            return redirect('add')

    else:
        form = cls()
        return render(request, 'inv/add_new.html', {'form' : form})


def add_Supplier_detail(request):
    return add_item(request, Supplier_detailForm)

def add_Supplier_transaction(request):
    return add_item(request, Supplier_transactionForm)

def add_Supplies(request):
    return add_item(request, SuppliesForm)

def add_Purchase(request):
    return add_item(request, PurchaseForm)

def add_Employee_Details(request):
    return add_item(request, Employee_DetailsForm)

def add_Customer(request):
    return add_item(request, CustomerForm)

def add_Bill(request):
    if request.method == "POST":
        form = BillForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('add')

    else:
        form = BillForm()
        return render(request, 'inv/add_Bill.html', {'form' : form})


  

def add_Product(request):
    return add_item(request, ProductForm)

def add_AMC(request):
    return add_item(request, AMCForm)

def add_Shop(request):
    return add_item(request, ShopForm)


def edit_item(request, pk, model, cls):
    item = get_object_or_404(model, pk=pk)

    if request.method == "POST":
        form = cls(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('add')
    else:
        form = cls(instance=item)

    return render(request, 'inv/edit_item.html', {'form': form})


def edit_Supplier_detail(request, pk):
    return edit_item(request, pk, Supplier_detail, Supplier_detailForm)

def edit_Supplier_transaction(request, pk):
    return edit_item(request, pk, Supplier_transaction, Supplier_transactionForm)

def edit_Supplies(request ,pk):
    return edit_item(request, pk, Supplies, SuppliesForm)

def edit_Purchase(request ,pk):
    return edit_item(request, pk, Purchase, PurchaseForm)

def edit_Employee_Details(request, pk):
    return edit_item(request, pk, Employee_Details, Employee_DetailsForm)

def edit_Customer(request ,pk):
    return edit_item(request, pk, Customer, CustomerForm)

def edit_Bill(request, pk):
    return edit_item(request, pk, Bill, BillForm)

def edit_Product(request, pk):
    return edit_item(request, pk, Product, ProductForm)

def edit_AMC(request, pk):
    return edit_item(request, pk, AMC, AMCForm)

def edit_Shop(request, pk):
    return edit_item(request, pk, Shop, ShopForm)


def delete_Supplier_detail(request, pk):

    template = 'inv/supplier_detail.html'
    Supplier_detail.objects.filter(GSTSupplier=pk).delete()

    items = Supplier_detail.objects.all()

    context = {
        'items': items,
    }

    return render(request, template, context)

def delete_Supplier_transaction(request, pk):

    template = 'inv/supplier_trans.html'
    Supplier_transaction.objects.filter(GST_NO=pk).delete()

    items = Supplier_transaction.objects.all()

    context = {
        'items': items,
    }

    return render(request, template, context)

def delete_Supplies(request, pk):

    template = 'inv/supplies.html'
    Supplies.objects.filter(id=pk).delete()

    items = Supplies.objects.all()

    context = {
        'items': items,
    }

    return render(request, template, context)

def delete_Purchase(request, pk):

    template = 'inv/purchase.html'
    Purchase.objects.filter(id=pk).delete()

    items = Purchase.objects.all()

    context = {
        'items': items,
    }

    return render(request, template, context)

def delete_Employee_Details(request, pk):

    template = 'inv/employee.html'
    Employee_Details.objects.filter(Empid=pk).delete()

    items = Employee_Details.objects.all()

    context = {
        'items': items,
    }

    return render(request, template, context)

def delete_Customer(request, pk):

    template = 'inv/customer.html'
    Customer.objects.filter(C_Id=pk).delete()

    items = Customer.objects.all()

    context = {
        'items': items,
    }

    return render(request, template, context)

def delete_Bill(request, pk):

    template = 'inv/bill.html'
    Bill.objects.filter(B_Id=pk).delete()

    items = Bill.objects.all()

    context = {
        'items': items,
    }

    return render(request, template, context)

def delete_Product(request, pk):

    template = 'inv/product.html'
    Product.objects.filter(ProductId=pk).delete()

    items = Product.objects.all()

    context = {
        'items': items,
    }

    return render(request, template, context)

def delete_AMC(request, pk):

    template = 'inv/amc.html'
    AMC.objects.filter(id=pk).delete()

    items = AMC.objects.all()

    context = {
        'items': items,
    }

    return render(request, template, context)

def delete_Shop(request, pk):

    template = 'inv/shop.html'
    Shop.objects.filter(GSTNo=pk).delete()

    items = Shop.objects.all()

    context = {
        'items': items,
    }

    return render(request, template, context)

def pie_chart(request):
    queryset=Supplier_transaction.objects.order_by('a_id')[:5]
    return render(request, 'inv/chart.html', {'data':queryset})

def graph(request):
    return render(request,'inv/hi.html')




def aka(request):
    return render(request,'inv/analysis.html')
