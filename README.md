Useful bash scripts that I wrote for automatic pain in the ass tasks
=====

* **k8sSecretsParser**: If you have base64 encoded secrets in a k8s deployment this will automatically pull them down and decode them. It'll print the decoded secrets to stdout. Syntax: ./k8sSecretsParser.sh [secret name]
   * Dependecy: yq
   https://yq.readthedocs.io/en/latest/

* **auto-npm-audit**: automatically run a security audit on your node or js repos and create a nice little json file that details any security risks you might have
   * Requires python
