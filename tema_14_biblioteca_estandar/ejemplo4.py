from subprocess import Popen
process = Popen(['ls', '-la'])
process.wait()
