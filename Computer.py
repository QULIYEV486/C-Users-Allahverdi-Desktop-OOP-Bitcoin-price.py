class komputer:
    def __init__(self, marka, model, ram, color, cost, monthly, card_payment):
        self.marka = marka
        self.model = model
        self.ram = ram
        self.color = color
        self.cost = cost
        self.monthly = monthly
        self.card_payment = card_payment

    def comp_info (self):
        print(f'bu {self.marka} - {self.model} cox gozeldi {self.ram} ram gucludur {self.color} renglidi {self.cost} Azndir {self.monthly} ayliq {self.card_payment} kardla odenis!')

    def monthly_payment (self):
        if self.monthly == 12:
            print(f"monthly is {self.cost//12}")
        elif self.monthly == 24:
            print(f"monthly is {self.cost//24}")
        elif self.monthly == 18:
            print(f"monthly is {self.cost//18}") 


    def sale_payment (self):
        if self.card_payment > 500:
            print(f"discounted price {self.cost - 200}")
        elif self.card_payment > 300:
            print(f"discounted price {self.cost - 190}")
        elif self.card_payment > 100:
            print(f"discounted price {self.cost - 170}")    

              

Lenova = komputer("Lenova", "Thinkbook", "4gb", "Grey", 1400, 12, 500) 
Apple = komputer("Apple", "Macbook", "8gb", "Whait", 3500, 24, 300)
Samsung = komputer("Samsung", "Galaxy", "6gb", "Red", 2000, 18, 200)

print(Lenova.monthly)
Lenova.comp_info()
Apple.comp_info()
Samsung.comp_info()

Lenova.monthly_payment()
Apple.monthly_payment()
Samsung.monthly_payment()

Lenova.sale_payment()
Apple.sale_payment()
Samsung.sale_payment()








        
