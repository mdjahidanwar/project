# project(Automated build script using Python)
#System requirements: Make sure that system have jdk 8(1.8.0_251 version is preferred), maven version 3.6.3,latest docker and git installed.


#pythonautomation.py (python script)
import subprocess                #need to import 'subprocess' so that we can pass shell command in python script 
subprocess.call('git clone https://github.com/a2z-ice/eureka-server.git || (cd eureka-server ; git pull)', shell = True)    #will clone a git repo if not cloned and if already cloned then it will pull in the eureka-server dir   
subprocess.call('cd eureka-server', shell = True)
subprocess.call('mvn -f pom.xml package -Dspring.profiles.active=docker', shell = True) # building java project.. we must have pom.xml file configured 
subprocess.call('cd ./eureka-server/', shell = True)
subprocess.call('docker build . -t eureka-server', shell = True) #creating docker image from Dockerfile(in my case docker file is in the current directory)




####after running the script we have to push the docker image to dockerhub 
####from terminal we need to login in docker with 'docker login' command
###then 
###run the following commands to push the docker image 

 docker push mdjahidanwar/eureka-server:7   ### here mdjahidanwar is my docker login and repo name 
 docker rm 148xxxxxxxx   ### to remove the container with container ID
 docker rmi 74dxxxxxxxx ### remove the docker image from local repo 
 docker pull mdjahidanwar/eureka-server:7 ###pull the docker image 



use "docker run" with arguments to run the image
