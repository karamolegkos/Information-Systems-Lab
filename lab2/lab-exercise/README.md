# First Docker Image Exercise

Μπορείτε να ακολουθήσετε τον παρακάτω οδηγό για να κατασκευάσετε ένα δικό σας Docker Image.

## Prerequisites

Πρέπει να έχετε εγκατεστημένα:
- Docker Engine / Docker Desktop
- Python3

### Κατασκευή και Έλεγχος Python Αρχείου

Αρχικά πρέπει να κατασκευάσουμε τον κώδικα που θέλουμε να χρησιμοποιήσουμε αλλά και να εξάγουμε τις σχετικές του βιβλιοθήκες. Χρησιμοποιήστε το αρχείο `exercise.py` το οποίο βρίσκεται σε αυτόν τον φάκελο. Κατεβάστε το και αφήστε το εντός ενός φακέλου τοπικά (έστω ο φάκελος είναι στο path `/test`).

Δοκιμάστε να εκτελέσετε το αρχείο γράφοντας την παρακάτω εντολή σε ένα τερματικό:
```
python exercise.py
```
Θα παρατηρήσετε πως θα εμφανιστεί το παρακάτω error, καθώς σας εξηγείται πως δεν έχετε εγκαταστήσει την βιβλιοθήκη `requests`.
```
Traceback (most recent call last):
  File "C:\Users\pkara\OneDrive\Υπολογιστής\test\exercise.py", line 1, in <module>
    import requests, time
    ^^^^^^^^^^^^^^^^^^^^^
ModuleNotFoundError: No module named 'requests'
```

Θα γίνει χρήση ενός Python Virtual Environment για την κατασκευή εγκατάσταση την διαχείριση των αναγκαίων βιβλιοθηκών του Python script. Αρχικά ελέγξτε αν έχετε εγκατεστημένο το σχετικό packet manager:
```
pip install virtualenv
```
Στην συνέχεια, κατασκευάστε και ενεργοποιήστε το Python Virtual Environment:
```
python -m venv my_venv

# (Για Windows)
.\my_venv\Scripts\activate
# (Για Linux)
source my_venv/bin/activate
```

Συνεχίζοντας εγκαταστήστε πλέον την βιβλιοθήκη `requests`.
```
pip install requests
```

Μόλις ολοκληρωθεί η διαδικασία, θα παρατηρήσετε πως το παρακάτω command εκτελεί πλέον τον κώδικά και φέρνει δεδομένα από ένα απομακρυσμένο API:
```
python exercise.py
```

Ο κώδικας είναι έτοιμος. Αποθηκεύστε τις βιβλιοθήκες σε ένα αρχείο με όνομα `requirements.txt`:
```
pip freeze > requirements.txt
deactivate
```

Πλέον ο φάκελος (με όνομε `my_venv`) που κρατάει τις βιβλιοθήκες του Python Virtual Environment είναι άχρηστος. Μπορείτε να τον διαγράψετε.

### Κατασκευή Image

Το `Dockerfile` είναι οι οδηγίες με τις οποίες κατασκευάζουμε ένα Docker Image. Ξεκινήστε κατεβάζοντας στον ίδιο φάκελο που έχετε και το script σας, το παρών Dockerfile αυτού του repo. Το παρών αρχείο είναι ήδη γραμμένο, αλλά εσείς θα πρέπει να γνωρίζετε πως να φτιάχνετε δικά σας Dockerfiles, οπότε μελετήστε τις εντολές που εκτελεί.

Αφού έχετε τα αρχεία: `exercise.py`, `Dockerfile` και `requirements.txt` έτοιμα, μπορείτε να κατασκευάσετε το image σας με το παρακάτω command. (Στην περίπτωση που δεν γίνεται εκτέλεση του παρακάτω, σιγουρευτείτε ότι τρέχει στο background το Docker Engine).
```
# Use sudo if you are not in docker-users groups
docker build -t my-first-image .
```

### Διαχείριση Container

Πλέον έχετε κατασκευάσει ένα Docker Image. Μπορείτε να το δείτε γράφοντας `docker images`.
Κατασκευάστε ένα Docker Container από το Docker Image εκτελώντας την παρακάτω εντολή:
```
docker run -d --name my-first-container my-first-image
```

Παραπάνω:
1. Το `docker run` είναι ουσιαστικά το "deployment" ενός container.
2. ΤΟ flag `-d` σημαίνει detached και συνεπώς κάνει το container να τρέχει στο background. Δοκιμάστε να κάνετε το ίδιο χωρίς το flag αυτό.
3. Το `--name my-first-container` είναι το όνομα που θα δώσουμε στο container.
4. Η τελευταία παράμετρος είναι το όνομα του image.

Μπορείτε να δείτε το container που εκτελείτε γράφοντας:
```
docker ps -a
```

Μπορείτε να το διαγράψετε γράφοντας:
```
docker stop my-first-container
docker rm my-first-container
```

### Docker Hub Upload

Για να ανεβάσετε την εικόνα που φτιάξατε στο Docker Hub αρκεί να γράψετε τα παρακάτω, υποθέτοντας πως το username σας είναι _sonem_
```
# Connect the local Docker Engine with our DockerHub account
# docker login -u <user_name>
docker login -u sonem
# Input password

# Provide an apropriate name for your user
# docker 
# docker tag image_name <user_name>/<image_name>
docker tag my-first-image sonem/my-first-image

# Push the image to DockerHub
# docker push <user_name>/<image_name>
docker push sonem/my-first-image
```