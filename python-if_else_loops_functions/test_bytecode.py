import dis
magic_calculation = __import__('102-magic_calculation').magic_calculation

print("Testing magic_calculation:")
print(f"magic_calculation(1, 2, 3) = {magic_calculation(1, 2, 3)}")
print(f"magic_calculation(5, 3, 10) = {magic_calculation(5, 3, 10)}")
print(f"magic_calculation(5, 3, 2) = {magic_calculation(5, 3, 2)}")

print("\nBytecode for magic_calculation:")
dis.dis(magic_calculation)
