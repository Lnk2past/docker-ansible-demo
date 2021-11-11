# docker-ansible-demo

[Live] demo to illustrate basic automation tasks. The idea is simple - we want to use `Ansible` to configure a few nodes, run code on them, and then patch that code.

**DISCLAIMER** The setup in this repository does some pretty dumb things and should not be used for more than just education.

## TL/DR

### Build

```shell
docker build -t my-alpine .
docker build -t my-ansible -f Dockerfile.ansible .
docker-compose up
```

### Run

```shell
docker exec -it ansible_docker_demo_ansible_1 sh
```

```shell
cd ansible_playbooks
ansible-playbook 01_install_python_setup.yaml
ansible-playbook 02_install_flask.yaml
ansible-playbook 03_deploy_webapp_v1.yaml
ansible-playbook 04_run_webapp.yaml
ansible-playbook 05_deploy_webapp_v2.yaml
```

## Docker

We use `Docker` with `Docker Compose` to simulate an environment with a handful of "fresh nodes" that a sysadmin will start to work with. There are a number of details assumed and heavily glossed over here, specifically with SSH keys/psswordless SSH being setup automatically. This allows `Ansible` to work nicely right from the beginning.

There are 3 "worker" nodes and 1 "admin" node. The admin node is the same image as the workers, but includes `Ansible` as well as some some files pre-installed. Once the compose environment is stood up we can exec into the admin node and begin automating some basic tasks on the worker nodes.

## Ansible

The playbooks are numbered, and should be executed in that order. They do the following:

1) installs some python requirements for used with `Ansible`
2) installs `Flask`
3) deploys v1 of our webapp
4) starts the webapp
5) deploys v2 of our webapp

Once playbook 04 is executed you can navigate to localhost:1333[7/8/9] to see the `Hello World` example taken from `Flask's` quick start. After playbook 05 is executed, refreshing your page will reveal the v2 webapp. The code that is running is a basic `Flask` webapp with the development environment. This is purely to simulate the deployment of live code to a server and is not meant to be a realistic use case for `Flask's` development environment.
