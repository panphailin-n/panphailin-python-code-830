# Set relationships

<<<<<<< HEAD
=======
print(f"All animals: {all_animals}")
print(f"Pets: {pets}")
print(f"Mammals: {mammals}")
print(f"Small pets: {small_pets}")

# Subset and superset
print(f"Are pets subset of all animals? {pets.issubset(all_animals)}") # pets เป็นสับเซตของสัตวืทั้งหมดมั้ย
print(f"Are all animals superset of pets? {all_animals.issuperset(pets)}")

# Disjoint sets (no common elements)
birds = {"eagle", "sparrow", "parrot"}
print(f"Birds: {birds}")
print(f"Are mammals and birds disjoint? {mammals.isdisjoint(birds)}")
print(f"Are pets and small_pets disjoint? {pets.isdisjoint(small_pets)}")

# Set equality
pets_copy = {"dog", "cat", "rabbit"}
print(f"Are pets equal to pets_copy? {pets == pets_copy}")

# Length and membership
print(f"Number of mammals: {len(mammals)}")
print(f"Is 'dog' in mammals? {'dog' in mammals}")
print(f"Is 'fish' in mammals? {'fish' in mammals}")
>>>>>>> 3246234867a2cd467afebad74eed3a182945b8eb
