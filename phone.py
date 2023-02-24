class phone:
    def __init__(self, marka, model, ram, memory, year, color, price, ayliq, products, card_payment):
        self.marka = marka
        self.model = model
        self.ram = ram
        self.memory = memory
        self.year = year
        self.color = color
        self.price = price
        self.ayliq = ayliq
        self.products = products
        self.card_payment = card_payment

    def phone_info(self):
        print(f"markasi {self.marka} - {self.model, } cox gozel modelir {self.ram}lıq rami var {self.memory}lıq  yaddasi var {self.year}ci ilde cixmis {self.color} rengleri var qiymeti {self.price} Azndir {self.ayliq} ay faizsiz ödeniş var {self.products} ededdir  {self.card_payment}larindan ödəniş olanda endirim olunur!")


    def phone_year(self):
        if self.year == 2019:
            print(f"old model")
        elif self.year == 2020:
            print(f"average model") 
        elif self.year == 2022:      
            print(f"new model")    


    def ayliq_odenis(self):
        if self.ayliq == 12:
            print(f"Ayliq ödeniş {self.price // 12} Azn")
        elif self.ayliq == 24:
            print(f"Ayliq ödeniş {self.price // 24} Azn")    
        elif self.ayliq == 18:
            print(f"Ayliq ödeniş {self.price // 18} Azn")  

    def mehsul_sayi(self):
        if self.products > 10:
            self.products = 15
            print(f"{self.products} eded bol mehsul")
        elif self.products < 15:
            self.products = 10
            print(f"{self.products} eded mehdud sayda")
        elif self.products == 10:
            self.products = 10  
            print(f"{self.products} eded mehdul qurtarir")    



    def Endirimli_payment(self):
        if self.card_payment  == "Birbank_card":
            print(f"Endirimli {self.price - 100} Azndir")
        elif self.card_payment == "Unibank_card":
            print(f"Endirimli {self.price - 500} Azndir")
        elif self.card_payment == "Xalqbank_Card":
            print(f"Endirimli {self.price - 300} Azndir")   





Samsung = phone("Samsung", "A73", "8gb", "256gb", 2019, "ağ", 500, 12, 15, "Birbank_card") 
Apple = phone("Apple", "14pro", "8gb", "512gb", 2022, "bənövşəyi", 3200, 24, 10, "Unibank_card")
Xiomi = phone("Xiomi", "note 11", "6gb", "256gb", 2020, "qara", 1300, 18, 10, "Xalqbank_Card")



print(Samsung.model)
print(Apple.model)
print(Xiomi.model)

print(Samsung.year)
print(Apple.price)
print(Xiomi.price)

Samsung.phone_info()
Apple.phone_info()
Xiomi.phone_info()

Samsung.phone_year()
Apple.phone_year()
Xiomi.phone_year()

Samsung.ayliq_odenis()
Apple.ayliq_odenis()
Xiomi.ayliq_odenis()


Samsung.mehsul_sayi()
Apple.mehsul_sayi()
Xiomi.mehsul_sayi()

Samsung.Endirimli_payment()
Apple.Endirimli_payment()
Xiomi.Endirimli_payment()







         