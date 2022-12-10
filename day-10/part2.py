from typing import List

def _register_value_at_cycle(at_cycle, lines: List[str]):
    current_cycle = 1
    register_value = 1
    for line in lines:
        split = line.split(' ')
        command = split[0]
        if command == 'noop':
            current_cycle += 1
        else:
            current_cycle += 2
        if current_cycle > at_cycle:
            return register_value
        elif len(split) > 1:
            register_value += int(split[1])
    raise "oops"

def _should_add_pixel(at_cycle, crt_position, lines) -> bool:
    register_value = _register_value_at_cycle(at_cycle, lines)
    return crt_position in list(range(register_value - 1, register_value + 2))

if __name__ == '__main__':
    with open('day-10/input.txt', 'r') as source:
        lines = source.read().splitlines()
        crt_pixes = []
        crt_position = 0
        for current_cycle in range(1, 241, 1):
            if _should_add_pixel(current_cycle, crt_position, lines):
                crt_pixes.append('#')
            else:
                crt_pixes.append('.')
            crt_position += 1
            if crt_position >= 40:
                crt_position = 0
        print('Part 2:')
        for i in range(0, 240, 40):
            print(''.join(crt_pixes[i:i+40]))

