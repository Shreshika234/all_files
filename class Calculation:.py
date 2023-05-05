class Calculation:
    def cal_lcm(self,x,y):
        self.x=x
        self.y=y
        if x>y:
            greater=x
        else:
            greater=y
        while True:
            if((greater%x==0)and(greater%y==0)):
                lcm=greater
                break
            greater+=1
        return lcm
p=Calculation()
n1=int(input("enter first num : "))
n2=int(input("enter second num : "))
print(p.cal_lcm(n1,n2))