class TV():
    
    def __init__(self,):
        self.energia = False
        self.canal = 3
        self.volume = 5
        self.mudoo = False
        
    
    def ligar_desligar(self):
        self.energia = not self.energia
        if self.energia:
            print('Á TV ESTÁ LIGADA !!!')   
        else:
            print('Á TV ESTÁ DESLIGADA !!!')
            
    
    def avancarcanal(self):
        if self.energia:
            self.canal += 1
            print('CANAL AVANÇADO PARA', self.canal)
        else:
            print('A TV ESTÁ DESLIGADA !!!')
            
    
    def retrocedercanal(self):
        if self.energia:
            self.canal -= 1
            print('CANAL RETROCEDIDO PARA', self.canal)
        else:
            print('A TV ESTÁ DESLIGADA !!!')
            
    
    def mutartv(self):
        if self.energia:
            self.mudoo = not self.mudoo
            if self.mudoo:
                print('FUNÇÃO MUDO ATIVADO !!!')
            else:
                print('FUNÇÃO MUDO DESATIVADO !!!')
        else:
            print('A TV ESTÁ DESLIGADA !!!')
            
    
    def aumentarvolume(self):
        if self.energia:
            if self.volume < 100:
                self.volume += 1
                print('VOLUME AUMENTADO PARA', self.volume)
            else:
                print('A TV ESTÁ NO VOLUME MÁXIMO !!!')
        else:
            print('A TV ESTÁ DESLIGADA !!!')
            
    
    def diminuirvolume(self):
        if self.energia:
            if self.volume > 0:
                self.volume -= 1
                print('VOLUME DIMINUIDO PARA', self.volume)
            else:
                print('A TV ESTÁ NO VOLUME MINÍMO !!!')
        else:
            print('A TV ESTÁ DESLIGADA !!!')
            
            
    def infodatv(self):
        print("----- INFORMAÇÕES DA TV -----:")
        print("ENERGIA:", "TV LIGADA !!!" if self.energia else "TV DESLIGADA !!!")
        print("CANAL:", self.canal)
        print("VOLUME:", self.volume)
        print("FUNÇÃO MUDO:", "ATIVADO" if self.mudoo else "DESATIVADO !!!")
        


#TESTANDO ...
tv = TV()
tv.ligar_desligar()
tv.aumentarvolume()
tv.aumentarvolume()
tv.avancarcanal()
tv.avancarcanal()
tv.retrocedercanal()
tv.mutartv()
tv.mutartv()

#tv.ligar_desligar()
tv.infodatv()
        