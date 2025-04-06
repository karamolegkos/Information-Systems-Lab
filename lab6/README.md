# Lab 6

## Περιεχόμενα

- [Flask Templates](flask-templates)
- [Flask Templates + Mongo](flask-templates-mongo)
- [Flask Containerization](flask-containerization)
- [Docker Compose + Flask](flask-compose)
- [Docker Compose + Flask + Startup Data](compose-with-data)
- Jinja (Δείτε Παρακάτω)

## Jinja
Η Jinja, είναι μία μηχανή κατασκευής template η οποία συνδέεται εύκολα με το Flask.

Παρακάτω διατίθενται παραδείγματα της Jinja, αν θέλετε παραπάνω παραδείγματα και να αποκτήσετε μία ποιο βαθιά γνώση επάνω σε αυτήν, αναφερθείτε στο σχετικό [documentation](https://jinja.palletsprojects.com/en/3.1.x/).

### Εμφάνιση Τιμών
Στην περίπτωση που έχετε μία μεταβλητή με όνομα `NAME = "John"`, μπορείτε εντός ενός template να χρησιμοποιήσετε την παρακάτω συγγραφή για να εμφανίσετε την τιμή:
```jinja
Hello {{ NAME }}
```
Στην οθόνη του χρήστη, θα εμφανιστεί το παρακάτω:
```
Hello John
```

### Πράξεις
Παρακάτω γίνεται ένα παράδειγμα χρήσης πράξεων σε μεταβλητές στις οποίες έχουμε βάλει παραδειγματικά τις τιμές: `X = 7` και `Y = 11`.
```jinja
Adding {{ X }} and {{ Y }} equals {{ X + Y }}
```
Στην οθόνη του χρήστη, θα εμφανιστεί το παρακάτω:
```
Adding 7 and 11 equals 18
```

### Σχόλια
Μπορούμε να εισάγουμε σχόλια, χρησιμοποιώντας το παρακάτω συντακτικό:
```jinja
{# This is an example of a comment #}
Hello {{ NAME }}
```
Στην οθόνη του χρήστη, θα εμφανιστεί το παρακάτω:
```
Hello John
```

### Φίλτρα
Η Jinja επιτρέπει επίσης την χρήση φίλτρων. Παρακάτω δίνεται ένα παράδειγμα. Αν επιθυμείτε να μάθετε περισσότερα, αναφερθείτε στο σχετικό [documentation](https://jinja.palletsprojects.com/en/3.0.x/templates/#id11).

Έστω η μεταβλητή `GREETING = "Hello"`. Μπορούμε να χρησιμοποιήσουμε τα δύο παρακάτω φίλτρα για να την επεξεργαστούμε:
```jinja
{{ GREETING | upper }}
{{ GREETING | lower }}
```
Στην οθόνη του χρήστη, θα εμφανιστεί το παρακάτω:
```
HELLO
hello
```

### Δομή Επιλογής
Μπορούμε να κάνουμε τα templates μας δυναμικά, με την χρήση Δομών Επιλογής και Επανάληψης. **Προσοχή**: Οι εντολές αυτές, επιλέγουν πρακτικά το <u>content</u> το οποίο θα εμφανιστεί στον χρήστη.

Έστω η μεταβλητή `GENDER = "Female"`. Παρακάτω εμφανίζεται ένα παράδειγμα της χρήσης Δομής Επιλογής.
```jinja
{% if GENDER == 'Male' %}
  Hello Sir
{% elif GENDER == 'Female' %}
  Hello Madam
{% else %}
  Hello
{% endif %}
```
Στην οθόνη του χρήστη, θα εμφανιστεί το παρακάτω:
```
Hello Madam
```

### Λογικοί Τελεστές
Για να εφαρμόσουμε Λογικού Τελεστές, αρκεί απλά να χρησιμοποιήσουμε τα λεκτικά `and`, `or`, `not`.

Παραδειγματικά, στην περίπτωση που έχουμε τις μεταβλητές: `AGE = 16` και `GENDER = "Male"`:
```jinja
{% if GENDER == 'Male' and AGE >= 18 %}
  Hello Sir
{% elif GENDER == 'Female' and AGE >= 18 %}
  Hello Madam
{% else %}
  Hello
{% endif %}
```
Στην οθόνη του χρήστη, θα εμφανιστεί το παρακάτω:
```
Hello
```

### Δομές Επανάληψης (For)
Έστω πως θέλουμε να κατασκευάσουμε ένα ένα template το οποίο εμφανίζει όλα τα ονόματα στην παρακάτω λίστα:
```python
NAMES = ["Melinda", "Thomas", "Zac"]
```

Μπορούμε να επαναλάβουμε το περιεχόμενο που εμφανίζεται στο template που χρησιμοποιούμε με τον παρακάτω τρόπο:
```jinja
{% for name in NAMES %}
  Hello {{ name }}
{% endfor %}
```
Στην οθόνη του χρήστη, θα εμφανιστεί το παρακάτω:
```
Hello Melinda
Hello Thomas
Hello Zac
```

### Χρήση Dictionaries

Έστω η παρακάτω Pyhton λίστα από Dictionaries:
```python
EMPLOYEES = [
  {
    "name": "Melinda",
    "age": 25,
    "gender": "Female"
  },
  {
    "name": "Natalie",
    "age": 42,
    "gender": "Female"
  },
  {
    "name": "Madison",
    "age": 30,
    "gender": "Female"
  }
]
```

Μπορούμε να κατασκευάσουμε ένα template το οποίο εμφανίζει όλους μας τους υπαλλήλους χρησιμοποιώντας το παρακάτω παράδειγμα:
```jinja
+------------------------+
|    Employee Details    |
+---------+-----+--------+
| Name    | Age | Gender |
+---------+-----+--------+
{% for EMPLOYEE in EMPLOYEES %}
| {{ EMPLOYEE.name }} | {{ EMPLOYEE.age }}  | {{ EMPLOYEE.gender }} |
{% endfor %}
+---------+-----+--------+
```
Στην οθόνη του χρήστη, θα εμφανιστεί το παρακάτω:
```
+------------------------+
|    Employee Details    |
+---------+-----+--------+
| Name    | Age | Gender |
+---------+-----+--------+
| Melinda | 25  | Female |
| Natalie | 42  | Female |
| Madison | 30  | Female |
+---------+-----+--------+
```

### Αναφορές
- Για τον παραπάνω οδηγό, μεταφράστηκε αυτό το [post](https://ultraconfig.com.au/blog/jinja2-a-crash-course-for-beginners/).