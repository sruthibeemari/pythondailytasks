prices = [100, 200, 300, 400]
updated_list=[i*0.9 if i>200 else i for i in prices]
print("Updated Price List: ",updated_list)