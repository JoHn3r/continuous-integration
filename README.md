# continuous-integration

http://ruleoftech.com/2017/dockerizing-all-the-things-running-ansible-inside-docker-container

from inside :

docker run --rm -it -v ${pwd}:/ansible/playbooks \
    walokra/ansible-playbook --version

With another file :

docker run --rm -it -v ${pw}):/ansible/playbooks continous-integration/ansible-docker:0.0.1 ./playbooks/playbook-apache



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
