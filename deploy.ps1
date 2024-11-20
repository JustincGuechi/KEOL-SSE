# Variables
$DOCKER_USERNAME = "justinguechi"
$FRONTEND_IMAGE = "keol-sse-frontend"
$BACKEND_IMAGE = "keol-sse-backend"
$TAG = "latest"
$MSSQL_IMAGE = "mcr.microsoft.com/mssql/server"
$MSSQL_CONTAINER_NAME = "keol-sse-mssql"
$MSSQL_SA_PASSWORD = "YourStrong!Passw0rd"
$MSSQL_DATABASE = "keol_sse_db"

# Build frontend image
Write-Output "Building frontend Docker image..."
docker build -t "$($DOCKER_USERNAME)/$($FRONTEND_IMAGE):$($TAG)" ./keol-sse-frontend

# Build backend image
Write-Output "Building backend Docker image..."
docker build -t "$($DOCKER_USERNAME)/$($BACKEND_IMAGE):$($TAG)" ./keol-sse-back-end

# Pull MSSQL image
Write-Output "Pulling MSSQL Docker image..."
docker pull $MSSQL_IMAGE

# Run MSSQL container
Write-Output "Running MSSQL Docker container..."
docker run -e "ACCEPT_EULA=Y" -e "SA_PASSWORD=$MSSQL_SA_PASSWORD" -e "MSSQL_DATABASE=$MSSQL_DATABASE" -p 1433:1433 --name $MSSQL_CONTAINER_NAME -d $MSSQL_IMAGE

# Run frontend container in a new PowerShell window
Write-Output "Running frontend Docker container..."
Start-Process powershell -ArgumentList "docker run -it --rm -p 80:80 $($DOCKER_USERNAME)/$($FRONTEND_IMAGE):$($TAG)"

# Run backend container in a new PowerShell window
Write-Output "Running backend Docker container..."
Start-Process powershell -ArgumentList "docker run -it --rm -p 5000:5000 $($DOCKER_USERNAME)/$($BACKEND_IMAGE):$($TAG)"

Write-Output "Deployment complete."