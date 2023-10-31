from django.shortcuts import render
from payment_gateway.settings import RAZOR_KEY_ID,RAZOR_KEY_SECRET
import razorpay
from fintech.models import PaymentRecord

# Create your views here.
def testing( request):
    if request.method =='GET':
        return render(request, 'base.html')
    else:
        pass






# authorize razorpay client with API Keys.
razorpay_client = razorpay.Client(
    auth=(RAZOR_KEY_ID, RAZOR_KEY_SECRET))


def payment(request):
  
  
   

    DATA = {
        "amount": 10000, #Razorpay accepts in paise Indian currency. 
        "currency": "INR",
       
        "payment_capture":1,
    }

    orders= razorpay_client.order.create(data=DATA)
    order_id=orders['id']
    payment_status = orders['status']
    # print(orders)
    # print(order_id)
    # print(payment_status)


    context={
        'api_key':RAZOR_KEY_ID,
        'order_id':order_id,
        'amount':100,
    }

    records=   PaymentRecord(
            order_id=order_id,
            status= payment_status,
            amount= DATA["amount"],
            currency= DATA["currency"],
          


    )
    records.save()

    return render(request,'base.html',context)


