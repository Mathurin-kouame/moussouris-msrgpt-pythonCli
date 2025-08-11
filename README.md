# MSGPT-Python_Cli
Un outil en ligne decommande permettant aux utilisateurs d'envoyer des prompts
spécialisés pour interagir avec un shell intelligent.
Chaque utlisateur dispose de 5 prompts maxmum par jour.
 
##  Fonctionnalités

-  Enregistrement et authentification utilisateur
-  Envoi de prompts structurés avec différentes options
-  Gestion des sessions (connexion / déconnexion)
-  Options disponibles : scan, enum, footprint


##  Installation
- Clonez ce dépôt.

- Le fichier requirements.txt contient les détails sur les dépendances à installer et la version minimale à utiliser :
  - requests>=2.32.4  
  - rich>=14.0.0 
  
Commande: pip install -r requirements.txt (nom du fichier) pour installer automatiquement les dependances

##  Configuration du PATH
  export PATH="/media/sf_formation_MOUSSOURIS/Moussourisgpt-backend/mousourisgpt-PythonCli:$PATH" 
/media/sf_formation_MOUSSOURIS/Moussourisgpt-backend/mousourisgpt-PythonCli: répresente emplacement de mon repertoire

Rechargez votre shell :

### Pour ZSH 
    source ~/.zshrc
    
### Pour BASH 
    source ~/.bashrc

##  Mode d'utilisation

### Créer un compte 
    msgpt register

### Se connecter 
    msgpt login

### Se déconnecter :
    msgpt logout

 Envoyer un prompt :

msgpt run -o "option" -p "prompt"

## Options possibles:

scan : pour analyser un réseau

enum : pour faire de l’énumération

footprint : pour  recueillir des données précieuses sur l'infrastructure, les technologies utilisées.

## Exemples d'utilisation

### Scanner un réseau :
    msgpt run -o "scan" -p "scanne le réseau 192.168.1.0"

### Enumération de ports :
    msgpt run -o "enum" -p "énumère les ports ouverts sur l’hôte 10.0.0.5"

### Profiling système :
    msgpt run -o "footprint" -p "récupère les informations système de la machine cible"

##  Portabilité & Open Source

-  Ce projet est open source : tu peux l’utiliser, le modifier et le redistribuer librement.
- 💻 Compatible Linux et macOS : MSGPT-Python-CLI fonctionne nativement sur les systèmes Unix-like.  
  >  Le support pour Windows n’est pas concerné.

