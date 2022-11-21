from django.shortcuts import render,redirect
from home.models import About,Service,Product,Blog,Album,Album_Image,Contact,Banners,Testimonial,Group_Of_Companies,Manage_Menu,Quick_Links,Feedback,Enquiry,Theme
from django.core.paginator import Paginator
# Create your views here.

def home_page(request):
    about = About.objects.last()
    contact = Contact.objects.last()
    services = Service.objects.filter(Status=False)
    products = Product.objects.filter(Status=False)
    blogs = Blog.objects.filter(Status=False)
    banners = Banners.objects.filter(Status=False)
    bnr1 = Banners.objects.first()
    bnr2 = Banners.objects.last()
    testimonials = Testimonial.objects.filter(Status=False)
    gof = Group_Of_Companies.objects.filter(Status=False)
    menu = Manage_Menu.objects.last()
    quick = Quick_Links.objects.last()
    color = Theme.objects.last()

    fs = []

    for x in services:
        if x.Show_Feature:
            fs.append(x)

    fp = []

    for x in products:
        if x.Show_Feature:
            fp.append(x)

    context = {
        'about' : about,
        'contact' : contact,
        'services' : services,
        'products' : products,
        'blogs' : blogs,
        'banners' : banners,
        'testimonials' : testimonials,
        'gof' : gof,
        'menu' : menu,
        'quick' : quick,
        'fs' : fs,
        'fp' : fp,
        'bnr1' : bnr1,
        'bnr2' : bnr2,
        'color' : color,
    }
    return render(request,'fp/index.html',context)

#####################################################################

def header(request):
    menu = Manage_Menu.objects.last()
    quick = Quick_Links.objects.last()
    contact = Contact.objects.last()
    color = Theme.objects.last()
    context = {
        'contact' : contact,
        'menu' : menu,
        'quick' : quick,
        'color' : color
    }
    return render(request,'fp/header.html',context)

#####################################################################

def footer(request):
    services = Service.objects.filter(Status=False)
    products = Product.objects.filter(Status=False)
    contact = Contact.objects.last()
    menu = Manage_Menu.objects.last()
    quick = Quick_Links.objects.last()
    color = Theme.objects.last()
    fs = []

    for x in services:
        if x.Show_Feature:
            fs.append(x)

    fp = []

    for x in products:
        if x.Show_Feature:
            fp.append(x)
    context = {
        'services' : services,
        'products' : products,
        'contact' : contact,
        'menu' : menu,
        'quick' : quick,
        'fs' : fs,
        'fp' : fp,
        'color' : color
    }
    return render(request,'fp/footer.html',context)

#####################################################################

def about(request):
    services = Service.objects.filter(Status=False)
    products = Product.objects.filter(Status=False)
    about = About.objects.last()
    contact = Contact.objects.last()
    menu = Manage_Menu.objects.last()
    quick = Quick_Links.objects.last()
    color = Theme.objects.last()

    fs = []

    for x in services:
        if x.Show_Feature:
            fs.append(x)

    fp = []

    for x in products:
        if x.Show_Feature:
            fp.append(x)

    context = {
        'about' : about,
        'services' : services,
        'products' : products,
        'contact' : contact,
        'menu' : menu,
        'quick' : quick,
        'fs' : fs,
        'fp' : fp,
        'color' : color
    }
    return render(request,'fp/about.html',context)

#####################################################################

def service_page(request):
    products = Product.objects.filter(Status=False)
    services = Service.objects.filter(Status=False)
    contact = Contact.objects.last()
    menu = Manage_Menu.objects.last()
    quick = Quick_Links.objects.last()
    color = Theme.objects.last()

    fs = []

    for x in services:
        if x.Show_Feature:
            fs.append(x)

    fp = []

    for x in products:
        if x.Show_Feature:
            fp.append(x)

    context = {
        'services' : services,
        'products' : products,
        'contact' : contact,
        'menu' : menu,
        'quick' : quick,
        'fs' : fs,
        'fp' : fp,
        'color' : color
    }
    return render(request,'fp/services.html',context)

#####################################################################

def service_details(request,url):
    services = Service.objects.filter(Status=False)
    products = Product.objects.filter(Status=False)
    service = Service.objects.get(Url=url)
    ser3 = Service.objects.filter(Status=False).order_by('-id')[:3]
    contact = Contact.objects.last()
    menu = Manage_Menu.objects.last()
    quick = Quick_Links.objects.last()
    color = Theme.objects.last()

    fs = []

    for x in services:
        if x.Show_Feature:
            fs.append(x)

    fp = []

    for x in products:
        if x.Show_Feature:
            fp.append(x)

    if request.method == 'POST' :
        name = request.POST.get('name')
        mobile = request.POST.get('mobile')
        email = request.POST.get('email')
        whatsapp = request.POST.get('whatsapp')
        district = request.POST.get('district')
        address = request.POST.get('address')

        sname= service.Title
        refer = service.Refer_number

        data = Enquiry(Name=name,Mobile_Number=mobile,Email=email,Product_Name=sname,Whatsapp=whatsapp,
        District=district,Address=address,Refer_number=refer)
        data.save()
        return redirect('/service-details/%s' %service.Url)

    context = {
        'service' : service,
        'services' : services,
        'ser3' : ser3,
        'products' : products,
        'contact' : contact,
        'menu' : menu,
        'quick' : quick,
        'fs' : fs,
        'fp' : fp,
        'color' : color
    }
    return render(request,'fp/service-single.html',context)

#####################################################################

def product_page(request):
    products = Product.objects.filter(Status=False)
    services = Service.objects.filter(Status=False)
    contact = Contact.objects.last()
    menu = Manage_Menu.objects.last()
    quick = Quick_Links.objects.last()
    color = Theme.objects.last()

    p = Paginator(Product.objects.filter(Status=False),6)
    page = request.GET.get('page')
    product = p.get_page(page)

    fs = []

    for x in services:
        if x.Show_Feature:
            fs.append(x)

    fp = []

    for x in products:
        if x.Show_Feature:
            fp.append(x)

    context = {
        'products' : products,
        'services' : services,
        'contact' : contact,
        'menu' : menu,
        'quick' : quick,
        'product' : product,
        'fs' : fs,
        'fp' : fp,
        'color' : color
    }
    return render(request,'fp/products.html',context)

#####################################################################

def product_details(request,url):
    products = Product.objects.filter(Status=False)
    product = Product.objects.get(Url=url)
    pro3 = Product.objects.filter(Status=False).order_by('-id')[:3]
    services = Service.objects.filter(Status=False)
    contact = Contact.objects.last()
    menu = Manage_Menu.objects.last()
    quick = Quick_Links.objects.last()
    color = Theme.objects.last()

    fs = []

    for x in services:
        if x.Show_Feature:
            fs.append(x)

    fp = []

    for x in products:
        if x.Show_Feature:
            fp.append(x)

    if request.method == 'POST' :
        name = request.POST.get('name')
        mobile = request.POST.get('mobile')
        email = request.POST.get('email')
        whatsapp = request.POST.get('whatsapp')
        district = request.POST.get('district')
        address = request.POST.get('address')

        pname= product.Title
        refer = product.Refer_number

        data = Enquiry(Name=name,Mobile_Number=mobile,Email=email,Product_Name=pname,Whatsapp=whatsapp,
        District=district,Address=address,Refer_number=refer)
        data.save()
        return redirect('/product-details/%s' %product.Url)
        
    context = {
        'product' : product,
        'pro3' : pro3,
        'products' : products,
        'services' : services,
        'contact' : contact,
        'menu' : menu,
        'quick' : quick,
        'fp' : fp,
        'fs' : fs,
        'color' : color
    }
    return render(request,'fp/products-single.html',context)

#####################################################################

def blogs_page(request):
    blogs = Blog.objects.filter(Status=False)
    blog3 = Blog.objects.filter(Status=False).order_by('id')[:3]
    services = Service.objects.filter(Status=False)
    products = Product.objects.filter(Status=False)
    contact = Contact.objects.last()
    menu = Manage_Menu.objects.last()
    quick = Quick_Links.objects.last()
    color = Theme.objects.last()
    

    p = Paginator(Blog.objects.filter(Status=False),4)
    page = request.GET.get('page')
    blog = p.get_page(page)

    fs = []

    for x in services:
        if x.Show_Feature:
            fs.append(x)

    fp = []

    for x in products:
        if x.Show_Feature:
            fp.append(x)

    context = {
        'blogs' : blogs,
        'blog3' : blog3,
        'services' : services,
        'products' : products,
        'contact' : contact,
        'menu' : menu,
        'quick' : quick,
        'blog' : blog,
        'fs' : fs,
        'fp' : fp,
        'color' : color
    }
    return render(request,'fp/blog.html',context)

#####################################################################

def blog_detailed(request,url):
    blog = Blog.objects.get(Url=url)
    blog3 = Blog.objects.filter(Status=False).order_by('id')[:3]
    services = Service.objects.filter(Status=False)
    products = Product.objects.filter(Status=False)
    contact = Contact.objects.last()
    menu = Manage_Menu.objects.last()
    quick = Quick_Links.objects.last()
    color = Theme.objects.last()

    fs = []

    for x in services:
        if x.Show_Feature:
            fs.append(x)

    fp = []

    for x in products:
        if x.Show_Feature:
            fp.append(x)

    context = {
        'blog' : blog,
        'blog3' : blog3,
        'services' : services,
        'products' : products,
        'contact' : contact,
        'menu' : menu,
        'quick' : quick,
        'fs' : fs,
        'fp' : fp,
        'color' : color
    }
    return render(request,'fp/blog-details.html',context)

#####################################################################

def gallery_page(request):
    albums = Album.objects.filter(Status=False)
    services = Service.objects.filter(Status=False)
    products = Product.objects.filter(Status=False)
    contact = Contact.objects.last()
    menu = Manage_Menu.objects.last()
    quick = Quick_Links.objects.last()
    color = Theme.objects.last()

    fs = []

    for x in services:
        if x.Show_Feature:
            fs.append(x)

    fp = []

    for x in products:
        if x.Show_Feature:
            fp.append(x)

    context = {
        'albums' : albums,
        'services' : services,
        'products' : products,
        'contact' : contact,
        'menu' : menu,
        'quick' : quick,
        'fs' : fs,
        'fp' : fp,
        'color' : color
    }
    return render(request,'fp/gallery.html',context)

#####################################################################

def album_page(request,id):
    images = Album_Image.objects.filter(Album_Name=id)
    services = Service.objects.filter(Status=False)
    products = Product.objects.filter(Status=False)
    contact = Contact.objects.last()
    menu = Manage_Menu.objects.last()
    quick = Quick_Links.objects.last()
    color = Theme.objects.last()

    fs = []

    for x in services:
        if x.Show_Feature:
            fs.append(x)

    fp = []

    for x in products:
        if x.Show_Feature:
            fp.append(x)

    context = {
        'images' : images,
        'services' : services,
        'products' : products,
        'contact' : contact,
        'menu' : menu,
        'quick' : quick,
        'fs' : fs,
        'fp' : fp,
        'color' : color
    }
    return render(request,'fp/album-single.html',context)

#####################################################################

def contact_page(request):
    contact = Contact.objects.last()
    services = Service.objects.filter(Status=False)
    products = Product.objects.filter(Status=False)
    contact = Contact.objects.last()
    menu = Manage_Menu.objects.last()
    quick = Quick_Links.objects.last()
    color = Theme.objects.last()

    fs = []

    for x in services:
        if x.Show_Feature:
            fs.append(x)

    fp = []

    for x in products:
        if x.Show_Feature:
            fp.append(x)

    if request.method == 'POST' :
        name = request.POST.get('name')
        email = request.POST.get('email')
        mobile = request.POST.get('phone')
        message = request.POST.get('message')
        website = request.POST.get('subject')
        data = Feedback(Name=name,Email=email,Contact=mobile,Message=message,Website=website)
        data.save()
        return redirect('.')

    context = {
        'contact' : contact,
        'services' : services,
        'products' : products,
        'contact' : contact,
        'menu' : menu,
        'quick' : quick,
        'fp' : fp,
        'fs' : fs,
        'color' : color
    }
    return render(request,'fp/contact.html',context)

#####################################################################

def processor(request):
    color = Theme.objects.last()
    return render(request,'processor.html',{'color':color})