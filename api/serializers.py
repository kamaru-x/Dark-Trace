from rest_framework import serializers
from home.models import Product,Feedback,About,Blog,Album,Album_Image,Contact,Service,Enquiry,Manage_Menu,Quick_Links,Group_Of_Companies,Testimonial,Banners,Theme,Appbnr

class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ['id','Name','Email','Contact','Website','Message']

class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = ['id','Title','Mission_Title','Mission','Vision_Title','Vision','Description','Image']

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['id','Date','Title','Description','Image']

class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ['id','Title','Thumbnail','Images']

class ImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album_Image
        fields = ['id','Album_Name','Image']

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['id','Company_Name','Adress','Telephone','Mobile','Whatsapp','Email','Website','Longitude','Latitude','Facebook','Instagram','Linkedin','Twitter','Image']

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['id','Title','Description','Image','Refer_number','Show_Price','Actual_Price','Offer_Price','Discount','Show_Whatsapp','Whatsapp_Number','Show_Enquiry','Show_Feature']

class EnquirySerializer(serializers.ModelSerializer):
    class Meta:
        model = Enquiry
        fields = ['id','Name','Mobile_Number','Email','Product_Name','Whatsapp','District','Address','Refer_number']

class HeaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manage_Menu
        fields = ['id','About_Page','Blog_Page','Image_Gallery','Contact_Page','Products_Page','Service_Page','Feedback_Page','Enquiry_Page','Group_Company','Testimonials']

class FooterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quick_Links
        fields = ['id','About_Page','Blog_Page','Image_Gallery','Contact_Page','Optional_Service','Optional_Products','Products_Page','Service_Page','Testimonials']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id','Title','Description','Image','Refer_number','Show_Price','Actual_Price','Offer_Price','Discount','Show_Whatsapp','Whatsapp_Number','Show_Enquiry','Show_Feature']

class GOCSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group_Of_Companies
        fields = ['id','Logo']

class TestimonialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonial
        fields = ['id','Tes_Name','Designation','Company_Name','Testimonial','Tes_Image']

class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appbnr
        fields = ['id','Caption','Sub_Caption','Button_Label','Link','Banner_Image']

class ThemeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Theme
        fields = ['id','Primary','Secondary']