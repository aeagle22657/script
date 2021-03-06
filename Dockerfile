FROM ubuntu

RUN apt-get update
RUN apt-get install -y -qq git python python-dev pip
RUN pip install shutit

WORKDIR /opt
# Change the next two lines to build your ShutIt module.
RUN git clone https://github.com/yourname/yourshutitproject.git
WORKDIR /opt/yourshutitproject
RUN shutit build --delivery dockerfile
CMD ["/bin/bash"]
