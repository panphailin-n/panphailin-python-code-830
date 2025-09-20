# Basic set operations
fruits = {"apple", "banana", "orange", "grape"}
citrus = {"orange", "lemon", "lime", "grapefruit"}

print(f"Fruits: {fruits}")
print(f"Citrus: {citrus}")

# Adding elements
fruits.add("strawberry") # เพิ่มสมาชิกใหม่
print(f"After adding strawberry: {fruits}")

# Adding multiple elements
fruits.update(["kiwi", "mango"])
print(f"After adding multiple: {fruits}")

# Removing elements
fruits.remove("banana")  # Raises error if not found เอาออก
print(f"After removing banana: {fruits}")

fruits.discard("pineapple")  # No error if not found เอาออก
print(f"After discarding pineapple: {fruits}")

removed_fruit = fruits.pop()  # Remove arbitrary element
print(f"Removed: {removed_fruit}")
print(f"Remaining fruits: {fruits}")

# Set mathematical operations ช่วยให้เราเชื่อมกระบวนการของ set ได้

 