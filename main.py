import stripe

keys = []
while True:
    key = (str(input("Enter Stripe API key(press q to exit): ")))
    if key == "q":
        break
    keys.append(key)

for api_key in keys:
    try:
        stripe.api_key = api_key
        stripe.Account.retrieve()
        print(f"API key: {api_key} is valid")
    except stripe.error.InvalidRequestError as e:
        print(f"API key: {api_key} is invalid. Error message: {e}")
