# Description

Le programme est un annuaire de contact écrit en langage python et la librairie "Qt". 

# Fonctionnalités

## Import/Export

Le programme permet l'ajout, l'édition et la suppression de contacts dans un annuaire.

Au chargement, l'annuaire charge les contacts enregistrés dans le fichier ```"contact.json"``` à la racine du projet.

Les modifications de l'annuaire peuvent êtres sauvegardées dans le fichier ```"contact.json"``` grâce à la fonctionnalité ```"Enregistrer"```.

L'annuaire peut être exporté au format JSON à la destination souhaitée grâce à la fonctionnalité ```"Enregistrer sous ..."```

Il est possible d'importer un nouvel annuaire à partir d'un fichier JSON, ceci charge les contacts du nouvel annuaire mais n'écrase pas le fichier ```"contact.json"```.

Il n'est pas possible d'enregistrer 2 contacts sous le même numéro de téléphone, une erreur sera affichée le cas échéant.
## Tri du tableau

Il est possible de rechercher des contacts par propriétés grâce à une saisie dans une barre de recherche.

Il est possible de trier les contacts par caractéristiques croissante ou décroissante en cliquant sur l'en-tête de la colonne correspondante.

## Choix du langage

L'interface peut être affichée en plusieurs langues :

- Français
- Anglais
- Singe
- Pioupiou

# Structure
- Model
    > Contacts : Représente un contact dans l'annuaire
    >> Nom  
    >> Prénom  
    >> Département    
    >> Numéro de téléphone  
    >> Email  
    >> Favoris  

    > Directory : Représente l'annuaire
    >> Liste de contacts
- View
    > Fenêtre principale

    > Formulaires : Les formulaires d'ajout et d'édition de contacts héritent d'une classe ```"ContactForm"``` 
- Controller
    > ContactController

    > DirectoryController

# Auteurs

Corentin BOLLAERT-LUCIANI  
Quentin ROBARD
 