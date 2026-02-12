# Step to run the application
  docker build -t python-host-log .
  docker images ls
  docker run --name hostlog-cont -d python-host-log
  docker ps
  PS D:\workspace\docker-playground\python-host-log> docker ps
------------------------------------------------------------------------------
    CONTAINER ID   IMAGE             COMMAND           CREATED         STATUS         PORTS      NAMES
    89c73ad285a3   python-host-log   "python app.py"   5 seconds ago   Up 4 seconds   8080/tcp   hostlog-cont
--------------------------------------------------------------------------------
  docker exec -it hostlog-cont /bin/bash 
--------------------------------------------------------------------------------

  D:\workspace\docker-playground\python-host-log> docker exec -it hostlog-cont /bin/bash
root@89c73ad285a3:/app# ls
Dockerfile  README.md  app.py  hostlogs  requirements.txt
 --------------------------------------------------------------------------------

root@89c73ad285a3:/app# cd hostlogs/
root@89c73ad285a3:/app/hostlogs# ls
apphost.log
--------------------------------------------------------------------------------

root@89c73ad285a3:/app/hostlogs# cat apphost.log
2026-02-10 11:45:31,323 - INFO - This is a log entry for host writable layer.
2026-02-10 11:46:01,348 - INFO - This is a log entry for host writable layer.
2026-02-10 11:46:31,374 - INFO - This is a log entry for host writable layer.
2026-02-10 11:47:01,400 - INFO - This is a log entry for host writable layer.
2026-02-10 11:47:31,428 - INFO - This is a log entry for host writable layer.
root@89c73ad285a3:/app/hostlogs#
Navigate to the root folder
cd ..

-------------------------------------------------------------

docker run -d -v /dev/fd:/app/myhostdata python-host-log

D:\workspace\docker-playground\python-host-log>docker ps
CONTAINER ID   IMAGE             COMMAND           CREATED          STATUS          PORTS      NAMES
07287d18cf09   python-host-log   "python app.py"   8 seconds ago    Up 8 seconds    8080/tcp   serene_lichterman
cf8becc8d1a8   python-host-log   "python app.py"   8 minutes ago    Up 8 minutes    8080/tcp   friendly_lehmann
2ca1c3e820bf   ubuntu            "bash"            16 minutes ago   Up 16 minutes              kind_shtern

D:\workspace\docker-playground\python-host-log>docker exec -it 072 sh
# pwd
/app
# ls
Dockerfile  README.md  app.py  hostlogs  myhostdata  requirements.txt
# cd myhostdata
# ls
0  1  2  3
#
------------------------------------------------------

D:\workspace\docker-playground\python-host-log>docker run -d -v /app/hostlogs:/app/myhostdata python-host-log
b2d7a515bd7d2780f4cded75b6c8d3056e80b18e44c32d40a273d744d30e740c

D:\workspace\docker-playground\python-host-log>docker ps
CONTAINER ID   IMAGE             COMMAND           CREATED          STATUS          PORTS      NAMES
b2d7a515bd7d   python-host-log   "python app.py"   5 seconds ago    Up 4 seconds    8080/tcp   boring_ellis
07287d18cf09   python-host-log   "python app.py"   7 minutes ago    Up 7 minutes    8080/tcp   serene_lichterman
cf8becc8d1a8   python-host-log   "python app.py"   15 minutes ago   Up 15 minutes   8080/tcp   friendly_lehmann
2ca1c3e820bf   ubuntu            "bash"            23 minutes ago   Up 23 minutes              kind_shtern
 
D:\workspace\docker-playground\python-host-log>docker exec -it b2d sh
# ls
Dockerfile  README.md  app.py  hostlogs  myhostdata  requirements.txt
# cd myhostdata
# ls
app.log
# exit
