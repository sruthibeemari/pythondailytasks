import numpy as np
import pandas as pd
import time

#1
def timer(func):
    def wrapper(*args,**kwargs):
        start=time.time()
        result=func(*args,**kwargs)
        end=time.time()
        print(f"Execution time: {end - start:.5f} seconds")
        return result
    return wrapper

#2
def read_numbers(file_name):
    with open(file_name,"r") as file:
        for line in file:
            try:
                yield float(line.strip())   # convert to number
            except ValueError:
                print("Invalid data skipped:", line.strip())


#3
@timer
def process_data(file_name):
    data=list(read_numbers(file_name))

    mean=np.mean(data)
    std=np.std(data)

    df=pd.DataFrame({
        "Metric":["Mean","Std Dev"],
        "Value":[mean,std]
    })

    return df

result = process_data("data.txt")
print("\nResult DataFrame:\n", result)
