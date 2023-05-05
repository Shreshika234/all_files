

class Calculation:
 def __init__(self):
   pass
 def cal_lcm(self,x,y):
   x=self.x
   y=self.y
   if x>y:
     greater=x
   else :
     greater=y
   while True:
      if((greater%x==0)and(greater%y==0)):
           lcm=greater
           break
      greater+=1
   return lcm
 p=Calculation()
 
 p.cal_lcm(3,7)

