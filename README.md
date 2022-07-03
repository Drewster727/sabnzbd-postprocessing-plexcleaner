# sabnzbd-postprocessing-plexcleaner

update docker.sock permissions:
```
sudo chmod 666 /var/run/docker.sock
```

Used in coordination wtith:
https://github.com/Drewster727/sabnzbd-docker

docker-compose example (docker.sock access is needed):
```
sabnzbd:
    image: drewster727/sabnzbd-docker:3.6.0
    container_name: sabnzbd
    environment:
      - PUID=1000
      - PGID=1000
      - TZ=America/Chicago
    volumes:
      - /opt/containers/sabnzbd/config:/config
      - /opt/containers/sabnzbd/sabnzbd_scripts:/scripts
      - /opt/plexcleaner:/plexcleaner
      - /data/sabnzbd/incomplete:/incomplete-downloads
      - tower-storage:/media/tower/Storage
      - /var/run/docker.sock:/var/run/docker.sock
```
