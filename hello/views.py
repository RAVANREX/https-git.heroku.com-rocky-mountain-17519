from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting
from .models import Product
from .models import Category
from .models import Invoice
from .models import Import

# Create your views here.
def index(request):
    oc=Import.objects.all()
    obj=Product.objects.all()
    invoice=Invoice.objects.all()

    c=0
    d=0
    a=0
    b=0
    e=0
    f=0
    k=0
    y=0
    for i in invoice:
        k=int(i.total)
        f=(e+k)
        e=f
        pass

    for i in oc:
        for j in obj:
            a=int(i.qty)
            b=int(j.pdt_price)
            d=c+(a*b)
            c=d
            break
        pass
    
    

    y=f-d
    # return HttpResponse('Hello from Python!')
    return render(request, "index.html",{"oc":oc,"d":d,"f":f,"y":y})
def login(request):
    return render(request, "login.html")
def p_import(request):
    pname=Product.objects.all()
    oc=Import.objects.all()
    return render(request, "import.html", {'pname':pname,"oc":oc})
def p_import_hid(request):
    did=request.POST.get("did")
    
    qty=request.POST.get("qty")
    oc=Import.objects.get(id=did)
    oc.qty=int(oc.qty)+int(qty)
    oc.save()

    return render(request, "import_hid.html",)
def add_product(request):
    did=request.POST.get("did")
    pdt_name=request.POST.get("pdt_name")
    pdt_price=request.POST.get("pdt_price")

    
    p=Category.objects.all()
    return render(request, "add_product.html",{'p':p,"pdt_name":pdt_name, "pdt_price":pdt_price,"did":did})
def add_pdt_hid(request):
    did=request.POST.get("did")
    if did == '':
        did='None'
    pdt_name=request.POST.get("pdt_name")
    pdt_price=request.POST.get("pdt_price")
    pdt_cat=request.POST.get("pdt_cat")
    p=Category.objects.all()
    pdt=Product.objects.filter(pdt_name=pdt_name).count()
    if pdt == 0:
        
        if did == 'None':
            obj=Product()
            obj.pdt_name=pdt_name
            obj.pdt_price=pdt_price
            obj.pdt_cat=pdt_cat
            obj.save()
            oc=Import()
            oc.pdt_name=pdt_name
            oc.qty=0
            oc.save()
        else :
            obj=Product.objects.get(id=did)
            obj.pdt_name=pdt_name
            obj.pdt_price=pdt_price
            obj.pdt_cat=pdt_cat
            obj.save()
            oc=Import.objects.get(id=did)
            oc.pdt_name=pdt_name
            oc.save()
    else:
        msg=("Product name already exist")
        return render(request, "add_product.html",{"msg":msg,'p':p,"did":did})


    
    
    
    

    
    return render(request, "add_pdt_hid.html",{"pdt_name":pdt_name, "pdt_price":pdt_price, "pdt_cat":pdt_cat})
def manage_product(request):
    pdt=Product.objects.all()
    return render(request, "manage_product.html",{'pdt':pdt})
def add_category(request):
    did=request.POST.get("did")
    cat_name=request.POST.get("cat_name")
    cat_gst=request.POST.get("cat_gst")
    

    


    return render(request, "add_category.html",{"cat_name":cat_name, "cat_gst":cat_gst,"did":did})
def add_cat_hid(request):
    did=request.POST.get("did")
    if did == '':
        did='None'

    
    cat_name=request.POST.get("cat_name")
    cat_gst=request.POST.get("cat_gst")
    cat=Category.objects.filter(cat_name=cat_name).count()
    if cat == 0:
        if did == 'None':
            cobj=Category()
            cobj.cat_name=cat_name
            cobj.cat_gst=cat_gst
            cobj.save()
        else :
            cobj=Category.objects.get(id=did)
            cobj.cat_name=cat_name
            cobj.cat_gst=cat_gst
            cobj.save()
    else:
        msg=("Category name already exist")
        return render(request, "add_category.html",{"msg":msg,"did":did})
        
        
    

    
    
    
    
    return render(request, "add_cat_hid.html", {"cat_name":cat_name, "cat_gst":cat_gst})
def manage_category(request):
    cat=Category.objects.all()
    return render(request, "manage_category.html", {'cat':cat})
def cat_v(request):

       

    return render(request, "cat_v.html", {})
def export(request):
    inv=Invoice.objects.all()
    return render(request, "export.html", {'inv':inv})
def invoice(request):
    p=Product.objects.all()
    return render(request, "invoice.html", {'p':p})
def invoice_hid(request):

    pname=request.POST.get("pname")
    qty=request.POST.get("qty")
    unitprice=request.POST.get("unitprice")
    cname=request.POST.get("cname")
    cnumber=request.POST.get("cnumber")
    dis=request.POST.get("dis")
    gst=request.POST.get("gst")
    total=((((int(unitprice)*int(qty))*int(gst)/100)+(int(unitprice)*int(qty)))-int(dis))
    oc=Import.objects.get(pdt_name=pname)
    c=int(oc.qty)-int(qty)
    if c<0 :
        msg="Product is out of stock"
        return render(request, "invoice.html",{"msg":msg})
    else :
        iobj=Invoice()
        iobj.pname=pname
        iobj.qty=qty
        iobj.unitprice=unitprice
        iobj.cname=cname
        iobj.cnumber=cnumber
        iobj.dis=dis
        iobj.gst=gst
        iobj.total=int(total)
        iobj.save()
        oc.qty=int(oc.qty)-int(qty)
        oc.save()
    
    
    oc.save()
    return render(request, "invoice_hid.html", {"pname":pname, "qty":qty, "unitprice":unitprice, "cname":cname, "cnumber":cnumber, "dis":dis,"gst":gst,"total":total})
def report(request):
    return render(request, "report.html")
def contact_us(request):
    return render(request, "contact_us.html")
def front(request):
    return render(request, "front.html")
def navbar(request):
    return render(request, "navbar.html")
def sidebar(request):
    return render(request, "sidebar.html")
def search(request):
    search=request.POST.get("search")
    msg="invoice found"
    i=Invoice.objects.filter(id=search).count()
    if i == 0:
        msg="No invoice found"

    else:
        inv=Invoice.objects.get(id=search)



    return render(request, "search.html",{"msg":msg,"inv":inv})
def stock(request):
    return render(request, "stock.html")
def list(request):
    return render(request, "list.html")
def delete(request):
    did=request.POST.get("did")
    page=request.POST.get("page")
    msg=request.POST.get("msg")
    check=request.POST.get("check")
    if check == '2':
        pdel=Product.objects.filter(id=did).delete()
        oc=Import.objects.filter(id=did).delete()
    else :
        cdel=Category.objects.filter(id=did).delete()
    

    return render(request, "delete.html", {"did":did,"page":page,"msg":msg})

def print(request):
    did=request.POST.get("did")
    psel=Invoice.objects.get(id=did)
    return render(request, "print.html",{"did":did, "psel":psel})
def lc(request):
    username=request.POST.get("username")
    password=request.POST.get("password")
    return render(request, "lc.html", {"username":username, "password":password})
def logout(request):
    return render(request, "logout.html")
def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})
