account_type=input("Enter account type, standard or premium").strip().lower()
Amount = float(input("Enter amount "))
if account_type=="standard":
    if Amount>500:
        print("Transaction exceeds the limit for Standard accounts.")
    else:
        print("Transaction approved.")
elif account_type == "premium":
    if Amount>1000:
        print("Transaction exceeds the limit for Premium accounts.")
    else:
        print("Transaction approved.")
else:
    print("Transaction complicated")
