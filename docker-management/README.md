# Docker Management

Το Docker είναι ένα εργαλείο για Containerization των εφαρμογών μας. Είναι καλό να γνωρίζουμε τα παρακάτω:
- Docker Engine: Το Docker Engine είναι το εργαλείο με το οποίο μπορούμε να πραγματοποιήσουμε containerization.
- Docker Desktop: Ένα GUI περιβάλλον που μπορούμε να εγκαταστήσουμε για να διευκολύνουμε την διαχείριση του Docker Engine.
- [DockerHub](https://hub.docker.com/): Το DockerHub αποτελεί ένα αποθετήριο εικόνων. Εκεί βρίσκονται διάφορα ήδη έτοιμα images τα οποία μπορούμε να χρησιμοποιούμε. Εκεί επίσης μπορούμε να ανεβάζουμε και δικά μας Images.

## Installation

Για να κάνουμε install το Docker Desktop, ακολουθούμε τα παρακάτω guides:
- [Docker Desktop for Windows](https://docs.docker.com/desktop/install/windows-install/)
- [Docker Desktopfor Linux](https://docs.docker.com/desktop/install/linux-install/)
- [Docker Desktopfor Mac](https://docs.docker.com/desktop/install/mac-install/)

Παρακάτω δίνεται μία επιπλέων βοήθεια για χρήστες Ubuntu. Μπορείτε να εγκαταστήσετε το Docker χωρίς το Docker Desktop κάνοντας το παρακάτω:
```
# Add Docker's official GPG key:
sudo apt-get update
sudo apt-get install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

# Add the repository to Apt sources (Copy and Paste this all together):
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

# Update again
sudo apt-get update
```

## Docker Commands

Από την στιγμή που έχουμε εγκαταστήσει το Docker Engine, μπορούμε στο τερματικό του υπολογιστή μας να χρησιμοποιούμε τα παρακάτω commands. Προσοχή, οι Linux users πρέπει να ξεκινάνε τις εντολές τους με `sudo`.

| Command               | Λειτουργία                                                                                |
| --------------------- | ----------------------------------------------------------------------------------------- |
| docker images         | Λίστα με όλα τα images που έχουμε                                                         |
| docker ps -a          | Λίστα με όλα τα containers που είναι ενεργά                                               |
| docker run _name_     | Δημιουργία και εκτέλεση container (Αν δεν υπάρχει το image τοπικά, γίνεται και κατέβασμα) |
| docker exec _name_    | Εκτέλεση εντολών μέσα σε ένα container                                                    |
| docker stop _name_    | Σταμάτημα ενός ενεργού container                                                          |
| docker rm _name_      | Αφαίρεση ενός σταματημένου container                                                      |
| docker rmi _name_     | Διαγραφή ενός image από τον υπολογιστή (πρώτα να είναι σταματημένο το container)          |
| docker inspect _name_ | Εμφάνιση low-level πληροφοριών για ένα container                                          |
| docker logs _name_    | Εμφάνιση των logs                                                                         |
| docker build .        | Κατασκευή image από το current directory                                                  |
| docker pull _name_    | Κατέβασμα τοπικά του image                                                                |
| docker push _name_    | Ανέβασμα του image σε κάποιο απομακρυσμένο image repository (By Default DockerHub)        |

## Build a Docker Image

Για την κατασκευή ενός Docker Image, όπως έχει προαναφερθεί, μπορούμε να χρησιμοποιούμε την εντολή `docker build .` (Προσοχή στην τελεία ".").

Στην περίπτωση που το Dockerfile του image μας βρίσκεται στον ίδιο κατάλογο είναι αρκετή η παρακάτω εντολή:
```
docker build .
```

Στην περίπτωση που θέλουμε και απευθείας να δώσουμε ένα όνομα στο image, μπορούμε να εκτελέσουμε το παρακάτω:
```
docker build --tag <image_name> .
```

## Upload Image to DockerHub

Παρακάτω δίνεται παράδειγμα του τρόπου με τον οποίο μπορούμε να ανεβάσουμε ένα image μας στο DockerHub.

Έστω ότι είμαστε ο DockerHub user με όνομα sonem και έχουμε ένα image με όνομα my-test-image, το οποίο έχουμε κατασκευάσει τοπικά και θέλουμε να ανεβάσουμε στο DockerHub.

Για να το κάνουμε αυτό πρέπει να εκτελέσουμε τα παρακάτω:
```
# Connect the local Docker Engine with our DockerHub account
# docker login -u <user_name>
docker login -u sonem
# Input password

# Provide an apropriate name for your user
# docker 
# docker tag image_name <user_name>/<image_name>
docker tag my-test-image sonem/my-test-image

# Push the image to DockerHub
# docker push <user_name>/<image_name>
docker push sonem/my-test-image
```
Ουσιαστικά, με την εντολή `docker login` συνδεόμαστε με τον λογαριασμό μας στο DockerHub. Στην συνέχεια με την εντολή `docker tag` μετονομάζουμε το image μας με τρόπο κατανοητό από το Docker Engine όσο αφορά το μέρος στο οποίο το image πρέπει να ανέβει (δηλαδή σε ποιο απομακρυσμένο image repository ανήκει). Τελικά, με το `docker push` ανεβάζουμε το image.

Για να ξανακατεβάσουμε το image μας αρκεί να γράψουμε την παρακάτω εντολή:
```
# docker pull <user_name>/<image_name>
docker pull sonem/my-test-image
```