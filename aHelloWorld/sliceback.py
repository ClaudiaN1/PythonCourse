        #            1         2
        #  01234567890123456789012345
letters = "abcdefghijklmnopqrstuvwxyz"

backwards = letters[25::-1]     # zyxwvutsrqponmlkjihgedcba
backwards = letters[::-1]       # zyxwvutsrqponmlkjihgedcba
backwards = letters[25:0:-1]    # zyxwvutsrqponmlkjihgedcb
print(backwards)

print(letters[16:13:-1])  # qpo
print(letters[4::-1])     # edcba
print(letters[:-9:-1])    # zyxwvuts

print(letters[-4:])  # wxyz
print(letters[-1:])  # z
print(letters[:1])   # a
print(letters[0])    # a