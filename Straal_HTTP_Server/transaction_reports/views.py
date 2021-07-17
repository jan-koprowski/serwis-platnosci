from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, JsonResponse, Http404
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import PayByLink, DirectPayment, Card, PblID, DpID, CardID
from .serializers import PayByLinkSerializer, DirectPaymentSerializer, CardSerializer, AddReportPblSerializer, AddReportDpSerializer, AddReportCardSerializer, AddReportPblIDSerializer, AddReportDpIDSerializer, AddReportCardIDSerializer




class MultipleModelsView(APIView):

    def get(self, request):
        pbl_obj = PayByLink.objects.all()
        pbl_obj_ser = PayByLinkSerializer(pbl_obj, many=True)
        dp_obj = DirectPayment.objects.all()
        dp_obj_ser = DirectPaymentSerializer(dp_obj, many=True)
        card_obj = Card.objects.all()
        card_obj_ser = CardSerializer(card_obj, many=True)
        pbl_ID_obj = PblID.objects.all()
        pbl_ID_obj_ser = PayByLinkSerializer(pbl_ID_obj, many=True)
        dp_ID_obj = DpID.objects.all()
        dp_ID_obj_ser = DirectPaymentSerializer(dp_ID_obj, many=True)
        card_ID_obj = CardID.objects.all()
        card__ID_obj_ser = CardSerializer(card_ID_obj, many=True)
        sum_of_obj = pbl_obj_ser.data + dp_obj_ser.data + card_obj_ser.data + pbl_ID_obj_ser.data + dp_ID_obj_ser.data + card__ID_obj_ser.data
        return Response(sum_of_obj)


class AddReportPBL(generics.CreateAPIView):
    queryset = PayByLink.objects.all()
    serializer_class = AddReportPblSerializer

    def create(self, request, *args, **kwargs):
        response = super(AddReportPBL, self).create(request, *args, **kwargs)
        return HttpResponseRedirect(redirect_to='../')


class AddReportDP(generics.CreateAPIView):
    queryset = DirectPayment.objects.all()
    serializer_class = AddReportDpSerializer

    def create(self, request, *args, **kwargs):
        response = super(AddReportDP, self).create(request, *args, **kwargs)
        return HttpResponseRedirect(redirect_to='../')


class AddReportCard(generics.CreateAPIView):
    queryset = Card.objects.all()
    serializer_class = AddReportCardSerializer

    def create(self, request, *args, **kwargs):
        response = super(AddReportCard, self).create(request, *args, **kwargs)
        return HttpResponseRedirect(redirect_to='../')


class AddReportPblID(generics.CreateAPIView):
    queryset = PblID.objects.all()
    serializer_class = AddReportPblIDSerializer

    def create(self, request, *args, **kwargs):
        response = super(AddReportPblID, self).create(request, *args, **kwargs)
        return HttpResponseRedirect(redirect_to='../')


class AddReportDpID(generics.CreateAPIView):
    queryset = DpID.objects.all()
    serializer_class = AddReportDpIDSerializer

    def create(self, request, *args, **kwargs):
        response = super(AddReportDpID, self).create(request, *args, **kwargs)
        return HttpResponseRedirect(redirect_to='../')


class AddReportCardID(generics.CreateAPIView):
    queryset = CardID.objects.all()
    serializer_class = AddReportCardIDSerializer

    def create(self, request, *args, **kwargs):
        response = super(AddReportCardID, self).create(request, *args, **kwargs)
        return HttpResponseRedirect(redirect_to='../')


def add_reports(request):
    return render(request, 'transaction_reports/add_reports.html')


def add_reports_ID(request):
    return render(request, 'transaction_reports/add_reports_ID.html')


def home(request):
    return render(request, 'transaction_reports/home.html')