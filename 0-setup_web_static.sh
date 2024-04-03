#!/usr/bin/env bash
# This script sets up your web servers for the deployment of web_static

# Install Nginx if not already installed
if ! command -v nginx &> /dev/null; then
    sudo apt-get -y update
    sudo apt-get -y install nginx
fi

# Create necessary directories if they don't exist
sudo mkdir -p /data/web_static/releases/test /data/web_static/shared

# Create a fake HTML file for testing
sudo bash -c 'cat > /data/web_static/releases/test/index.html << EOF
<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>
EOF'

# Create symbolic link
sudo unlink /data/web_static/current
sudo ln -sf /data/web_static/releases/test /data/web_static/current

# Set ownership to ubuntu user and group recursively
sudo chown -R ubuntu:ubuntu /data/

# Update Nginx configuration
sudo sed -i "s|location / {|\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}\n\n\tlocation / {|" /etc/nginx/sites-available/default

# Restart Nginx
sudo service nginx restart
