alice_candies = int(input("Kẹo của Alice: "))
bob_candies = int(input("Kẹo của Bob: "))
carol_candies = int(input("Kẹo của Carol: "))
to_smash= (alice_candies+bob_candies+carol_candies)%3
print("Kẹo dư: ", to_smash)