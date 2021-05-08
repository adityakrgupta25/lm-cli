import os
import cmd_handlers

if __name__ == "__main__":
    print("***Like-Minds CLI Tool***\n")
    while True:
        inp = input(">> ")
        params = inp.split()
        cmd = params[0]

        if cmd == "quit":
            os._exit(0)

        if cmd == "debug":
            import pdb
            pdb.set_trace()

        f = cmd_handlers.exec.get(cmd, None)
        if f is None:
            print("Cant recognize this command")
            continue

        # Execute commands
        f(params[1:])
