from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from blog.models import Blog


class BlogCreateView(CreateView):
    model = Blog
    fields = ('title', 'content', 'preview', 'is_published',)
    success_url = reverse_lazy('blog:blog_list')


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ('title', 'content', 'preview', 'is_published',)
    success_url = reverse_lazy('blog:blog_list')

    def get_success_url(self):
        return reverse_lazy('blog:blog_view', args=[self.object.pk])



class BlogListView(ListView):
    model = Blog


class BlogDetailView(DetailView):
    model = Blog

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        obj.views_count += 1
        obj.save()
        return obj


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('blog:blog_list')
