import sys


def main():
    log_path = "/tmp/write_args_script.log"
    with open(log_path, 'w') as log:
        log.write(str(sys.argv))
        print("logged at " + log_path)

if __name__ == "__main__":
   main()
