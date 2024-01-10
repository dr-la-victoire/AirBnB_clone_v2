#!/usr/bin/env bash
# This script sets up the web servers for the deployment of web_static

# install nginx if not already installed
sudo apt-get update
sudo apt-get install -y nginx
sudo ufw allow "Nginx HTTP"

# creating the folders
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/

# creating the fake HTML file for testing
sudo touch /data/web_static/releases/test/index.html

# putting fake content into the file
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html

# creating the symlink
# if it exists, it's deleted and recreated each time script is run
target="/data/web_static/releases/test/"
link="/data/web_static/current"
if [ -e "$link" ]; then
	rm "$link"
fi

sudo ln -s -f "$target" "$link"

# giving ownership of the folder to a user and group
sudo chown -R ubuntu:ubuntu /data/

# updating the nginx conf to serve the content of /./current to hbnb_static
echo "location /hbnb_static {
	alias /data/web_static/current/;
}" | sudo tee -a /etc/nginx/sites-enabled/default > /dev/null 

# restarting nginx
sudo service restart nginx
