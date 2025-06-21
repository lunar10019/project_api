FROM jenkins/jenkins

USER root

RUN apt update && apt install -y python3 python3-pip