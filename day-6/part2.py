SEQUENCE_SIZE = 14

with open('day-6/input.txt', 'r') as source:
    data = source.read().splitlines()[0]
    chunks = [data[i:i + SEQUENCE_SIZE] for i in range(len(data))]
    print(next(index for (index, chunk) in enumerate(chunks) if len(set(chunk)) == SEQUENCE_SIZE) + SEQUENCE_SIZE)

