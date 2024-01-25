#!/usr/bin/env bash

mkdir downloads
git clone --branch 0.18.8 --single-branch https://github.com/great-expectations/great_expectations.git downloads
rsync -av --exclude='.github' --exclude='.gitignore' --exclude='sync.sh' --exclude='sonar-project.properties' downloads/* ./
rm -rf downloads