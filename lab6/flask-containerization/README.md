# Τρόπος Εκτέλεσης

## Prerequisites
- Docker Engine
  - `docker pull mongo:8.0.5`
- Python
  - `pip install virtualenv`

## Κατασκευή Mongo DBMS

Ανοίγουμε ένα τερματικό και γράφουμε την παρακάτω εντολή για να σηκώσουμε ένα Mongo DBMS:
```shell
docker run -d -p 27017:27017 --name my-mongo mongo:8.0.5
```

## Κατασκευή requirements.txt Αρχείου
Για την κατασκευή του `requirements.txt` αρκεί να χτίσουμε ένα Python Virtual Environment και στην συνέχεια, αφού το κάνουμε `activate`, να προχωρήσουμε στο να κάνουμε `pip install <lib>` τις βιβλιοθήκες του.

Κατασκευάζουμε το Python Virtual Environment και το ονομάζουμε `venv`:
```shell
python -m venv venv
```

Συνεχίζοντας, το ενεργοποιούμε:
```shell
# (Για Windows)
.\venv\Scripts\activate
# (Για Linux)
source venv/bin/activate
```

Κάνουμε install τις αναγκαίες βιβλιοθήκες του κώδικα:
```shell
pip install flask
pip install pymongo
```

Πριν κατασκευάσουμε το ένα Docker Image πάντα πρέπει να έχουμε ένα `requirements.txt` αρχείο, το οποίο πλέον μπορούμε να κατασκευάσουμε με τον παρακάτω τρόπο. Ουσιαστικά, εμφανίζουμε τις εγκατεστημένες βιβλιοθήκες του Python Virtual Environment και το output το εισάγουμε σε ένα txt αρχείο.
```shell
pip freeze > requirements.txt
``` 

Πλέον μπορείτε να βγείτε από το `venv` το οποίο κατασκευάσατε και να το διαγράψετε:
```shell
deactivate
rm -rf venv
```

## Κατασκευή Docker Image & Container
Χρησιμοποιούμε το παρακάτω command για να κατασκευάσουμε το Docker Image του API Server μας:
```shell
docker build --tag my-server:1.0.0 .
```

Χρησιμοποιούμε το παρακάτω command για να κατασκευάσουμε ένα image από το `my-server:1.0.0` image το οποίο χτίσαμε προηγουμένως:
```shell
# Windows (Copy it all together)
docker run -d -p 5000:5000 ^
--name my-server-container ^
--env SERVER_HOST="0.0.0.0" ^
--env MONGO_HOST="host.docker.internal" ^
--env MONGO_DATABASE="TEST_DATABASE" ^
my-server:1.0.0

# Linux (Copy it all together)
docker run -d -p 5000:5000 \
--name my-server-container \
--env SERVER_HOST="0.0.0.0" \
--env MONGO_HOST="host.docker.internal" \
--env MONGO_DATABASE="TEST_DATABASE" \
my-server:1.0.0
```

**Σημείωση**: Δίνουμε ως Environment Variable ότι ο SERVER_HOST θα τρέχει στο `0.0.0.0` με σκοπό εσωτερικά στο container να γίνεται εμφανής ο Server σε όλα τα δίκτυα του container. Τελικά ζητάμε από το Docker να δώσει πρόσβαση στο port `5000` του host PC (σε εμάς δηλαδή), στο εσωτερικό διαθέσιμο `5000` SERVER_PORT.

## Πρόσβαση στην Υπηρεσία

Χρησιμοποιείστε τον browser σας και μεταβείτε στην παρακάτω διεύθυνση για να αποκτήσετε πρόσβαση στο UI του server σας:
```
localhost:5000
```

## Πως Σταματάω τον Κώδικα?
Για να διαγράψετε το container του API Server: `docker rm -f my-server-container`.

Για να διαγράψετε το container του Mongo DBMS: `docker rm -f my-mongo`.