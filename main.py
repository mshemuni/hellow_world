from hello_world import Character, Message, Hello

if __name__ == '__main__':
    m = Message(
        [
            Character("H"), Character("e"), Character("l"),
            Character("l"), Character("o"), Character(" "),
            Character("W"), Character("o"), Character("r"),
            Character("l"), Character("d"), Character("!")
        ]
    )
    h = Hello(m)
    h.print()
