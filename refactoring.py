def read_data():
    with open('/tmp/data.txt') as f:
        data = f.readline()
        return data


a = [1, 2, 3, 4]
print(sum(a))


a = [1, -2, 3, -4]
print(
    list(
        filter(lambda i: i > 0, a)
    )
)
