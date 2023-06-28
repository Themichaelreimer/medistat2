try:
    import os, sys
    import dotenv
    import importlib
except ModuleNotFoundError:
    print("Could not find required package for CLI. Try running `pip3 install -r commands/requirements.txt`.")

if __name__ == "__main__":

    dotenv.load_dotenv()
    command = None
    try:
        command = sys.argv[1]
    except:
        module = importlib.import_module(f"commands.help")
        module.run()
        exit(127)

    if command:
        try:
            sys.argv = sys.argv[1:]  # Effectively removes the manager.py from sys.argv. Makes things easier for argparse
            module = importlib.import_module(f"commands.{command}")
            module.run()
        except ModuleNotFoundError as e:
            print(e)
            print(f"Could not find command {command} in commands folder")