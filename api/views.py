from home.models import About,Contact,Product,Feedback,Enquiry,Quick_Links,Manage_Menu,Theme,Banners,Blog,Album,Album_Image,Group_Of_Companies,Service,Testimonial
from api.serializers import ProductSerializer,AboutSerializer,ContactSerializer,FeedbackSerializer,EnquirySerializer,FooterSerializer,HeaderSerializer,ThemeSerializer,BannerSerializer,BlogSerializer,AlbumSerializer,ImagesSerializer,GOCSerializer,ServiceSerializer,TestimonialSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

@api_view(['GET'])
def home(request):
    a = About.objects.last()
    c = Contact.objects.last()
    p = Product.objects.filter(Status=1).filter(Show_Feature=1)
    s = Service.objects.filter(Status=1).filter(Show_Feature=1)
    b = Blog.objects.filter(Status=1)
    t = Testimonial.objects.filter(Status=1)
    sl = Banners.objects.filter(Status=1)
    g = Group_Of_Companies.objects.filter(Status=1)
    th = Theme.objects.last()


    about = AboutSerializer(a)
    contact = ContactSerializer(c)
    product = ProductSerializer(p,many=True)
    services = ServiceSerializer(s,many=True)
    blogs = BlogSerializer(b,many=True)
    testimonials = TestimonialSerializer(t,many=True)
    banners = BannerSerializer(sl,many=True)
    clints = GOCSerializer(g,many=True)
    theme = ThemeSerializer(th)

    data = [about.data,contact.data,product.data,services.data,blogs.data,testimonials.data,banners.data,clints.data,theme.data]

    array = {'about':data[0],'contact':data[1],'products':data[2],'services':data[3],'blogs':data[4],'testimonials':data[5],'banners':data[6],'clints':data[7],'theme':data[8]}

    return Response(array)

#####################################################################################

@api_view(['GET'])
def about_us(request):
    if request.method == 'GET':
        about = About.objects.last()
        serializer = AboutSerializer(about)
        return Response(serializer.data,status=status.HTTP_200_OK)

#####################################################################################

@api_view(['GET','POST'])
def contact_us(request):
    if request.method == 'GET':
        contact = Contact.objects.last()
        serializer = ContactSerializer(contact)
        return Response(serializer.data,status = status.HTTP_200_OK)

    if request.method ==  'POST':
        serializer2 = FeedbackSerializer(data = request.data)
        if serializer2.is_valid():
            serializer2.save()
            return Response(serializer2.data,status=status.HTTP_201_CREATED)

#####################################################################################

# @api_view(['GET','POST'])
# def feedback(request):
#     if request.method == 'GET':
#         feedbacks = Feedback.objects.filter(Status=1)
#         serializer = FeedbackSerializer(feedbacks,many=True)
#         return Response(serializer.data,status=status.HTTP_200_OK)

    # if request.method ==  'POST':
    #     serializer = FeedbackSerializer(data = request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data,status=status.HTTP_201_CREATED)       

#####################################################################################

# @api_view(['GET','POST'])
# def enquiry(request):
#     if request.method == 'GET':
#         enquiries = Enquiry.objects.filter(Status=1)
#         serializer = EnquirySerializer(enquiries,many=True)
#         return Response(serializer.data,status=status.HTTP_200_OK)

    # if request.method ==  'POST':
    #     serializer = EnquirySerializer(data = request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data,status=status.HTTP_201_CREATED)       

#####################################################################################

# @api_view(['GET'])
# def footer(request):
#     if request.method == 'GET':
#         footer = Quick_Links.objects.last()
#         serializer = FooterSerializer(footer)
#         return Response(serializer.data,status=status.HTTP_200_OK)      

#####################################################################################

@api_view(['GET','POST'])
def header(request):
    if request.method == 'GET':
        header = Manage_Menu.objects.last()
        serializer = HeaderSerializer(header)
        return Response(serializer.data,status=status.HTTP_200_OK)       

#####################################################################################

@api_view(['GET'])
def theme(request):
    if request.method == 'GET':
        theme = Theme.objects.last()
        serializer = ThemeSerializer(theme)
        return Response(serializer.data,status=status.HTTP_200_OK)       

#####################################################################################

# @api_view(['GET'])
# def banner(request):
#     if request.method == 'GET':
#         banners = Banners.objects.filter(Status=1)
#         serializer = BannerSerializer(banners,many=True)
#         return Response(serializer.data,status=status.HTTP_200_OK)      

#####################################################################################

@api_view(['GET'])
def blog(request):
    if request.method == 'GET':
        blog = Blog.objects.filter(Status=1)
        serializer = BlogSerializer(blog,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

#####################################################################################

@api_view(['GET'])
def blog_details(request,id):
    if request.method == 'GET':
        try:
            blog = Blog.objects.get(pk=id)
        except Blog.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = BlogSerializer(blog)
        return Response(serializer.data,status=status.HTTP_200_OK)

#####################################################################################

@api_view(['GET'])
def album(request):
    if request.method == 'GET':
        album = Album.objects.filter(Status=1)
        serializer = AlbumSerializer(album,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)     

#####################################################################################

@api_view(['GET'])
def album_images(request,id):
    if request.method == 'GET':
        try:
            album = Album.objects.get(pk=id)
        except Album.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        images = Album_Image.objects.filter(Album_Name=album)
        serializer = ImagesSerializer(images,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)       

#####################################################################################

# @api_view(['GET'])
# def goc(request):
#     if request.method == 'GET':
#         gof = Group_Of_Companies.objects.filter(Status=1)
#         serializer = GOCSerializer(gof,many=True)
#         return Response(serializer.data,status=status.HTTP_200_OK)       

#####################################################################################

@api_view(['GET'])
def products(request):
    if request.method == 'GET':
        products = Product.objects.filter(Status=1)
        serializer = ProductSerializer(products,many=True)
        return Response(serializer.data)

#####################################################################################

@api_view(['GET','POST'])
def product_details(request,id):
    if request.method == 'GET':
        try:
            product = Product.objects.get(pk=id)
        except Product.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = ProductSerializer(product)
        return Response(serializer.data,status=status.HTTP_200_OK)

    if request.method ==  'POST':
        serializer = EnquirySerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)

#####################################################################################

@api_view(['GET'])
def services(request):
    if request.method == 'GET':
        services = Service.objects.filter(Status=1)
        serializer = ServiceSerializer(services,many=True)
        return Response(serializer.data)

#####################################################################################

@api_view(['GET','POST'])
def service_details(request,id):
    if request.method == 'GET':
        try:
            service = Service.objects.get(pk=id)
        except Service.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = ServiceSerializer(service)
        return Response(serializer.data,status=status.HTTP_200_OK)

    if request.method ==  'POST':
        serializer = EnquirySerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)

#####################################################################################

# @api_view(['GET'])
# def testimonials(request):
#     if request.method == 'GET':
#         testimonials = Testimonial.objects.filter(Status=1)
#         serializer = TestimonialSerializer(testimonials,many=True)
#         return Response(serializer.data)