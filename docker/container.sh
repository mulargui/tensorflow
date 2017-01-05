sudo docker stop TENSORFLOW
sudo docker rm -f TENSORFLOW
sudo docker run -ti --name TENSORFLOW -p 6006:6006 -p 8888:8888 -v /vagrant/apps/tensorflow:/myapp gcr.io/tensorflow/tensorflow /bin/bash
#sudo docker run -ti --name TENSORFLOW -p 6006:6006 -p 8888:8888 -v /vagrant/apps/tensorflow:/myapp gcr.io/tensorflow/tensorflow 