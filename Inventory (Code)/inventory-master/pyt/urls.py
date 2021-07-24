from django.urls import path
from django.conf.urls import url
from pyt.views import *
from django.views.generic import TemplateView

import pyt.views
from .import views


urlpatterns=[
    url(r'^$', index, name='index'),
    path('add' , views.add , name='add'),
    path('print_bill' , views.print_bill , name='print_bill'),
    path('analysis' , views.analysis , name='analysis'),
    path('pie_chart/',views.pie_chart,name='pie_chart'),
    path('graph/',views.graph,name='graph'),  
    path('chart/', views.chartj, name='chartj'),
    path('charts/', views.charts, name='charts'),
    url(r'^hello$', hello , name='hello'),
    path('purchasechart/', views.purchasechart, name='purchasechart'),
    path('salechart/', views.salechart, name='salechart'),
    url(r'^due_payments$', due_payments, name="due_payments"),
    url(r'^due_amc$', due_amc, name="due_amc"),
    url(r'^due_bill$', due_bill, name="due_bill"),

    url(r'^display_Supplier_detail$', display_Supplier_detail, name="display_Supplier_detail"),
    url(r'^display_Supplier_transaction$', display_Supplier_transaction, name="display_Supplier_transaction"),
    url(r'^display_Supplies$', display_Supplies, name="display_Supplies"),
    url(r'^display_Purchase$', display_Purchase, name="display_Purchase"),
    url(r'^display_Employee_Details$', display_Employee_Details, name="display_Employee_Details"),
    url(r'^display_Customer$', display_Customer, name="display_Customer"),
    url(r'^display_Bill$', display_Bill, name="display_Bill"),
    url(r'^display_Product$', display_Product, name="display_Product"),
    url(r'^display_AMC$', display_AMC, name="display_AMC"),
    url(r'^display_Shop$', display_Shop, name="display_Shop"),
    url(r'^add_Supplier_detail$', add_Supplier_detail, name="add_Supplier_detail"),
    url(r'^add_Supplier_transaction$', add_Supplier_transaction, name="add_Supplier_transaction"),
    url(r'^add_Supplies$', add_Supplies, name="add_Supplies"),
    url(r'^add_Purchase$', add_Purchase, name="add_Purchase"),
    url(r'^add_Employee_Details$', add_Employee_Details, name="add_Employee_Details"),
    url(r'^add_Customer$', add_Customer, name="add_Customer"),
    url(r'^add_Bill$', add_Bill, name="add_Bill"),
    
    url(r'^add_Product$', add_Product, name="add_Product"),
    url(r'^add_AMC$', add_AMC, name="add_AMC"),
    url(r'^add_Shop$', add_Shop, name="add_Shop"),
    url(r'^Supplier_detail/edit_item/(?P<pk>\d+)$', edit_Supplier_detail, name="edit_Supplier_detail"),
    url(r'^Supplier_transaction/edit_item/(?P<pk>\d+)$', edit_Supplier_transaction, name="edit_Supplier_transaction"),
    url(r'^Supplies/edit_item/(?P<pk>\d+)$', edit_Supplies, name="edit_Supplies"),
    url(r'^Purchase/edit_item/(?P<pk>\d+)$', edit_Purchase, name="edit_Purchase"),
    url(r'^Employee_Details/edit_item/(?P<pk>\d+)$', edit_Employee_Details, name="edit_Employee_Details"),
    url(r'^Customer/edit_item/(?P<pk>\d+)$', edit_Customer, name="edit_Customer"),
    url(r'^Bill/edit_item/(?P<pk>\d+)$', edit_Bill, name="edit_Bill"),
    url(r'^Product/edit_item/(?P<pk>\d+)$', edit_Product, name="edit_Product"),
    url(r'^AMC/edit_item/(?P<pk>\d+)$', edit_AMC, name="edit_AMC"),
    url(r'^Shop/edit_item/(?P<pk>\d+)$', edit_Shop, name="edit_Shop"),
    url(r'^Supplier_detail/delete/(?P<pk>\d+)$', delete_Supplier_detail, name="delete_Supplier_detail"),
    url(r'^Supplier_transaction/delete/(?P<pk>\d+)$', delete_Supplier_transaction, name="delete_Supplier_transaction"),
    url(r'^Supplies/delete/(?P<pk>\d+)$', delete_Supplies, name="delete_Supplies"),
    url(r'^Purchase/delete/(?P<pk>\d+)$', delete_Purchase, name="delete_Purchase"),
    url(r'^Employee_Details/delete/(?P<pk>\d+)$', delete_Employee_Details, name="delete_Employee_Details"),
    url(r'^Customer/delete/(?P<pk>\d+)$', delete_Customer, name="delete_Customer"),
    url(r'^Bill/delete/(?P<pk>\d+)$', delete_Bill, name="delete_Bill"),
    url(r'^Product/delete/(?P<pk>\d+)$', delete_Product, name="delete_Product"),
    url(r'^AMC/delete/(?P<pk>\d+)$', delete_AMC, name="delete_AMC"),
    url(r'^Shop/delete/(?P<pk>\d+)$', delete_Shop, name="delete_Shop")
   
    
]
 