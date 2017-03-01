# -*- coding: utf-8 -*-
from openprocurement.api.utils import opresource
from openprocurement.api.models import get_now
from openprocurement.tender.openua.views.tender_document import TenderUaDocumentResource
from openprocurement.tender.openua.utils import calculate_business_date
from openprocurement.tender.twostage.models import TENDERING_EXTRA_PERIOD


@opresource(name='Tender Two Stage Documents',
            collection_path='/tenders/{tender_id}/documents',
            path='/tenders/{tender_id}/documents/{document_id}',
            procurementMethodType='aboveThresholdTS',
            description="Tender Two Stage related binary files (PDFs, etc.)")
class TenderTSDocumentResource(TenderUaDocumentResource):

    def validate_update_tender(self, operation):
        if self.request.authenticated_role != 'auction' and self.request.validated['tender_status'] != 'active.tendering' or \
           self.request.authenticated_role == 'auction' and self.request.validated['tender_status'] not in ['active.auction', 'active.qualification']:
            self.request.errors.add('body', 'data', 'Can\'t {} document in current ({}) tender status'.format(operation, self.request.validated['tender_status']))
            self.request.errors.status = 403
            return
        if self.request.validated['tender_status'] == 'active.tendering' and calculate_business_date(get_now(), TENDERING_EXTRA_PERIOD, self.request.validated['tender']) > self.request.validated['tender'].tenderPeriod.endDate:
            self.request.errors.add('body', 'data', 'tenderPeriod should be extended by {0.days} days'.format(TENDERING_EXTRA_PERIOD))
            self.request.errors.status = 403
            return
        return True
