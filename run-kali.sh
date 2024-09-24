#!/bin/bash

GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'

set -e

echo_color() {
    echo -e "${2}${1}${NC}"
}

if ! command -v docker &> /dev/null
then
    echo_color "Docker is not installed. Please install Docker and try again." "$YELLOW"
    exit 1
fi

if ! command -v docker compose &> /dev/null
then
    echo_color "Docker Compose is not installed. Please install Docker Compose and try again." "$YELLOW"
    exit 1
fi

echo_color "Creating shared directory..." "$GREEN"
mkdir -p shared

echo_color "Building Kali Linux image..." "$GREEN"
docker compose build

echo_color "Starting Kali Linux container..." "$GREEN"
docker compose up -d

# Check if the container is running
if [ "$(docker-compose ps -q kali)" ]; then
    echo_color "Kali Linux container is up and running." "$GREEN"
    echo_color "Connecting to the container..." "$GREEN"
    
    # Connect to the container
    docker compose exec kali bash
else
    echo_color "Failed to start Kali Linux container. Please check your Docker Compose configuration." "$YELLOW"
    exit 1
fi