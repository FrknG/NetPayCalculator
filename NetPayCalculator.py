#Employee should have the following attributes:
#StaffID, LastName, FirstName, RegHours, HourlyRate,
#OTMultiple, TaxCredit, StandardBand,



#https://github.com/FrknG/NetPayCalculator

import unittest

class Employee:
    def __init__(self,id,lname,fname,hours,rate,otm,tc,band) :
        self.__id= id
        self.__fname= fname
        self.__lname= lname
        self.__hours= hours
        self.__rate= rate
        self.__otm= otm
        self.__tc= tc
        self.__band= band       

    def computePayment(self,hworked,date) : 
       payment_info = {}
       overtime_r = (self.__rate * self.__otm) 
       if(hworked <= self.__hours):
            if(hworked <= 0):
                hworked = 0
            overtime_h = 0
            overtime_p = 0            
            reg_hworked = hworked
            pay = hworked * self.__rate
            reg_p = pay
            gross_p = pay
       elif(hworked > self.__hours):
            overtime_h = hworked - self.__hours            
            overtime_p = overtime_h * overtime_r
            reg_hworked = self.__hours
            reg_p = self.__hours * self.__rate
            gross_p = reg_p + overtime_p
       
       
       tax_dic = self.calcTax(gross_p)       
       net_de = self.calcDeduc(tax_dic,gross_p)
       net_pay = gross_p - net_de['Net Deductions']     
       

       keys =['Name','Date','Regular Hours Worked','Overtime Hours Worked','Regular Rate',
              'Overtime Rate','Regular Pay','Overtime Pay','Gross Pay']
       values=[self.__fname + self.__lname, date, reg_hworked, overtime_h, self.__rate,
               overtime_r, reg_p, overtime_p, gross_p]
       for i in range(len(keys)):
           payment_info[keys[i]] = values[i]
       payment_info.update(tax_dic)
       payment_info.update(net_de)
       payment_info['Net Pay'] = net_pay

       with open("Pay Information.txt", 'w') as f:
           for key, value in payment_info.items():
               f.write('%s:%s\n' %(key, value))
           f.write('\n')
       return payment_info 
   
         
    def calcTax(self,gross_p):
        tax_dic = {}
        s_ratepay = self.__band
        if(gross_p <= s_ratepay):
            s_ratepay = gross_p
            h_ratepay = 0
        else:
            s_ratepay = self.__band
            h_ratepay = gross_p - s_ratepay  
        s_tax =  s_ratepay * 0.2        
        h_tax =  h_ratepay * 0.4        
        t_tax = s_tax + h_tax       
        keys = ['Standart Rate Pay','Higher Rate Pay','Standart Tax','Higher Tax','Total Tax']
        values = [s_ratepay,h_ratepay,s_tax,h_tax,t_tax]
        for i in range(len(keys)):
            tax_dic[keys[i]] = values[i]
        return tax_dic
        
        
    def calcDeduc(self, tax,gross_p):
        prsi = gross_p * 0.04
        if(tax['Total Tax']<=self.__tc):
            net_tax = tax['Total Tax']
        else:
            net_tax= tax['Total Tax'] - self.__tc        
        deduc = prsi + net_tax
        keys = ['Tax Credit','Net Tax', 'PRSI','Net Deductions']
        values = self.__tc , round(net_tax, 2),prsi,round(deduc, 2)
        for i in range(len(keys)):
            tax[keys[i]] = values[i]
        return tax
        

class testEmployee(unittest.TestCase):
   def testNetLessEqualGross(self):
    e=Employee(12345,'Green','Joe ',37,16,1.5,72,710)
    pi=e.computePayment(1,'31/10/2021')
    self.assertLessEqual(pi['Net Pay'], pi['Gross Pay'])
   def testOvertime(self):
    e=Employee(12345,'Green','Joe ',37,16,1.5,72,710)
    pi=e.computePayment(10,'31/10/2021')
    self.assertGreaterEqual(pi['Overtime Hours Worked'], 0)
    self.assertGreaterEqual(pi['Overtime Pay'], 0)
   def testRegularHours(self):
    e=Employee(12345,'Green','Joe ',37,16,1.5,72,710)
    pi=e.computePayment(15,'31/10/2021')
    self.assertLessEqual(pi['Regular Hours Worked'], 15 )
   def testHigherTax(self):
    e=Employee(12345,'Green','Joe ',37,16,1.5,72,710)
    pi=e.computePayment(15,'31/10/2021')
    self.assertGreaterEqual(pi['Higher Tax'], 0 )
   def testNetPay(self):
    e=Employee(12345,'Green','Joe ',37,16,1.5,72,710)
    pi=e.computePayment(-1,'31/10/2021')
    self.assertGreaterEqual(pi['Net Pay'], 0)
    
   

unittest.main(argv=['ignored'],exit=False)
jg= Employee(12345,'Green','Joe ',37,16,1.5,72,710)
print(jg.computePayment(42,'31/10/2021'))




