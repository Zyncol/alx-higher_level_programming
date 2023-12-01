#!/usr/bin/python3
# prints all the names
if __name__ == "__main__":
    import hidden_4
    for dzina in dir(hidden_4):
        if not dzina[0] == '_' and not dzina[1] == '_':
            print(dzina)
