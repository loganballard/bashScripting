#! /bin/bash

mkdir output-jsons
cd repos
REPOS=$(ls -l | awk '{print $9}')
for R in $REPOS
do
    cd $R
    npm i --package-lock-only
    npm audit --json > ../../output-jsons/$R.json
    cd ..
done
cd ..
python $PWD/parse-npm-audit.py