# csv

### Debug-run
1. `pip3 install -r requirements.txt`
2. `python3 app.py`


## Deploy-server
1. Install Dependencies \
  `sudo apt-get update` \
  `sudo apt install python3-pip python3-dev python3-venv nginx`
  
2. Python Virtual Enviroment \
  `python3 -m venv env` \
  `source env/bin/activate` 
  
3. Python dependencies \
  `pip3 install r- dependencies.txt` 
  
4. Test Gunicorn(Optional) \
  `gunicorn --bind 0.0.0.0:5000 wsgi:app` \
  view app at *http://localhost:5000* \
  controll C to exit
  
5. Create WSGI Socket
   `gunicorn --workers 3 --bind unix:/home/movieapp/app.sock -m 777 wsgi:app
  
6. Configure NGINX \
  - `ls /etc/nginx/` \
  - nano /etc/nginx/sites-available/app \
  - ```
    server {
      listen 80;
 
      location / {
        include proxy_params;
        proxy_pass http://unix:/(Directory)/app.sock;
      }  
    }
    ```
  



  

  
  
