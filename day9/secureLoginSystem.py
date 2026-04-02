def login_required(func):
    def wrapper(is_logged_in):
        if is_logged_in:
            func(is_logged_in)
        else:
            print("Access Denied, Please login")
            return wrapper
@login_required
def viewDashboard():
    print("welcome to Dashboard")
@login_required
def makePayment():
    print("payment successful")

viewDashboard(True)
makePayment(False)
