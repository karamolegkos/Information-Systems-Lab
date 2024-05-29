# Τρόπος Εκτέλεσης

## Prerequisites
- Docker Engine
  - For Linux Users you need to write the follow command:
```shell
sudo apt-get -y install docker-compose
```

## Εγκατάσταση
Για να εγκαταστήσουμε το Πληροφοριακό Σύστημα, αρκεί να βάλουμε το περιεχόμενο του `flask-containerization` project εντός του `/flask-server` φακέλου.

Στην συνέχεια, μπορούμε να χρησιμοποιήσουμε την επόμενη εντολή για να σηκώσουμε όλο μας το σύστημα:
```shell
docker compose up -d
```

## Απεγκατάσταση

Μπορούμε πλέον να απεγκαταστήσουμε όλο το Πληροφοριακό μας Σύστημα, χρησιμοποιώντας την παρακάτω εντολή:
```shell
docker rm -f my-server-container my-mongo
```