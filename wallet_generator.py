from eth_account import Account

print("=== Web3 Wallet Generator ===")

num = int(input("How many wallets do you want to generate? "))

for i in range(num):
    acct = Account.create()

    print("\nWallet", i + 1)
    print("Address:", acct.address)
    print("Private Key:", acct.key.hex())
