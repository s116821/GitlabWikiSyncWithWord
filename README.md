# GitlabWikiSyncWithWord

This repository houses Python code that will serve as a background task in Windows for pushing Word documents to Gitlab Wiki pages.

## Development Setup

This section briefly describes the process to setup the repository for local testing on a Windows machine:

1. Clone this repository to your local machine.
2. Clone the Gitlab Wiki repositories to the location of your choice
    a. For the Wiki git url, go to the wiki page home via Gitlab Web interface and press the clone repository button
    b. Make sure to add an SSH key for your user (there are guides online for that)
    c. IMPORTANT -> If your self-hosted instance has it's sshd port set to something other than the default, consult the bottomost section for additional guidance
3. Navigate into this background task's repository directory
4. Run the development setup script (WINDOWS ONLY, you may need to run inside an admin shell):
    `.\dev_setup.ps1`
5. Modify the `.env` file as needed for your local testing
6. Enjoy
    a. If you needed to update the dependencies, make sure to update the dependency list as well (WHILE IN THE VIRTUAL ENVIRONMENT) like so:
        `pip freeze > requirements.txt`
    b. If using VS Code, the default Python File debugger should work for testing, just make sure the correct virtual environment is selected in bottom right of IDE

## Deployment

This section briefly explains the deployment process of the python module as a background task on a Windows Machine.
This deployment is made for a self-hosted version of Gitlab.  I've not tested it with the web version.

1. Clone this repository to your local machine.
2. Clone the Gitlab Wiki repositories to the location of your choice
    a. For the Wiki git url, go to the wiki page home via Gitlab Web interface and press the clone repository button
    b. Make sure to add an SSH key for your user (there are guides online for that)
    c. IMPORTANT -> If your self-hosted instance has it's sshd port set to something other than the default, consult the bottomost section for additional guidance
3. Navigate into this background task's repository directory
4. Make a copy of the `default.env` and rename it to `.env`
5. Modify the `.env` file as needed for your deployment
6. Run the deployment script (WINDOWS ONLY, you may need to run inside an admin shell):
    `.\install_task.ps1`


## Dealing with Gitlab Host Servers with Non-standard SSH Port

If your self-hosted instance has it's sshd port set to something other than the default, you should know that the gitlab instance WILL STILL run its own sshd on the standard port.  So, if your local dev machine ssh config file has an entry in it for the custom SSH port, you will need to make an alias entry for the gitlab host so it routes to the right port.  For example:  

&emsp; Normally you may use a wiki git url like so `git@{YOUR_MACHINE_HOSTNAME}:some_project_space/some_code_repo.wiki.git`, but if you added an additional entry to the ssh config file like so:

&emsp;&emsp; Host <gitlab_self-host>
&emsp;&emsp;&emsp; HostName YOUR_MACHINE_HOSTNAME
&emsp;&emsp;&emsp; Port 22
&emsp;&emsp;&emsp; IdentityFile ~/.ssh/some_ssh_key_file

&emsp; Then you would use the following url instead: `git@<gitlab_self-host>:some_project_space/some_code_repo.wiki.git` when performing your git clone and it should work!