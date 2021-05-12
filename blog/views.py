from django.views.generic import ListView, DetailView
#from django.shortcuts import render
from .models import Post


class BlogListView(ListView):
    model = Post
    paginate_by = 3
    template_name = 'base.html'


class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

'''
def by_rubric(request, rubric_id):
    bbs = Bb.objects.filter(rubric = rubric_id)
    rubrics = Rubric.objects.all()
    current_rubric = Rubric.objects.get(pk=rubric_id)
    context = {
        'bbs': bbs,
        'rubrics': rubrics,
        'current_rubric': current_rubric}
    return render(request, 'by_rubric.html', context)

def index(request):
    bbs = Bb.objects.all()
    rubrics = Rubric.objects.all()
    context = {
        'bbs': bbs,
        'rubrics': rubrics
        }
    return render(request, 'index.html', context)
'''
