from datetime import date, timedelta , datetime
from .forms import PriceSearchForm

class getDateService():
    def getCurrentDateView(self):
        datetime_today = date.today()
        date_today = str(datetime_today) 
        date_10daysago = str(datetime_today - timedelta(days=10)) 

        date_from = date_10daysago 
        date_to = date_today

        return date_from,date_to

class getDefaultData():
    def makeDefaultApiView(self, date_from, date_to):
        PriceFormSearch = initialData(date_from, date_to) 
        search_form_default= PriceFormSearch 

        return search_form_default

class getUserInputDateRange():
    def userFormInputView(self, date_from, date_to, date_today):
        if date_to > date_today: 
            date_to = date_today
        PriceFormSearch = initialData(date_from, date_to) 
        search_form_current= PriceFormSearch  

        return  search_form_current
class outOfRange():
    def ooR(self, date_from, date_to, range_error):
        from_date= datetime.strptime(date_from, '%Y-%m-%d').date()
        to_date= datetime.strptime(date_to, '%Y-%m-%d').date()

        if from_date < (to_date - timedelta(days=90)):  
            range_error= 'No more than 3 months data can be displayed'

        PriceFormSearch = initialData(date_from, date_to)  
        search_form_values= PriceFormSearch 

        return date_from, date_to, range_error, search_form_values

def initialData(date_from, date_to):  
    initial_data={'date_from':date_from,   
                    'date_to':date_to,
                }
    PriceForm = PriceSearchForm(initial=initial_data) 

    return PriceForm