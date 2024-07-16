FROM chaoge615/myflask:latest

WORKDIR /var/www/

RUN apt update&&apt install git -y&&git clone https://github.com/lcc-666/gaokao.git&&pip install -r ./gaokao/fun/requirements.txt \
    && cp ./gaokao/custom.conf /etc/apache2

EXPOSE 5002