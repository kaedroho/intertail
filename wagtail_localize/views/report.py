from django.utils.translation import gettext as _, gettext_lazy
import django_filters
from django_filters.constants import EMPTY_VALUES
from wagtail.admin.filters import DateRangePickerWidget, WagtailFilterSet
from wagtail.admin.views.reports import ReportView

from wagtail_localize.models import Translation


class SearchPageTitleFilter(django_filters.CharFilter):
    def filter(self, qs, value):
        if value in EMPTY_VALUES:
            return qs

        return qs.filter(source__object_repr__icontains=value)


class TranslationsReportFilterSet(WagtailFilterSet):
    page = SearchPageTitleFilter(label=gettext_lazy("Source title"))
    # first_started_at = django_filters.DateFromToRangeFilter(label=gettext_lazy("Started at"), widget=DateRangePickerWidget)

    class Meta:
        model = Translation
        fields = ['page', 'source__locale', 'target_locale']


class TranslationsReportView(ReportView):
    template_name = 'wagtail_localize/admin/translations_report.html'
    title = gettext_lazy('Translations')
    header_icon = ''

    filterset_class = TranslationsReportFilterSet

    def get_queryset(self):
        return Translation.objects.all()
