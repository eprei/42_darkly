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

if [[ "$(docker images -q my-kali-linux 2> /dev/null)" == "" ]]; then
    echo_color "Kali Linux image not found. Building..." "$GREEN"
    docker compose build
else
    echo_color "Kali Linux image already exists. Skipping build." "$GREEN"
fi

echo_color "Starting Kali Linux container..." "$GREEN"
docker compose up -d

if [ "$(docker compose ps -q kali)" ]; then
    echo_color "Kali Linux container is up and running." "$GREEN"
    echo_color "Connecting to the container..." "$GREEN"
    
    docker compose exec kali bash
else
    echo_color "Failed to start Kali Linux container. Please check your Docker Compose configuration." "$YELLOW"
    exit 1
fi