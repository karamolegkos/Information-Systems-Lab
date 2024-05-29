# Τρόπος Εκτέλεσης

## Prerequisites
- Docker Engine
  - `docker pull mongo:7.0.9`
- Python
  - `pip install virtualenv`

## Κατασκευή Mongo DBMS

Ανοίγουμε ένα τερματικό και γράφουμε την παρακάτω εντολή για να σηκώσουμε ένα Mongo DBMS:
```shell
docker run -d -p 27017:27017 --name my-mongo mongo:7.0.9
```

## Εκτέλεση του Κώδικα
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

Χρησιμοποιούμε το παρακάτω `requirements.txt` αρχείο για να εγκαταστήσουμε τις βιβλιοθήκες του `server.py`:
```shell
pip install -r requirements.txt
```

Εκτελούμαι των κώδικα:
```shell
python server.py
```

## Πρόσβαση στην Υπηρεσία

Χρησιμοποιείστε τον browser σας και μεταβείτε στην παρακάτω διεύθυνση για να αποκτήσετε πρόσβαση στο UI του server σας:
```
localhost:5000
```

## Πως Σταματάω τον Κώδικα?

Για να σταματήσετε την εκτέλεση του κώδικά σας, αρκεί να πατήσετε `CTRL + C` εντός του terminal στο οποίο εκτελείτε των server σας.

Για να σταματήσετε το Virtual Environment, γράφετε το παρακάτω στο terminal σας:
```
deactivate
```

Για να διαγράψετε το Virtual Environment ακρεί να διαγράψετε τον φάκελο `venv`.

Για να διαγράψετε το container το οποίο κατακσευάσατε: `docker rm -f my-mongo`