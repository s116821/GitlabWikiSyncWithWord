# INSTALLATION SCRIPT FOR WINDOWS TASK SCHEDULER

# Define relative paths
$repoPath = (Get-Location).Path
$scriptPath = "$repoPath\gitlab_wiki_sync.py"
$venvPath = "$repoPath\venv"
$requirementsPath = "$repoPath\requirements.txt"
$taskName = "GitLabWikiUpdater"

# Check if the .env file exists
if (-Not (Test-Path $envFilePath)) {
    Write-Output ".env file does not exist. Please create the .env file before running this script."
    exit 1
}

# Create virtual environment if it doesn't exist
if (-Not (Test-Path $venvPath)) {
    python -m venv $venvPath

    # Activate virtual environment
    & "$venvPath\Scripts\Activate.ps1"

    # Install required Python modules from requirements.txt
    pip install -r $requirementsPath

    # Deactivate virtual environment
    & deactivate
}

# Check if the scheduled task already exists
$taskExists = Get-ScheduledTask -TaskName $taskName -ErrorAction SilentlyContinue

if (-Not $taskExists) {
    # Define the action to run the Python script
    $action = New-ScheduledTaskAction -Execute "$venvPath\Scripts\python.exe" -Argument $scriptPath

    # Define the trigger to run the task every hour
    $trigger = New-ScheduledTaskTrigger -Hourly -At (Get-Date).Date.AddHours(1)

    # Register the scheduled task
    Register-ScheduledTask -Action $action -Trigger $trigger -TaskName $taskName -Description "Updates GitLab Wiki from Word documents every hour" -User "SYSTEM" -RunLevel Highest
} else {
    Write-Output "Scheduled task '$taskName' already exists."
}
