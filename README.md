# GitlabWikiSyncWithWord
This repository houses Python code that will serve as a background task in Windows for pushing Word documents to Gitlab Wiki pages.

## Development Setup
This section briefly describes the process to setup the repository for local testing on a Windows machine:
1. Clone the repository to your local machine.
2. Navigate into the repository directory
3. Run the development setup script (WINDOWS ONLY, you may need to run inside an admin shell):
    `.\dev_setup.ps1`
4. Modify the `.env` file as needed for your local testing
5. Enjoy
    a. If you needed to update the dependencies, make sure to update the dependency list as well (WHILE IN THE VIRTUAL ENVIRONMENT) like so:
        `pip freeze > requirements.txt`

## Deployment
This section briefly explains the deployment process of the python module as a background task on a Windows Machine.
This deployment is made for a self-hosted version of Gitlab.  I've not tested it with the web version.
1. Clone the repository to your local machine.
2. Navigate into the repository directory
3. Make a copy of the `default.env` and rename it to `.env`
4. Modify the `.env` file as needed for your deployment
5. Run the deployment script (WINDOWS ONLY, you may need to run inside an admin shell):
    `.\install_task.ps1`