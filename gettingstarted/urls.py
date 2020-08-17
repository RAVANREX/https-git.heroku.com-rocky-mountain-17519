from django.urls import path, include

from django.contrib import admin

admin.autodiscover()

import hello.views

# To add a new path, first import the app:
# import blog
#
# Then add the new path:
# path('blog/', blog.urls, name="blog")
#
# Learn more here: https://docs.djangoproject.com/en/2.1/topics/http/urls/

urlpatterns = [
    path("", hello.views.index, name="index"),
    path("stock/", hello.views.stock, name="stock"),
    path("search/", hello.views.search, name="search"),
    path("login/", hello.views.login, name="login"),
    path("logout/", hello.views.logout, name="logout"),
    path("lc/", hello.views.lc, name="lc"),
    path("import/", hello.views.p_import, name="p_import"),
    path("import_hid/", hello.views.p_import_hid, name="p_import_hid"),
    path("add_product/", hello.views.add_product, name="add_product"),
    path("add_pdt_hid/", hello.views.add_pdt_hid, name="add_pdt_hid"),
    path("manage_product/", hello.views.manage_product, name="manage_product"),
	path("add_category/", hello.views.add_category, name="add_category"),
	path("add_cat_hid/", hello.views.add_cat_hid, name="add_cat_hid"),
	path("manage_category/", hello.views.manage_category, name="manage_category"),
	path("export/", hello.views.export, name="export"),
	path("invoice/", hello.views.invoice, name="invoice"),
	path("invoice_hid/", hello.views.invoice_hid, name="invoice_hid"),
	path("report/", hello.views.report, name="report"),
	path("contact_us/", hello.views.contact_us, name="contact_us"),
	path("list/", hello.views.list, name="list"),
	path("delete/", hello.views.delete, name="delete"),
	path("cat_v/", hello.views.cat_v, name="cat_v"),
	path("print/", hello.views.print, name="print"),
    path("db/", hello.views.db, name="db"),
    path("admin/", admin.site.urls),
]
