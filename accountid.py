# this python code slice and provide me only the account id in this arn
account_id= "arn:aws:iam::123456789012:user/Development/product_1234/*\n\n"
print(account_id[13:25])
print(f"the aws account id is: {account_id[13:25]}")