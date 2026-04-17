try:
    with open("logs.txt","a") as file:
        while True:
            log=input("Enter Log(type 'exit' to stop): ")
            if log.lower()=="exit":
                break
            file.write(log)

        print("Logs Saved Successfully")
except FileNotFoundError:
    print("File not Found")
except PermissionError:
    print("Permission Denied")