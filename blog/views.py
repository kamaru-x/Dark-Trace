from django.shortcuts import render,redirect
from home.models import Blog,Manage_Menu
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.

########################################################################

@login_required
def blog(request):
    manage = Manage_Menu.objects.last()
    if request.method == 'POST':
        title = request.POST.get('title')
        image = request.FILES['image']
        description = request.POST.get('description')
        url = request.POST.get('url')
        smtitle = request.POST.get('smtitle')
        smkeywords = request.POST.get('smkeywords')
        smdescription = request.POST.get('smdescription')
        
        Data = Blog(Title=title,Description=description,Image=image,Url=url,SMTitle=smtitle,
        SMDescription=smdescription,SMKeywords=smkeywords)
        Data.save()
        messages.success(request,'new blog added successfully.....!')
        return redirect('blog')

    context = {
        'manage' : manage
    }
    return render(request,'blog.html',context)

########################################################################

@login_required
def manage_blog(request):
    blogs = Blog.objects.filter(Status=False)
    manage = Manage_Menu.objects.last()
    return render(request,'manage_blog.html',{'blogs':blogs,'manage':manage})

########################################################################

@login_required
def edit_blog(request,bid):
    manage = Manage_Menu.objects.last()
    blog = Blog.objects.get(id=bid)
    if request.method == 'POST':
        if len(request.FILES) != 0:
        #     if len(blog.Image) > 0:
        #         os.remove(blog.Image.path)
            blog.Image = request.FILES['image']
        #     else:
        blog.Title = request.POST.get('title')
        blog.Description = request.POST.get('description')
        blog.Url = request.POST.get('url')
        blog.SMTitle = request.POST.get('smtitle')
        blog.SMDescription = request.POST.get('smdescription')
        blog.SMKeywords = request.POST.get('smkeywords')
        blog.save()
        messages.success(request,'blog edited successfull...!')
        return redirect('.')
    context = {
        'blog' : blog,
        'manage' : manage
    }
    return render(request,'edit_blog.html',context)

########################################################################

@login_required
def remove_blog(request,bid):
    blog = Blog.objects.get(id=bid)

    blog.Status = True
    blog.save()
    messages.error(request,'blog deleted')
    return redirect('manage_blog')

########################################################################

@login_required
def remove_blog_img(request,bid):
    blog = Blog.objects.get(id=bid)

    blog.Image.delete(save=True)
    blog.save()

    return redirect('/admin/edit_blog/%s' %blog.id)

########################################################################