import subprocess
subprocess.call('git clone https://github.com/a2z-ice/eureka-server.git || (cd eureka-server ; git pull)', shell = True)
subprocess.call('cd eureka-server', shell = True)
subprocess.call('mvn -f pom.xml package -Dspring.profiles.active=docker', shell = True)
subprocess.call('cd ./eureka-server/', shell = True)
subprocess.call('docker build . -t eureka-server', shell = True)





