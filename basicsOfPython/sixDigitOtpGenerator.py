import random

def myotp(otp,urotp):
    if otp == urotp:
        return f"Otp matched successfully !"
    elif otp != urotp:
        return f"Otp not matched !"
    else:
        return f"something went to wrong"
if __name__ == "__main__":
    while True:
        otp = random.randrange(100000,999999)
        print(f"Your otp:{otp}")
        urotp = int(input("Enter your otp:"))
        print(myotp(otp,urotp))
