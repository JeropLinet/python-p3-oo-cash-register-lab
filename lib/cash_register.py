#!/usr/bin/env python3

class CashRegister:
  def __init__(self,discount=0):
   self.discount=discount
   self.total=0
   self.items=[]
   self.last_item=0
  
  def add_item(self,title,price,quantity=1):
    total_cost=price*quantity
    #how the += logic works
    #takes the value of the left side and adds it to the value of the right side
    #if self.total was 10sh and self.final item was 2sh total would be 12sh
    #and 12sh would be the value of the total
    self.total += total_cost
    for _ in range(quantity):
      self.items.append(title)
    
  def apply_discount(self):
        if self.discount > 0:
            discount_amount = (self.discount / 100) * self.total
            self.total -= discount_amount
            print(f"After the discount, the total comes to ${self.total:.2f}.")
        else:
            print("There is no discount to apply.")

  def void_final_item(self):
        self.total =- self.last_item
        if self.total <0:
           self.total=0













