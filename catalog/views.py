from django.shortcuts import render, get_object_or_404
from django.forms import inlineformset_factory
from catalog.forms import ProductForm, VersionForm
from catalog.models import Product, Version
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView

from django.urls import reverse_lazy


class ProductListView(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:product_list")


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm

    def get_success_url(self):
        return reverse_lazy('catalog:product_detail', kwargs={"pk": self.object.pk})

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        ProductFormSet = inlineformset_factory(Product, Version, VersionForm, extra=1)
        if self.request.method == 'POST':
            context_data["formset"] = ProductFormSet(self.request.POST, instance=self.object)
        else:
            context_data["formset"] = ProductFormSet(instance=self.object)
        return context_data

    def form_valid(self, form):
        """ Сохраняем изменения продукта и версии  """
        context_data = self.get_context_data()
        formset = context_data["formset"]
        if form.is_valid() and formset.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()

            # проверяем наличие активных версий
            versions = Version.objects.filter(product=self.object, version_active=True)
            if len(versions) > 1:
                form.add_error(None, 'У продукта не может быть более одной активной версии.')
                return super().form_invalid(form)

            return super().form_valid(form)
        else:
            return self.render_to_response(self.get_context_data(form=form, formset=formset))


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy("catalog:product_list")


def contacts(request):
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")
        print(f"{name}\n{phone}\n{message}")
    return render(request, "contacts.html")
