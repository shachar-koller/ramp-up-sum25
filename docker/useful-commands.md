## 🐳 Useful Docker Commands

```bash
# Run a Docker image (creates and starts a container)
docker run <image_name>

# Run a Docker image in interactive mode (e.g. for bash access)
docker run -it <image_name>

# Run a Docker image in detached mode (runs in background)
docker run -d <image_name>

# List currently running containers
docker ps

# List all containers (running and stopped)
docker ps -a

# Stop a running container
docker stop <container_id_or_name>

# Start container with name
docker run --name <container_name> <image_name>

# Filter running container on name
docker ps -f "name=<container_name>"

# See logs for container
docker logs <container_id_or_name>

# See live logs for container
docker logs -f <container_id_or_name>

# Exit live log view of container
Ctrl + C

# Remove a stopped container
docker rm <container_id_or_name>

```