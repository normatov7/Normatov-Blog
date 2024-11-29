from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from .models import Article

# LoginRequiredMixin bu user login qilgan yoki qilmaganligin tekshirish uchu ishlatiladi
# UserPassesTestMixin esa viewlarga test yozish uchun ishlatiladi yani agar foydalanuvchi testdan otsa keyin viewni ichiga kirishi mumkin

class ArticleListView(ListView):
    model = Article
    template_name = 'article_list.html'

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article_detail.html'

class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Article
    fields = ('title', 'summary', 'body', 'photo',)
    template_name = 'article_edit.html'

    # bu yerda agar user postni authori bolsa va royxatdan otgan bolsa  update qila oladi aks holda yoq shuni tekshiruvchi kod
    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Article
    template_name = 'article_delete.html'
    success_url = reverse_lazy('article_list')

    # user agar royxatdan otgan bolsa  va authori bolsa postni delete qilishi mumkin
    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    template_name = 'article_new.html'
    fields = ('title', 'summary', 'body', 'photo',)

    # user royxatdan otgan yoki otmaganligini tekshirish
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    # user super user ekanini tekshirish
    def test_func(self):
        return self.request.user.is_superuser