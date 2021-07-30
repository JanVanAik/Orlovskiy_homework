src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
num_gen = (v for k, v in enumerate(src) if src[k] > src[k-1] and k != 0)
print(type(num_gen))
print(list(num_gen))
