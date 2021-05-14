# -*- coding: utf-8 -*-

# TASK-1

sales = {
  "cost_value": 31.87,
  "sell_value": 45.00,
  "inventory": 1000
}  



price = (sales["sell_value"] - sales["cost_value"]) * sales["inventory"]
total_profit = "%.1f" %price

print(f"the profit will be {total_profit} dollars")


# TASK-2

worker1 = float(input("çalışanın alacağı ödemeyi yazınız: "))
worker2 = float(input("çalışanın alacağı ödemeyi yazınız: "))
worker3 = float(input("çalışanın alacağı ödemeyi yazınız: "))

payrolls = "%.2f" %worker1, "%.2f" %worker2, "%.2f" %worker3

print(f"the workers in company payrolls is here {payrolls}")