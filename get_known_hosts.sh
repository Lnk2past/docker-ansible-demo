#!/bin/sh
ssh-keyscan -H node1 >> ~/.ssh/known_hosts
ssh-keyscan -H node2 >> ~/.ssh/known_hosts
ssh-keyscan -H node3 >> ~/.ssh/known_hosts