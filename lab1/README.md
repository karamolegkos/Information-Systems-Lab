# Lab 1

## Δομή του Μαθήματος
* Εισαγωγή με την Υπηρεσιοστρεφή Αρχιτεκτονική (SOA) και τα Web Services
    * SOA
    * REST & Restful APIs
* Γνωριμία με τη Python 3
    * Γενικές έννοιες
    * Anaconda distribution
* Git
    * GitΗub account
    * Δημιουργία νέου repository
    * Βασικές εντολές

Πολλοί από τους κώδικες του μαθήματος, μπορούν να χρησιμοποιηθούν και απευθείας από το [Google Colab](https://colab.research.google.com/drive/1MYr0KkR8zyxaodZ3XjVDlJJMdpxPRFsk?usp=sharing) του Εργαστηρίου. Στους παρών φακέλους του Lab 1, υπάρχουν επιπλέων παραδείγματα.

## Παραδείγματα Χρήσης Python3
Για να γίνει χρήση της Python3 τοπικά, πρέπει αρχικά να γίνει η σχετική εγκατάσταση.

Για την εξήγηση του τρόπου εκτέλεσης ενός Python Script, θα χρησιμοποιηθεί ο παρακάτω κώδικας ως παράδειγμα. Ο κώδικας είναι αποθηκευμένος σε ένα αρχείο ονομασμένο ως `my_file.py`:
```
# Flask example
from flask import Flask

x = 5 + 5
print(x)
```

Ο παραπάνω κώδικας, εγκαθιστά την βιβλιοθήκη `flask` για να εκτελεστεί. Αν προσπαθήσουμε να εκτελέσουμε το αρχείο με την εντολή `python my_file.py` θα έχουμε το παρακάτω error:
```
Traceback (most recent call last):
  File "C:\Users\pkara\OneDrive\Υπολογιστής\test\my_file.py", line 2, in <module>
    from flask import Flask
ModuleNotFoundError: No module named 'flask'
```

Ο κώδικας δεν εκτελείται, επειδή δεν έχουμε εγκαταστήσει την βιβλιοθήκη flask. Θα πραγματοποιήσουμε την εγκατάσταση, χρησιμοποιώντας ένα Python Virtual Environment. Εκτελούμε στο τερματικό τις παρακάτω εντολές:
```
# Εγκαθιστώ το virtualenv αν δεν υπάρχει
pip install virtualenv

# Κατασκευάζω το Python Virtual Environment
python -m venv my_venv

# Ενεργοποιώ το Python Virtual Environment
# (Για Windows)
.\my_venv\Scripts\activate
# (Για Linux)
my_venv/bin/activate

# Εγκαθιστώ την βιβλιοθήκη flask
pip install flask
```

Τώρα έχω εγκαταστήσει τις απαραίτητες βιβλιοθήκες της `flask` αλλά και την ίδια. Μπορώ να δω τις βιβλιοθήκες γράφοντας `pip freeze` και μπορώ να τις αποθηκεύσω σε ένα αρχείο όλες μαζί γράφοντας `pip freeze > requirements.txt`.

Πλέον μπορώ να εκτελέσω το αρχείο μου γράφοντας το παρακάτω και αναμένω να εμφανιστεί ο αριθμός `10`:
```
python my_file.py
```

Για να βγω από το Python Virtual Environment (Δηλαδή να το απενεργοποιήσω), μπορώ να γράψω το παρακάτω στο τερματικό:
```
# Απενεργοποίηση Virtual Environment
deactivate

# Αν θέλω να το ξαναενεργοποίησω (Windows)
.\my_venv\Scripts\activate
```