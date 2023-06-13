#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    for w in dir(hidden_4):
        if w[0] != '_' and w[1] != '_':
            print(w)
