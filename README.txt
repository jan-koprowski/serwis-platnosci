
cd .\STRAAL_Serwis_HTTP\Straal_HTTP_Server
activate your virtualenv
pip install -r requirements.txt

py manage.py runserver

#index
http://127.0.0.1:8000 

#all reports
http://127.0.0.1:8000/api/ 

#adding report, picking type of payment
http://127.0.0.1:8000/report/ 

#adding pay_by_link type report
http://127.0.0.1:8000/report/pbl

#adding direct_payment type report
http://127.0.0.1:8000/report/dp

#adding card type report
http://127.0.0.1:8000/report/card

#adding report with customer_id, picking type of payment
http://127.0.0.1:8000/report/ 

#adding pay_by_link type report with customer_id
http://127.0.0.1:8000/report/pbl_id

#adding direct_payment type report with customer_id
http://127.0.0.1:8000/report/dp_id

#adding card type report with customer_id
http://127.0.0.1:8000/report/card_id