#!/bin/sh
set -e
KUBE_SECRET="$1"
# check for secret existence
if [ -z $KUBE_SECRET ]; then
    echo "no secret specified "
    exit 1
fi
if [ -z "$(kubectl get secret $KUBE_SECRET)" ]; then
    if ! [ -z "$(kubectl get secrets | grep $KUBE_SECRET)" ]; then
        echo "Did you mean one of these?"
        echo "$(kubectl get secrets | grep $KUBE_SECRET)"
    fi
    exit 1
fi

# get secret data
kubectl get secret "$KUBE_SECRET" -o yaml > kubeSec
echo "$(yq r kubeSec data)" > kubeSecData

# loop through secret data and pull individuals
IFS='\n'
while read secretLine; do
    echo "Encoded:\n$secretLine"
    IFS=':' 
    read -ra SECARR <<< "$secretLine"
    SECRET_ENCODED="$(echo ${SECARR[1]} | sed 's/ //g')" # trim whitespace
    SECRET_DECODED="$(echo $SECRET_ENCODED | base64 -D)"
    echo "Unencoded:\n$SECRET_DECODED\n"
    IFS='\n'
done < kubeSecData

rm -f ./kubeSecData ./kubeSec