import sys
my_dict = {}
size_dict = {}
for i in range(1000):
    my_dict[i] = i
    size = sys.getsizeof(my_dict)
    if size in size_dict:
        size_dict[size] += 1
    else:
        size_dict[size] = 1

total = 0
bucket_size = 2 ** 3
for _, value in size_dict.items():
    total += value
    print(total, bucket_size * 2 / 3)

    bucket_size *= 2
print(size_dict)

my_list = []
size_dict2 = {}
for i in range(1000):
    my_list.append(i)
    size = sys.getsizeof(my_list)
    if size in size_dict2:
        size_dict2[size] += 1
    else:
        size_dict2[size] = 1
print(size_dict2)
total = 0
bucket_size = 2 ** 3
for _, value in size_dict2.items():
    total += value
    print(total, value)
    bucket_size *= 2

print(sys.getsizeof(my_list))
print(sys.getsizeof([1 for i in range(1000)]))