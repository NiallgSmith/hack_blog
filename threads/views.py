from django.shortcuts import render, get_object_or_404
from threads.models import Subject, Thread, Post
from django.shortcuts import redirect
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.template.context_processors import csrf
from .forms import ThreadForm, PostForm


# Create your views here.

def forum(request):
    return render(request, 'forum.html', {'subjects':Subject.objects.all()})

def threads(request, subject_id):
    subject = get_object_or_404(Subject, pk=subject_id)
    return render(request, 'threads.html', {'subject':subject})

def thread(request, thread_id):
    thread_ = get_object_or_404(Thread, pk=thread_id)
    args = {'thread': thread_}
    args.update(csrf(request))
    return render(request, 'thread.html', args)

@login_required
def new_thread(request, subject_id):
    subject = get_object_or_404(Subject, pk=subject_id)
    # This is saying if the request is a POST (normally means a form was submitted, your new thread button is just a link, so it sends a GET request, so none of the code in the if is running
    # skips this if, which has no else
    if request.method == "POST":
        thread_form = ThreadForm(request.POST)
        post_form = PostForm(request.POST)
        if thread_form.is_valid() and post_form.is_valid():
            thread = thread_form.save(False)
            thread.subject = subject
            thread.user = request.user
            thread.save()

            post = post_form.save(False)
            post.user = request.user
            post.thread = thread
            post.save()

            messages.success(request, "You have created a new thread!")

            return redirect(reverse('thread', args={thread.pk}))

    thread_form = ThreadForm()
    post_form = PostForm(request.POST)

    args = {
        'thread_form' : thread_form,
        'post_form' : post_form,
        'subject' : subject,
    }
    args.update(csrf(request))

    return render(request, 'thread_form.html', args)
    
@login_required
def new_post(request, thread_id):
    thread = get_object_or_404(Thread, pk=thread_id)
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(False)
            post.thread = thread
            post.user = request.user
            post.save()

            messages.success(request, "Your post hasbeen added to the thread!")

            return redirect(reverse('thread', args={thread.pk}))

    else:
        form = PostForm()

    args = {
        'form' : form,
        'form_action' : reverse('new_post', args={thread.id}),
        'button_text' : 'Update Post',
    }
    args.update(csrf(request))

    return render(request, 'post_form.html', args)

@login_required
def edit_post(request, thread_id, post_id):
    thread = get_object_or_404(Thread, pk=thread_id)
    post = get_object_or_404(Post, pk=post_id)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, "You have updated your thread!")

            return redirect(reverse('thread', args={thread.pk}))

    else:
        form = PostForm(instance=post)

    args = {
        'form': form,
        'form_action': reverse('edit_post', kwargs={"thread_id" : thread_id, "post_id" : post_id}),
        'button_text': 'Update Post'
    }
    args.update(csrf(request))

    return render(request, 'post_form.html', args)

@login_required
def delete_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    thread_id = post.thread_id
    post.delete()

    messages.success(request, "Post deleted!")

    return redirect(reverse('thread', args={thread_id}))
#    return redirect(reverse('thread', args=(thread_id, post_id)))



