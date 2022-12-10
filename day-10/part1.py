if __name__ == '__main__':
    with open('day-10/input.txt', 'r') as source:
        stop_cycles = [20, 60, 100, 140, 180, 220]
        stop_cycles_values = []
        register_value = 1
        current_cycle = 1
        lines = source.read().splitlines()
        for line in lines:
            split = line.split(' ')
            command = split[0]
            if command == 'noop':
                current_cycle += 1
            else:
                current_cycle += 2

            if len(stop_cycles) == 0:
                break
            if current_cycle > stop_cycles[0]:
                stop_cycles_values.append(stop_cycles[0] * register_value)
                stop_cycles = stop_cycles[1:]

            if len(split) > 1:
                register_value += int(split[1])
        print(sum(stop_cycles_values))

                

