import subprocess
import shlex
from subprocess import PIPE
import pexpect


def run_command(command):
    process = subprocess.Popen(shlex.split(command), stdout=subprocess.PIPE, stdin = subprocess.PIPE)
    while True:
        output = process.stdout.readline()
        
        if output == '' and process.poll() is not None:
            break
        if output:
            print (output.strip())
            process.stdin.write(b"Hello friend!")
           
    rc = process.poll()
    return rc

def tryOutput():
    p = subprocess.Popen("echo hello", stdout=subprocess.PIPE, stdin = subprocess.PIPE)
    #p.communicate("echo you too")
    print (p.communicate(input = b"echo you"))
    print (p.communicate(input = b"echo you"))

    
    
    p.wait()
    print (p.returncode)


def tryExpect():
    child = pexpect.popen_spawn.PopenSpawn("scp rasa shell")
    child.expect("Your input ->")
    child.sendline("hello!")
