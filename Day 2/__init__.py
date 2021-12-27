def calculate_pos(commands):
    x = 0
    depth = 0
    for command in commands:
        if command[0] == "forward":
            x += command[1]
        elif command[0] == "up":
            depth -= command[1]
        elif command[0] == "down":
            depth += command[1]
    return (x * depth)

def calculate_pos_fixed(commands):
    x = 0
    depth = 0
    aim = 0
    for command in commands:
        if command[0] == "forward":
            x += command[1]
            depth += (aim * command[1])
        elif command[0] == "up":
            aim -= command[1]
        elif command[0] == "down":
            aim += command[1]
    return (x * depth)


if __name__ == "__main__":
    f = open('Day 2/input.txt', 'r')
    commands_unparsed = (f.read()).splitlines()
    commands = []
        
    for command in commands_unparsed:
        command_split = command.split(" ")
        commands.append([command_split[0], int(command_split[1])])
    
    print(calculate_pos_fixed(commands))