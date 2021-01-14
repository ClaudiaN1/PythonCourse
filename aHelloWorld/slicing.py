#                   1
#         012345678901234
parrot = "Norwegian Blue"

print(parrot[0:6])     # Norweg
print(parrot[-14:-8])  # Norweg

print(parrot[3:5])     # we
print(parrot[-11:-9])  # we

print(parrot[0:9])  # Norwegian
print(parrot[:9])   # Norwegian
print(parrot[-14:-5])

print(parrot[-4:])  # Blue
      # or
print(parrot[10:14])
      # or
print(parrot[10:])

print(parrot[:6])  # Norweg
print(parrot[6:])  # ian Blue

print(parrot[:-8])  # Norweg
print(parrot[-8:])  # ian Blue

print(parrot[:6] + parrot[6:])  # Norwegian Blue

print(parrot[:])  # Norwegian Blue
