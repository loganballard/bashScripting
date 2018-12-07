## NPM Auto-audit

* This handy-dandy little script will run NPM audits on your code repos and output a useful json file with recommendations on what to do.  
* First make sure you have python installed and that it's on your $PATH
* Navigate to the repos directory
* `git clone` any repos you want to audit such that you have a copy of the repo as a subdirectory of "repos"
* remove the "insert-repos-here" file
* remove the "tickets-go-here" file
* From the root directory of this repo, run the auto-run-audit.sh script as sudo and you should be golden!
* tickets directory will be populated with "tickets" that are really just human-readable output of the JSON recommendations file.  Eventually I'd love to hook this in to JIRA, but that's for the future
