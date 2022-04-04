#Employee should have the following attributes:
#StaffID, LastName, FirstName, RegHours, HourlyRate,
#OTMultiple, TaxCredit, StandardBand,


class Employee:
    def __init__(self,id,lname,fname,hours,rate,otm,tc,band) :
        self.__id= id
        self.__fname= fname
        self.__lname= lname
        self.__hours= hours
        self.__rate= rate
        self.__otm= otm
        self.__tc= tc
        self.band= band

    def computePayment(self,hworked,date) : 
       if(hworked <= self.__hours):          
            overtime_h = 0
            overtime_p = 0
            reg_hworked = hworked
            pay = hworked * self.__rate
            reg_p = pay
            gross_p = pay
       elif(hworked > self.__hours):
            overtime_h = hworked - self.__hours
            overtime_r = (self.__rate * 1.5) 
            overtime_p = overtime_h * overtime_r
            reg_hworked = self.__hours
            reg_p = self.__hours * self.__rate
            gross_p = reg_p + overtime_p


       print (self.__fname,date,reg_hworked,overtime_h,self.__rate,overtime_r,reg_p,overtime_p,gross_p)   

     

jg= Employee(12345,'Green','Joe',37,16,1.5,72,710)
jg.computePayment(42,'31/10/2021')



