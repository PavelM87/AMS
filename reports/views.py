from django.db import transaction, IntegrityError
from django.template.loader import render_to_string
from weasyprint import HTML, CSS
import tempfile

from django.http import HttpResponse
from django.template.loader import get_template
from django.shortcuts import render, reverse, get_object_or_404, redirect
from django.views import generic
from django.forms import modelformset_factory

from crm import settings
from .forms import ReportModelForm, AMSEquipmentForm
from .models import Report, AMSEquipment
from users.mixins import SuperuserAndLoginRequiredMixin, ModeratorAndLoginRequiredMixin


######################################
# def fetch_pdf_resources(uri, rel):
#     if uri.find(settings.MEDIA_URL) != -1:
#         path = os.path.join(settings.MEDIA_ROOT, uri.replace(settings.MEDIA_URL, ''))
#     elif uri.find(settings.STATIC_URL) != -1:
#         path = os.path.join(settings.STATIC_ROOT, uri.replace(settings.STATIC_URL, ''))
#     else:
#         path = None
#     print(path)
#     return path
#
#
# def report_pdf(request, *args, **kwargs):
#     pk = kwargs.get('pk')
#     report = get_object_or_404(Report, pk=pk)
#     template_path = 'reports/pdf.html'
#     context = {'report': report}
#     # Create a Django response object, and specify content_type as pdf
#     response = HttpResponse(content_type='application/pdf')
#     # if download:
#     # response['Content-Disposition'] = 'attachment; filename="report.pdf"'
#     # if display:
#     response['Content-Disposition'] = 'filename="report.pdf"'
#     # find the template and render it.
#     template = get_template(template_path)
#     html = template.render(context)
#
#     # create a pdf
#     pisa_status = pisa.CreatePDF(
#         html, dest=response, link_callback=fetch_pdf_resources, encoding='utf-8')
#     # if error then show some funy view
#     if pisa_status.err:
#         return HttpResponse('We had some errors <pre>' + html + '</pre>')
#     print()
#     print(pisa_status)
#     print()
#     return response


######################################

def generate_pdf(request, *args, **kwargs):
    """Создание pdf."""
    # Данные модели
    pk = kwargs.get('pk')
    report = get_object_or_404(Report, pk=pk)

    # Обработка шаблона
    html_string = render_to_string('reports/pdf.html', {'report': report})
    html = HTML(string=html_string, base_url=request.build_absolute_uri())
    result = html.write_pdf()

    # Создание http ответа
    pdf = html.write_pdf(stylesheets=[CSS(settings.STATIC_ROOT + '/css/pdf_report.css')])
    response = HttpResponse(pdf, content_type='application/pdf;')
    response['Content-Disposition'] = 'inline; filename=report.pdf'
    response['Content-Transfer-Encoding'] = 'binary'
    with tempfile.NamedTemporaryFile(delete=True) as output:
        output.write(result)
        output.flush()
        output = open(output.name, 'rb')
        response.write(output.read())
    return response


class ReportListView(generic.ListView):
    template_name = "reports/reports_list.html"
    queryset = Report.objects.all()
    context_object_name = "reports_objects"


class ReportDetailView(ModeratorAndLoginRequiredMixin, generic.DetailView):
    template_name = "reports/report_detail.html"
    queryset = Report.objects.all()
    context_object_name = "report"


class ReportCreateView(generic.CreateView):
    template_name = "reports/report_create.html"
    form_class = ReportModelForm

    def get_success_url(self):
        return reverse("reports:reports-list")


def create(request):
    context = {}
    EquipmentFormset = modelformset_factory(AMSEquipment, form=AMSEquipmentForm)
    form = ReportModelForm(request.POST or None)
    formset = EquipmentFormset(request.POST or None, queryset=AMSEquipment.objects.none(), prefix='equipment')
    if request.method == "POST":
        if form.is_valid() and formset.is_valid():
            try:
                with transaction.atomic():
                    report = form.save(commit=False)
                    report.save()

                    for equipment in formset:
                        data = equipment.save(commit=False)
                        data.report = report
                        data.save()
            except IntegrityError:
                print("Error Encountered")

            return redirect("reports:reports-list")

    context['formset'] = formset
    context['form'] = form
    return render(request, 'reports/report_create.html', context)


class ReportUpdateView(ModeratorAndLoginRequiredMixin, generic.UpdateView):
    template_name = "reports/report_update.html"
    queryset = Report.objects.all()
    form_class = ReportModelForm

    def get_success_url(self):
        return reverse("reports:reports-list")


class ReportDeleteView(ModeratorAndLoginRequiredMixin, generic.DeleteView):
    template_name = "reports/report_delete.html"
    queryset = Report.objects.all()

    def get_success_url(self):
        return reverse("reports:reports-list")
