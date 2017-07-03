import sys
import subprocess
import re


def main():
    preferences = subprocess.check_output(
        ['defaults', 'read', 'com.gvne.urlhandler']
    )
    for line in preferences.split('\n'):
        if "Script = " in line:
            # value should be Script = "path I need";
            m = re.match("Script = \"(.*)\";", line.strip())
            script = m.groups()[0]
            pid = subprocess.Popen(["python", script, sys.argv[1]])

if __name__ == "__main__":
   main()
