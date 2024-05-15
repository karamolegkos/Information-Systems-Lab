# MongoDB

## Γενικά

Σε  αυτό το εργαστήριο γίνεται αναφορά στα παρακάτω:
* Δημιουργία Mongo Docker Container
* Αλληλεπίδραση με το Mongo Shell
* Αλληλεπίδραση με την PyMongo

### Δημιουργία Mongo Docker Container

Για να κάνουμε pull το image από το Docker Hub: 
```
(sudo) docker pull mongo
```
Αν θέλουμε κάποια συγκεκριμένα version μπορούμε να τη κατεβάσουμε έτσι: 
```
(sudo) docker pull mongo:4.0.4 
```
Για να κάνουμε deploy το image για πρώτη φορά:
```
(sudo) docker run -d -p 27017:27017 --name mongodb mongo:4.0.4
```
Για να ξεκινήσουμε πάλι το container
```
(sudo) docker ps -a                 # To get Running Containers
(sudo) docker start mongodb			# To start a container
```
Για να σταματήσουμε το container
```
(sudo) docker stop mongodb
```

### Αλληλεπίδραση με το Mongo Shell

Για να χρησιμοποιήσουμε το mongo shell 
```
(sudo) docker exec -it mongodb mongo
```

Μερικές φορές, μπορεί να έχουμε αρχεία έτοιμα τα οποία να θέλουμε να τα περάσουμε εντός της Βάσης Δεδομένων. Ένα παράδειγμα για να το κάνουμε αυτό είναι το παρακάτω:
```
# Copy from Host Machine inside the Container
(sudo) docker cp students.json mongodb:/students.json

# Provide the Information in MongoDB
(sudo) docker exec -it mongodb mongoimport --db=InfoSys --collection=Students --file=students.json
```

#### Mongo Shell Commands

Οι μαθητές προτείνονται να κάνουν την σχετική μελέτη από τις διαφάνειες του εργαστηρίου.

#### Τελεστές Mongo

Οι μαθητές προτείνονται να κάνουν την σχετική μελέτη από τις διαφάνειες του εργαστηρίου.

### Αλληλεπίδραση με την PyMongo

Οι μαθητές προτείνονται να κάνουν την σχετική μελέτη από τις διαφάνειες του εργαστηρίου.