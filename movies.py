age=int(input("enter your age:"))
day=input("enter the day:")

price=12 if(age>=18) else 8
if(day=="wednesday"):
    price-=2
print(f"ticket rate is ${price}")
# if age>=18:
#     # if(day=="wednesday"):
#     #     print("ticket rate is $10")
#     # else:
#     #     print("ticket rate is $12")

# else:
#     if(day=="wednesday"):
#         print("ticket rate is $6")
#     else:
#         print("ticket rate is $8")


