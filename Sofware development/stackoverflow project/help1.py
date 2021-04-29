string='here is what you asked for';
print(string.split());
print(list(string));

import random

class cards:

    @staticmethod
    def show(card,suits):
        print(card+' of '+suits);


card=random.randint(2,14);
suits=random.randint(15,18);

call=cards(); #instance variable

if card ==11 and suits ==15:
    call.show('Jack','Clubs');
elif card==12 and suits==15:
    call.show('Queen','Clubs');


#--------------
act,au,ag,pd,pt='act','gold','silver','paladium','platinum';
spot_price={au:1918.40,ag:24.23,pt:912.45,pd:2353.53}; #python dictionary definition
portfolio={'Act':100000,au:0,ag:0,pd:0,pt:0};#python dictionary defintion

def purchase(portfolio,metal,amt):

    price_au=spot_price[au];
    price_ag=spot_price[ag];
    price_pt=spot_price[pt];
    price_pd=spot_price[pd];

    account_total=portfolio['Act'];
    for key,value in portfolio.items():
        if key ==metal:
            portfolio[metal]=amt;
        elif key=='Act':
            portfolio['Act']=account_total-((price_ag*amt)+(price_au*amt)+(price_pd*amt)+(price_pt*amt));
    return portfolio;
print(purchase(portfolio,'au',2))

import re

string='03/10/2020 15:00 A.F.C. Wimbledon v Accrington Stanley'; #python string definition
pattern=re.compile(r'');
matches=pattern.finditer(string); #search for pattern in string
for match in matches:
    print(match);

#---------
x=int(input('Enter a number between 50 and 100')); #collect user input

if x <50:
    print('That is below 50');
elif x >50 and x<100:
    print('That is between 50 and 100');
else:
    print('that is greater than 100');