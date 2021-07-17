from django.db import models
import requests


class PaymentModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    CURRENCIES = (
        ('EUR', ('EUR')),
        ('USD', ('USD')),
        ('GBP', ('GBP')),
        ('PLN', ('PLN')))
    currency = models.CharField(max_length=5, choices=CURRENCIES, default="EUR")
    amount = models.PositiveIntegerField()  # najnizszy nominal
    description = models.TextField(max_length=30)


    #przeliczanie na PLN, do osobnego pliku
    @property
    def recounting(self):
        if self.currency == 'PLN':
            return self.amount
        else:
            url = f"http://api.nbp.pl/api/exchangerates/rates/a/{self.currency}/last"
            r = requests.get(url)
            my_json = r.json()
            currency_rate = my_json.get('rates')[0].get('mid')
            amount_in_original_curr = float(self.amount)
            return currency_rate * amount_in_original_curr


class PayByLink(PaymentModel):
    bank = models.CharField(max_length=20)


class DirectPayment(PaymentModel):
    iban = models.CharField(max_length=40)


class Card(PaymentModel):
    cardholder_name = models.CharField(max_length=20)
    cardholder_surname = models.CharField(max_length=30)
    card_number = models.CharField(max_length=30)

    #maskowanie numeru karty, do osobnego pliku
    def masking_card_number(self, card_num):
        card_number = str(card_num)
        first4 = card_number[:4]
        last4 = card_number[-4:]
        return first4 + '*' * (len(card_number) - 8) + last4

    #zlozenie danych platnika do jednego stringa
    def holder_data_in_line(self):
        return str(self.cardholder_name) + ' ' + str(self.cardholder_surname) + ' ' + self.masking_card_number(self.card_number)


class PblID(PayByLink):
    customer_id = models.PositiveIntegerField(blank='True', unique=True)


class DpID(DirectPayment):
    customer_id = models.PositiveIntegerField(blank='True')


class CardID(Card):
    customer_id = models.PositiveIntegerField(blank='True')

