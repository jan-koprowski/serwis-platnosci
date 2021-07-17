from django.urls import path
from .views import MultipleModelsView, AddReportPBL, AddReportDP, AddReportCard, add_reports, home, add_reports_ID, AddReportPblID, AddReportDpID, AddReportCardID

urlpatterns = [
    path('', home, name='home'),
    path('api/', MultipleModelsView.as_view(), name='allReports'),
    path('report/', add_reports, name='add_reports'),
    path('customer_report/', add_reports_ID, name='add_reports_ID'),
    path('report/pbl', AddReportPBL.as_view(), name='AddReportPBL'),
    path('report/dp', AddReportDP.as_view(), name='AddReportDP'),
    path('report/card', AddReportCard.as_view(), name='AddReportCard'),
    path('report/pbl_id', AddReportPblID.as_view(), name='AddReportPBL_ID'),
    path('report/dp_id', AddReportDpID.as_view(), name='AddReportDP_ID'),
    path('report/card_id', AddReportCardID.as_view(), name='AddReportCard_ID')
]