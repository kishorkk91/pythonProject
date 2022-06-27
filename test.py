def transformdata(data, group_size):
    for i in data:
        if not isinstance(i, int):
            data.remove(i)
    for i in range(0, len(data), group_size):
        yield data[i:i + group_size]


mylist = [1, 2, 3, 4, 5, '22', 6, 7, 5.6, 8, 9, 10]
chunk_size = 3
print(list(transformdata(mylist, chunk_size)))
