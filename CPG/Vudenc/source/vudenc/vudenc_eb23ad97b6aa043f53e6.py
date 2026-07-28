from django.apps import apps
from clickgestion.transactions.forms import TransactionEditForm, TransactionPayForm
from clickgestion.transactions.models import BaseConcept, Transaction
from django.shortcuts import get_object_or_404, render, redirect, reverse
from django.utils.translation import gettext, gettext_lazy
from clickgestion.transactions.filters import ConceptFilter, TransactionFilter
from clickgestion.core.utilities import invalid_permission_redirect
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from pure_pagination.mixins import PaginationMixin
from django.http import HttpResponse, QueryDict
from django.conf import settings
from django.utils import timezone
from django_xhtml2pdf.utils import generate_pdf
@login_required()...
extra_context = {}
concept, concept_form = get_concept_and_form_from_kwargs(**kwargs)
extra_context['concept'] = concept
transaction = concept.transaction
if transaction.closed:
return redirect('message', message=gettext('Transaction Closed'))
extra_context['transaction'] = transaction
extra_context['header'] = gettext('Delete {}?'.format(concept.concept_type))
extra_context['message'] = concept.description_short
extra_context['next'] = request.META['HTTP_REFERER']
if request.method == 'POST':
default_next = reverse('transaction_detail', kwargs={'transaction_code':
    concept.transaction.code})
return render(request, 'core/delete.html', extra_context)
concept.delete()
next_page = request.POST.get('next', default_next)
return redirect(next_page)
