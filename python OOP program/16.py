class student:

    def __init__(self,name,phy,maths,chemistry):
        self.name=name
        self.phy=phy
        self.maths=maths
        self.chemistry=chemistry

    def avg(self):
        avarage=self.phy+self.maths+self.chemistry/3
        print("hi",self.name, "your avg is",avarage)

s1=student("parthiv",23,56,89)
s1.avg()
        