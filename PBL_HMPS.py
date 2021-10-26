# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 10:17:45 2021

@author: 91952
"""


from twilio.rest import Client 

import random 

otp_number=random.randint(100000,999999)  

#Authentification of Twilio 

auth_sid="AC5581ab2a1285607920b71fb064246c13" 

auth_token="44fe383cfdbce7cea156cda96f7249e2" 

otp_client=Client(auth_sid,auth_token) 

#Message that will OTP receiver get 

otp_message = otp_client.messages.create( 

     body="Your OTP number is "+str(otp_number),
 
     from_="+15597850327", 

     to="+919373243606",
     )

print('OTP number is '+str(otp_number))