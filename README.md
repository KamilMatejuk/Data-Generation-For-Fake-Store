**Note** Data created using [Faker](https://faker.readthedocs.io/en/master/)


## Install oracle database ???
https://docs.oracle.com/en/database/oracle/oracle-database/21/deeck/index.html
```
docker rm -f database; docker run -d \
    --name database \
    -e ORACLE_SID=service \
    -e ORACLE_PWD=password \
    -e ORACLE_PASSWORD=password \
    -p 1521:1521 -p 5500:5500 \
    -v scripts:/opt/oracle/scripts/setup \
    gvenzl/oracle-xe:21-full
```
## Enter database SQL cli
```
docker exec -it database sqlplus /
```
## Setup connection in generate.py and run
```
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt
python3 generate.py
```
