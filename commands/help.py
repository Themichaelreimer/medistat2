import os


def run() -> None:
    print("Usage: python3 manager.py <COMMAND_NAME> <ARGS?>")

    files = [x for x in os.listdir("commands") if x[-3:] == ".py"]
    files.sort()

    print(f"Available commands: ")
    for file in files:
        # File with out the extension, since the command won't be entered with the extension
        print("".join(file.split(".")[:-1])) 