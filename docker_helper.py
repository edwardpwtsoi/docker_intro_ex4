import subprocess
from subprocess import PIPE
from datetime import datetime

class NiceLogger:
    def log(self, message):
        datenow = datetime.today().strftime('%d-%m-%Y %H:%M:%S')
        print("{0} |  {1}".format(datenow, message))
        
class DockerHelper:
    niceLogger = NiceLogger()

    def build_and_run(self):
        image_build_command = ["docker","build","-t","postgre5432:latest",'.']
        self.run_command(image_build_command)
        name = datetime.today().strftime('%d_%m_%Y_%H_%M_%S')
        mountStr = "source=vol_{0},target=/var/lib/postgresql/data".format(name)
        run_container_command = ["docker","run","--name",name,"--mount",mountStr,"-P","-d","postgre5432:latest"]
        popen_run_container = self.run_command(run_container_command)
        error = popen_run_container.stderr.readline().decode("utf-8")
        if error != "":
            error = error.replace("\n", "")
            self.niceLogger.log("An error occurred:" + error)
            return error
        else:
            id = popen_run_container.stdout.readline().decode("utf-8")
            id = id.replace("\n", "")
            self.niceLogger.log(" - New container ID " + id)
        get_port_command=["docker","port",id]
        popen_prot = self.run_command(get_port_command)
        error2 = popen_prot.stderr.readline().decode("utf-8")
        if error2 != "":
            error2 = error2.replace("\n", "")
            self.niceLogger.log("An error occurred:" + error2)
            return error2
        else:
            port = popen_prot.stdout.readline().decode("utf-8").split(":")[-1]
            port = port.replace("\n", "")
            self.niceLogger.log(" - The new container is hosting on " + port)
            return port

    def run_command(self, command):
        debugcommand = " - {0}".format(" ".join(command))
        self.niceLogger.log(debugcommand)

        popen = subprocess.Popen(command, stdin=PIPE, stdout=PIPE, stderr=PIPE)
        popen.wait(500) # wait a little for docker to complete

        return popen

if __name__ == "__main__":

    print("This is a docker-helper module")