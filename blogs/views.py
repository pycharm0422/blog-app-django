from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from .models import *
from .forms import UserRegisterForm, BlogUpdateCreate, accountUpdate, accountCreate, createComment
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.template.loader import render_to_string
from django.views.generic import ListView

# def home(request):
#     posts = Posts.objects.all()
#     context = {
#         'posts':posts,
#     }
#     return render(request, 'blogs/home.html', context)

class PostListView(ListView):
    model = Posts
    template_name = 'blogs/home.html'
    context_object_name = 'posts'



                                                                                 # REGISTER

def registerForm(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('account_set-page')
    else:
        form = UserRegisterForm()
    context = {
        'form':form,
    }
    user = User.objects.all()

    if request.user in user:
        return redirect('home-page')
    
    return render(request, 'blogs/register.html', context)

                                                                                #SET ACCOUNT

def setAccount(request):
    # profile = Profile.objects.order_by('-pk')[0]
    user = User.objects.order_by('-pk')[0]
    if request.method == 'POST':
        # form = accountCreate(request.POST, request.FILES, instance=profile)
        form = accountCreate(request.POST, request.FILES, initial={'user':user})
        if form.is_valid():
            form.save()
        return redirect('login-page')
    else:
        # form = accountCreate(instance=profile)
        form = accountCreate( initial={'user':user})

    context = {
        'form':form,
        # 'profile':profile
        'user':user
    }
    return render(request, 'blogs/account_form.html', context)

                                                                                # DETAIL POST

def detail(request, pk):
    post = Posts.objects.get(pk=pk)
    comments  = Comments.objects.filter(post__id=pk)
    # detail = get_object_or_404(Posts, pk=pk)

    if request.method == 'POST':
        comment = createComment(request.POST)
        if comment.is_valid():
            comments = request.POST.get('comment')
            comment = Comments.objects.create(post=post, user=request.user, comment=comments)
            comment.save()
        return redirect('detail-page', pk=pk)
    else:
        comment = createComment(initial={'post':post, 'user':request.user})
    # context = {
    #     'comment':comment
    # }

    context = {
        'post':post,
        'get_likes_count':post.get_likes_count(),
        'comments':comments,
        'comment':comment

    }
    return render(request, 'blogs/detail.html', context)

    
                                                                                # UPDATE BLOG


@login_required(redirect_field_name='login-page')
def updateBlog(request, pk):
    post = Posts.objects.get(id=pk)
    if request.method == 'POST':
        blog = BlogUpdateCreate(request.POST, instance=post)
        if blog.is_valid():
            blog.save()
            return redirect('home-page')

    else:
        blog = BlogUpdateCreate(instance=post)
    context = {
        'blog':blog,
    }
    if post.author != request.user:
        return redirect('home-page')
    
    return render(request, 'blogs/update.html', context)


                                                                                # CREATE BLOG

@login_required(login_url='login-page')
def createBlog(request):
    if request.method == 'POST':
        blog = BlogUpdateCreate(request.POST)
        if blog.is_valid():
            blog.save()
            return redirect('home-page')
    else:
        blog = BlogUpdateCreate(initial={'author':request.user})
    context = {
        'blog':blog
     }
    # def form_valid(blog):
    #     blog.instance.author = request.user
    return render(request, 'blogs/create.html', context)



# def likePost(request):
#     post = get_object_or_404(Posts, id=request.POST.get('post_id'))
#     is_liked = False

#     if post.likes.filter(id=request.user.id).exists():
#         post.likes.remove(request.user)
#         is_liked = False
#     else:
#         post.likes.add(request.user)
#         is_liked = True
    
#     context = {
#         'post':post,
#         'is_liked':is_liked,
#         'get_likes_count':post.get_likes_count()
#     }
#     # return HttpResponseRedirect(post.get_absolute_url())
#     if request.is_ajax():
#         html = render_to_string('blogs/like_section.html', context, request=request)
#         return JsonResponse({'form' : html})
    # return redirect('detail-page', post.id)

                                                                                    # POST LIKE


def likePost(request):
    user = request.user
    if request.method == 'POST':
        pk = request.POST.get('post_pk')
        post_obj = Posts.objects.get(pk=pk)
        if user in post_obj.likes.all():
            post_obj.likes.remove(user)
        else:
            post_obj.likes.add(user)
        
    return render(request, 'blogs/home.html')


def post_serialized_view(request):
    data = list(Posts.objects.values())
    return JsonResponse(data, safe=False)


                                                                                    # DELETE BLOG

def deleteBlog(request, pk):
    post = Posts.objects.get(id=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('home-page')
    context = {
        'post':post,
    }
    return render(request, 'blogs/delete.html', context)


                                                                                    # INDIVIDUAL POST


def individualPost(request, username):
    posts = Posts.objects.filter(author__username__contains=username)
    context = {
        'posts':posts,
        'username':username,
    }
    return render(request, 'blogs/individual.html', context)


                                                                                        # ACCOUNT


def account(request):
    profiles = request.user.profile
    posts = Posts.objects.filter(author__username__contains=profiles.user)
    if request.method == 'POST':
        form = accountUpdate(request.POST, request.FILES, instance=profiles)
        if form.is_valid():
            form.save()
        return redirect('account-page')
    else:
        form = accountUpdate(instance=profiles)

    context = {
        'form':form,
        'profiles':profiles,
        'posts':posts
    }
    return render(request, 'blogs/account.html', context)

                                                                                        # ABOUT

def about(request):
    return render(request, 'blogs/about.html')

                                                                                        # COMMENTS

