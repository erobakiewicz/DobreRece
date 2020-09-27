from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Sum
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, FormView, ListView

from charity.constants import Institutions
from charity.forms import DonationForm
from charity.models import Category, Donation, Institution


class LandingPageView(ListView):
    paginate_by = 2
    model = Institution

    def get_context_data(self, *args, **kwargs):
        ctx = super().get_context_data(*args, **kwargs)
        ctx['foundations'] = Institution.objects.filter(type=Institutions.Fundacja)
        ctx['ngos'] = Institution.objects.filter(type=Institutions.Organizacja_pozarządowa)
        ctx['local_collections'] = Institution.objects.filter(type=Institutions.Zbiórka_lokalna)
        ctx['donation_counter'] = Donation.objects.aggregate(Sum("quantity"))['quantity__sum']
        if ctx['donation_counter'] is None:
            ctx['donation_counter'] = 0
        ctx['institution_counter'] = Institution.objects.filter(donation__quantity__gte=1).distinct().count()
        return ctx


class DonationFormView(LoginRequiredMixin, FormView):
    form_class = DonationForm
    template_name = 'form.html'
    success_url = reverse_lazy('form_confirmation')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        raise Exception
        return super().form_invalid(form)


class FormConfirmationView(TemplateView):
    template_name = "form-confirmation.html"


class CategoryCreateView(CreateView):
    model = Category
    fields = ['name']
    template_name = 'category_form.html'
    success_url = reverse_lazy("/")
