FROM ubuntu:focal


# Installing Python and Django
RUN 	apt update && apt install -y software-properties-common &&\
	add-apt-repository ppa:deadsnakes/ppa &&\
	apt install -y python3.8 &&\
	apt-get install -y python3-distutils python3-apt &&\
	curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py && python3 get-pip.py &&\
	python3 -m pip install Django && pip install django-environ




