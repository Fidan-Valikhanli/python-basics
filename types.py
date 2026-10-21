# Təxminlər:
# 10 -> int
# 10.0 -> float
# "10" -> str
# True -> bool
# "True" -> str
# 3 + 2.0 -> float
# "3" + "2" -> str
# 10 / 2 -> int (təxminim)

print("10:", type(10))
print("10.0:", type(10.0))
print('"10":', type("10"))
print("True:", type(True))
print('"True":', type("True"))
print("3 + 2.0:", type(3 + 2.0))
print('"3" + "2":', type("3" + "2"))
print("10 / 2:", type(10 / 2))

# Səhv təxminim: 10 / 2 nəticəsinin int olduğunu düşündüm.
# Python-da / operatoru nəticəni float qaytarır: 5.0.
