# continuous-integration

http://ruleoftech.com/2017/dockerizing-all-the-things-running-ansible-inside-docker-container

from inside :

docker run --rm -it -v ${pwd}:/ansible/playbooks \
    walokra/ansible-playbook --version

With another file :

docker run --rm -it -v ${pw}):/ansible/playbooks continous-integration/ansible-docker:0.0.1 ./playbooks/playbook-apache

#####################

Certif

openssl rsa -noout -modulus -in .\EV-amivac.com-decembre2018.key | openssl md5 ; openssl x509 -noout -modulus -in .\EV-amivac.com-decembre2
018.cer | openssl md5 ; openssl req -noout -modulus -in .\EV-amivac.com-decembre2018.csr | openssl md5

#####################
- hosts: pchr-elk-ce7410

  tasks:
    - shell: >-
        hostname
      register: res
    - debug:
        msg: "/data/elasticsearch/{{ inventory_hostname }}-node01"
        #msg: "{{ hostvars['elasticsearch_ingests'].ansible_host }}"
        #msg: "{{ res }}"


####################
