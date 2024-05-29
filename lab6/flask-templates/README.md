# Τρόπος Εκτέλεσης

Παρακάτω δίνεται ο τρόπος εκτέλεσης του κώδικα με την χρήση ενός Python Virtual Environment.

## Python Virtual Envrionment

Αρχικά εγκαθιστούμε το Python Virtual Environment στην περίπτωση που δεν το έχουμε ήδη:
```shell
pip install virtualenv
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