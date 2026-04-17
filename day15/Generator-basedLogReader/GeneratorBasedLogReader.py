def read_logs(file_name):
    with open(file_name,"r") as file:
        for line in file:
            yield line.strip()

error_count={}

for log in read_logs("log.txt"):
    if "ERROR" in log:
        print("Log Error",log)

        error_count[log]=error_count.get(log,0)+1

print("Error Summary: \n")
for err,count in error_count.items():
    print(err,"==>",count)

