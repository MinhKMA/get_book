# Install 

## Cài đăt python3 trên centos7

```sh
yum -y install https://centos7.iuscommunity.org/ius-release.rpm
yum -y install python35u
yum -y install python35u-pip
yum install python35u-devel -y
mkdir environments
cd environments
python3.5 -m venv minhkma
source minhkma/bin/activate
```

## Cài đặt python3 trên ubuntu16

Tham khảo link: https://www.digitalocean.com/community/tutorials/how-to-install-python-3-and-set-up-a-local-programming-environment-on-ubuntu-16-04

## Clone repo 

`git clone https://github.com/MinhKMA/get_book.git`

## Install requirements

`pip3 install -r requirements.txt`

## Chạy chương trình 

`python3 get_book.py`
