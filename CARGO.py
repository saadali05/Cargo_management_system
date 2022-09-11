class cargo:
    def __init__(self,Sender_Name,Reciver_Name,parcel_type,parcel_weight,send_country,send_city,recive_country,recive_city):
        self.Sender_Name = Sender_Name
        self.Reciver_Name = Reciver_Name
        self.parcel_type = parcel_type 
        self.parcel_weight = parcel_weight
        self.send_country = send_country
        self.send_city = send_city 
        self.recive_city = recive_city 
        self.recive_country = recive_country

class final(cargo):        
    def CustomerD(self):
        print('Sender name: ',self.Sender_Name)
        print('Sender country: ',self.send_country)
        print('Sender city: ',self.send_city)
        print('Reciver name: ',self.Reciver_Name)
        print('Reciver city: ',self.recive_country)
        print('Reciver city: ',self.recive_city)
        
    def parcel(self):
        if self.parcel_weight <= 15 and self.parcel_type == 'Solid' or self.parcel_type == 'solid':
            print('Your parcel weight is: ',self.parcel_weight,'KG')
            print('Your parcel type is: ',self.parcel_type)
            base = datetime.datetime.today()
            print('Sender handed over parcel on ',base.strftime("%A, %d-%B-%Y,  , time: %I:%M:%S %p"))
            for x in range(0, 5,-5):
                print('Reciver will get parcel till ',base + datetime.timedelta(days=x))
                
def END(TCS):
    TCS.CustomerD()
    TCS.parcel()
    

Sender_Name = input('Enter Sender Name: ')
Reciver_Name = input('Enter Reciver Name: ')
parcel_type = input('Enter Parcel Type: ')
parcel_weight = eval(input('Enter Parcel Weight in "KG": '))
send_country = input('Enter Sender_country: ')
send_city = input('Enter Sender_city: ')
recive_country = input('Enter Recive_country: ')
recive_city = input('Enter Reciver_city: ')

tcs = final(Sender_Name,Reciver_Name,parcel_type,parcel_weight,send_country,send_city,recive_country,recive_city)
print(' ')
END(tcs)
