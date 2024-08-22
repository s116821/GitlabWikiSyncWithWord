# SETUP SCRIPT FOR LOCAL TESTING ON WINDOWS

# Define relative paths
$repoPath = (Get-Location).Path
$venvPath = "$repoPath\venv"
$requirementsPath = "$repoPath\requirements.txt"
$defaultEnvPath = "$repoPath\default.env"
$envFilePath = "$repoPath\.env"

# Create virtual environment if it doesn't exist
if (-Not (Test-Path $venvPath)) {
    python -m venv $venvPath

    # Activate virtual environment
    & "$venvPath\Scripts\Activate.ps1"

    # Install required Python modules from requirements.txt
    pip install -r $requirementsPath

    # Deactivate virtual environment
    & "$venvPath\Scripts\Deactivate.ps1"
}

# Copy default.env to .env if .env doesn't exist
if (-Not (Test-Path $envFilePath)) {
    Copy-Item -Path $defaultEnvPath -Destination $envFilePath
    Write-Output "Copied default.env to .env"
} else {
    Write-Output ".env file already exists"
}