from django.db.models import Sum
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView

from charity.models import Category, Donation, Institution


class LandingPageView(TemplateView):

    def get_context_data(self, *args, **kwargs):
        ctx = super().get_context_data(*args, **kwargs)
        ctx['foundations'] = Institution.objects.filter(type=10)
        ctx['ngos'] = Institution.objects.filter(type=20)
        ctx['local_collections'] = Institution.objects.filter(type=30)
        ctx['donation_counter'] = Donation.objects.aggregate(Sum("quantity"))['quantity__sum']
        if ctx['donation_counter'] is None:
            ctx['donation_counter'] = 0
        ctx['institution_counter'] = Institution.objects.filter(donation__quantity__gte=1).distinct().count()
        return ctx





class CategoryCreateView(CreateView):
    model = Category
    fields = ['name']
    template_name = 'category_form.html'
    success_url = reverse_lazy("/")
