# A converter for international currency exchange.

USD_TO_GBP = 0.76
USD_TO_EUR = 0.86
USD_TO_JPY = 114.08
USD_TO_INR = 63.64

GBP_sign = '\u00A3'
EUR_sign = '\u20AC'
JPY_sign = '\u00A5'
INR_sign = '\u20B9'

dollars = 1000 # The number of dollars to convert

pounds = dollars * USD_TO_GBP
euros = dollars * USD_TO_EUR
yen = dollars * USD_TO_JPY
rupees = dollars * USD_TO_INR

print('Today, $' + str(dollars))
print('convert to ' + GBP_sign + str(pounds))
print('convert to ' + EUR_sign + str(euros))
print('convert to ' + JPY_sign + str(yen))
print('convert to ' + INR_sign + str(rupees))