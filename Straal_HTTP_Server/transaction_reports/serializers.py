from rest_framework import serializers
from .models import PaymentModel, PayByLink, DirectPayment, Card, PblID, DpID, CardID


class PaymentSerializer(serializers.Serializer):
    customer_id = serializers.IntegerField(required=False)
    date = serializers.DateTimeField(source='created_at')
    type = serializers.CharField()
    payment_mean = serializers.CharField()
    description = serializers.CharField()
    currency = serializers.CharField()
    amount = serializers.IntegerField()
    amount_in_pln = serializers.IntegerField(source='recounting')

    class Meta:
        model = PaymentModel
        fields = ['customer id', 'date', 'type', 'payment_mean', 'description', 'amount', 'currency', 'amount_in_pln']


class PayByLinkSerializer(PaymentSerializer):
    payment_mean = serializers.CharField(source='bank')
    type = 'Pay by link'

    class Meta(PaymentSerializer.Meta):
        model = PayByLink
        fields = '__all__'


class DirectPaymentSerializer(PaymentSerializer):
    payment_mean = serializers.CharField(source='iban')
    type = 'Direct Payment'

    class Meta(PaymentSerializer.Meta):
        model = DirectPayment
        fields = '__all__'


class CardSerializer(PaymentSerializer):
    payment_mean = serializers.CharField(source='HolderDataInLine')
    type = 'Card'

    class Meta(PaymentSerializer.Meta):
        model = Card
        fields = '__all__'


class AddReportPblSerializer(serializers.ModelSerializer):
    class Meta:
            model = PayByLink
            fields = "__all__"


class AddReportDpSerializer(serializers.ModelSerializer):
    class Meta:
            model = DirectPayment
            fields = "__all__"


class AddReportCardSerializer(serializers.ModelSerializer):
    class Meta:
            model = Card
            fields = "__all__"


class AddReportPblIDSerializer(serializers.ModelSerializer):
    class Meta:
            model = PblID
            fields = ('customer_id', 'currency', 'amount', 'description', 'bank')


class AddReportDpIDSerializer(serializers.ModelSerializer):
    class Meta:
            model = DpID
            fields = ('customer_id', 'currency', 'amount', 'description', 'iban')


class AddReportCardIDSerializer(serializers.ModelSerializer):
    class Meta:
            model = CardID
            fields = ('customer_id', 'currency', 'amount', 'description', 'cardholder_name', 'cardholder_surname', 'card_number')