#Employee should have the following attributes:
#StaffID, LastName, FirstName, RegHours, HourlyRate,
#OTMultiple, TaxCredit, StandardBand,


class Employee:
    def __init__(self,id,lname,fname,hours,rate,otm,tc,band):
        self.__id= id
        self.__fname= fname
        self.__lname= lname
        self.__hours= hours
        self.__rate= rate
        self.__otm= otm
        self.__tc= tc
        self.band= band

    

        





