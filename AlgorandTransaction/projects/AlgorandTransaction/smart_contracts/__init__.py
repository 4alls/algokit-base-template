import algokit_utils as au
# 1. Se connecter au LocalNet via AlgoKit Utils
algorand = au.AlgorandClient.default_localnet()
# 2. Obtenir le compte "dispenser" qui est pré-financé sur le LocalNet
dispenser = algorand.account.localnet_dispenser()
print(f"Adresse du Dispenser: {dispenser.address}\n")
# 3. Créer deux comptes de test : Alice et Bob
alice = algorand.account.random()
bob = algorand.account.random()
print(f"Compte d'Alice: {alice.address}")
print(f"Compte de Bob: {bob.address}\n")
# 4. Financer ces comptes à partir du dispenser pour qu'ils puissent effectuer des transactions
algorand.send.payment(
    au.PaymentParams(
        sender=dispenser.address,
        receiver=alice.address,
        amount=au.AlgoAmount.from_algo(10) # 10 ALGOs
    )
)
algorand.send.payment(
    au.PaymentParams(
        sender=dispenser.address,
        receiver=bob.address,
        amount=au.AlgoAmount.from_algo(10)
    )
)
print("Comptes d'Alice et Bob financés avec succès !")