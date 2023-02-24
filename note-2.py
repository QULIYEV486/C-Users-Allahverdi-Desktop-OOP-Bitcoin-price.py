import sys
class Home:
    def __init__(self, model, otaq, mertebe, qiymet, card_payment, monthly):
        self.model = model
        self.otaq = otaq
        self.mertebe = mertebe
        self.qiymet = qiymet 
        self.card_payment = card_payment 
        self.monthly = monthly


    def home_info (self):
        print(f" gozel temirli {self.model} modelde - {self.otaq} otaqli {self.mertebe}cü mertebede yerləşir {self.qiymet} Azndir {self.card_payment} Azn kardla ödenişdə endirim {self.monthly} faizsiz ödeniş")

    def Ayliq_Ödeniş (self):
        if self.monthly == 24:
            print(f"Ayliq {self.qiymet // 24} Azn")  
        elif self.monthly == 12:
            print(f"Ayliq {self.qiymet // 12} Azn")
        elif self.monthly == 36:
            print(f"Ayliq {self.qiymet // 36} Azn")


    def kardla_ödeniş (self):
        if self.card_payment == "Birbank":
            print(f"Endirim {self.qiymet - 5000 } Azn")  
        elif self.card_payment == "Unibank":
            print(f"Endirim {self.qiymet - 8000} Azn")
        elif self.card_payment == "Dostbank":
            print(f"Endirim {self.qiymet - 4000} Azn")         





İcəri_Şəhər = Home("Avropa style", 5, 5, 150000, "Birbank", 24)
Gənclik = Home("Yapon style", 4, 17, 200000, "Unibank", 12)
Nəsimi =  Home("Amerika style", 8, 15, 100000, "Dostbank", 36)


İcəri_Şəhər.Ayliq_Ödeniş()
Gənclik.Ayliq_Ödeniş()
Nəsimi.Ayliq_Ödeniş()

İcəri_Şəhər.kardla_ödeniş()
Gənclik.kardla_ödeniş()
Nəsimi.kardla_ödeniş()

       



