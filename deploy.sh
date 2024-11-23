
#!/bin/bash

# Variables
DOCKER_USERNAME="justinguechi"
FRONTEND_IMAGE="keol-sse-frontend"
BACKEND_IMAGE="keol-sse-backend"
TAG="latest"

# Build frontend image
echo "Building frontend Docker image..."
docker build -t $DOCKER_USERNAME/$FRONTEND_IMAGE:$TAG ./keol-sse-frontend

# Push frontend image
echo "Pushing frontend Docker image..."
docker push $DOCKER_USERNAME/$FRONTEND_IMAGE:$TAG

# Build backend image
echo "Building backend Docker image..."
docker build -t $DOCKER_USERNAME/$BACKEND_IMAGE:$TAG ./keol-sse-back-end

# Push backend image
echo "Pushing backend Docker image..."
docker push $DOCKER_USERNAME/$BACKEND_IMAGE:$TAG

echo "Deployment complete."