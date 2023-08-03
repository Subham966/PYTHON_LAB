class bank:
    bank_name = "SBI"
    roi = 12.25
    
    @staticmethod
    def simple_interest(prin,n):
        si = (prin*n*bank.roi)/100
        print("Simple interest is: ",si)
        
prin = int(input("Enter the principal amount: "))
n = int(input("Enter the No of year: "))
result = bank.simple_interest(prin,n)
