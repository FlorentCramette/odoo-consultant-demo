# 🚀 Guide d'Installation Rapide - Odoo Consultant Demo

## Prérequis

### Logiciels nécessaires
- ✅ **Docker Desktop** : [Télécharger](https://www.docker.com/products/docker-desktop/)
  - Windows : Docker Desktop for Windows
  - Minimum 4 GB RAM alloués à Docker
- ✅ **Git** : [Télécharger](https://git-scm.com/downloads)
- ✅ **VS Code** (optionnel) : [Télécharger](https://code.visualstudio.com/)

### Vérification installation
```powershell
# PowerShell (Windows)
docker --version
# Docker version 24.0.0 ou supérieur

docker-compose --version
# Docker Compose version v2.20.0 ou supérieur

git --version
# git version 2.40.0 ou supérieur
```

---

## Installation en 5 étapes

### Étape 1 : Cloner le repository

```powershell
# Ouvrir PowerShell
cd C:\Users\flore\Desktop

# Cloner le projet (si déjà sur GitHub)
git clone https://github.com/votre-username/odoo-consultant-demo.git

# Ou utiliser le dossier existant
cd odoo-consultant-demo
```

### Étape 2 : Lancer Docker Compose

```powershell
# Aller dans le dossier configuration
cd configuration

# Lancer les conteneurs (première fois : télécharge images ~2 GB)
docker-compose up -d

# Vérifier que les conteneurs sont démarrés
docker-compose ps
```

**Résultat attendu** :
```
NAME                COMMAND                  STATUS              PORTS
odoo_app           "/entrypoint.sh odoo"    Up 2 minutes       0.0.0.0:8069->8069/tcp
odoo_db            "docker-entrypoint.s…"   Up 2 minutes       0.0.0.0:5432->5432/tcp
odoo_pgadmin       "/entrypoint.sh"         Up 2 minutes       0.0.0.0:8080->80/tcp
```

### Étape 3 : Accéder à Odoo

1. **Ouvrir navigateur** : http://localhost:8069

2. **Créer base de données** (première utilisation)
   - Cliquer "Créer une base de données"
   - Nom base : `odoo_demo`
   - Email : `admin@example.com`
   - Password : `admin`
   - Langue : Français
   - Pays : France
   - Démo data : ☑️ Charger données de démonstration
   - Cliquer "Créer une base de données"

3. **Patienter** (2-3 minutes)
   - Installation des modules de base
   - Chargement des données

4. **Connexion**
   - Login : `admin@example.com`
   - Password : `admin`

### Étape 4 : Activer mode développeur

```
1. Paramètres (icône ⚙️ en haut à droite)
2. En bas : "Activer le mode développeur"
3. Ou directement : http://localhost:8069/web?debug=1
```

### Étape 5 : Installer le module custom

```
1. Apps (menu principal)
2. Cliquer sur ⋮ (trois points) > "Mettre à jour la liste des Apps"
3. Confirmer "Mettre à jour"
4. Rechercher "Project Service Pro"
5. Cliquer "Installer"
6. Patienter (1-2 min)
```

**✅ Installation terminée !**

---

## Configuration initiale

### 1. Installer modules dépendants

Si pas déjà installés, installer dans cet ordre :
```
1. CRM
2. Ventes
3. Projet
4. Feuilles de temps
5. Comptabilité
```

**Raccourci** : Tous ces modules s'installent automatiquement avec "Project Service Pro".

### 2. Configurer les utilisateurs

#### Créer utilisateurs de test

**Commercial** :
```
Paramètres > Utilisateurs > Créer
- Nom : Jean Commercial
- Email : commercial@techservices.pro
- Droits : Ventes > Utilisateur: Gérer son propre pipeline uniquement
```

**Chef de Projet** :
```
Paramètres > Utilisateurs > Créer
- Nom : Marie Chef Projet
- Email : chef.projet@techservices.pro
- Droits : 
  - Projet > Utilisateur
  - Feuilles de temps > Utilisateur
```

**Consultant** :
```
Paramètres > Utilisateurs > Créer
- Nom : Paul Consultant
- Email : consultant@techservices.pro
- Droits : 
  - Feuilles de temps > Utilisateur
  - Projet > Utilisateur (lecture seule)
```

### 3. Configurer les produits/services

**Créer service "Consultation IT"** :
```
Ventes > Produits > Créer
- Nom : Consultation IT
- Type : Service
- Politique de facturation : Basé sur les feuilles de temps
- Prix de vente : 600 € (TJM moyen)
- Coût : 400 € (coût interne)
- ☑️ Peut être vendu
- ☑️ Peut être acheté
```

**Créer service "Formation"** :
```
Ventes > Produits > Créer
- Nom : Formation
- Type : Service
- Politique de facturation : Quantités livrées (manuel)
- Prix de vente : 1200 € (par jour)
```

### 4. Configurer liste de prix

```
Ventes > Configuration > Listes de prix > Créer
- Nom : Tarifs ESN 2025
- Lignes :
  * Consultation IT (Junior) : 400 €
  * Consultation IT (Confirmé) : 600 €
  * Consultation IT (Senior) : 800 €
  * Formation : 1200 €
```

---

## Charger données de démo

### Option 1 : Via l'interface Odoo

```
Paramètres > Technique > Données de démonstration > Charger
(Si option disponible en mode développeur)
```

### Option 2 : Via script Python (avancé)

```powershell
# Se connecter au conteneur Odoo
docker exec -it odoo_app bash

# Lancer script Python
odoo-bin shell -d odoo_demo --no-http

# Dans le shell Python :
>>> from odoo import api, SUPERUSER_ID
>>> with api.Environment.manage():
...     env = api.Environment(self.env.cr, SUPERUSER_ID, {})
...     env['project.project'].load_demo_data()
...     env.cr.commit()
```

### Option 3 : Import CSV manuel

**Fichiers CSV fournis** :
- `demo/clients.csv` : 10 clients fictifs
- `demo/projets.csv` : 5 projets exemples
- `demo/jalons.csv` : 15 jalons

**Importer** :
```
1. Paramètres > Technique > Importer un fichier
2. Sélectionner modèle (ex: Contacts)
3. Charger le CSV
4. Mapper les colonnes
5. Importer
```

---

## Vérification installation

### Checklist ✅

Tester chaque fonctionnalité :

- [ ] **CRM** : Créer opportunité
- [ ] **Ventes** : Créer devis
- [ ] **Projet** : Projet créé automatiquement
- [ ] **Jalons** : Jalons visibles dans projet
- [ ] **Timesheet** : Saisir temps sur jalon
- [ ] **Dashboard** : Vue chef de projet fonctionnelle
- [ ] **Facturation** : Générer facture depuis jalon
- [ ] **Alertes** : Alerte si dépassement budget

### Commandes utiles Docker

```powershell
# Voir les logs Odoo (en temps réel)
docker-compose logs -f odoo

# Redémarrer Odoo (après modif code)
docker-compose restart odoo

# Arrêter tous les conteneurs
docker-compose down

# Arrêter ET supprimer volumes (ATTENTION : perte données)
docker-compose down -v

# Reconstruire les images (après update Dockerfile)
docker-compose up -d --build

# Accéder au shell du conteneur Odoo
docker exec -it odoo_app bash

# Accéder à PostgreSQL
docker exec -it odoo_db psql -U odoo
```

---

## Accès aux services

| Service | URL | Login | Password |
|---------|-----|-------|----------|
| **Odoo** | http://localhost:8069 | admin@example.com | admin |
| **PgAdmin** | http://localhost:8080 | admin@odoo-demo.local | admin |

### Connexion PgAdmin à PostgreSQL

```
1. Ouvrir http://localhost:8080
2. Login PgAdmin
3. Ajouter serveur :
   - Nom : Odoo Demo
   - Host : db (nom du service Docker)
   - Port : 5432
   - Database : postgres
   - Username : odoo
   - Password : odoo
```

---

## Dépannage

### ❌ Erreur "Port 8069 already in use"

**Cause** : Un autre service utilise le port 8069

**Solution** :
```powershell
# Modifier docker-compose.yml
ports:
  - "8070:8069"  # Utiliser port 8070 au lieu de 8069

# Relancer
docker-compose down
docker-compose up -d

# Accéder via http://localhost:8070
```

### ❌ Erreur "Database creation failed"

**Cause** : PostgreSQL pas prêt

**Solution** :
```powershell
# Vérifier logs PostgreSQL
docker-compose logs db

# Attendre 30 secondes puis réessayer

# Ou redémarrer les conteneurs
docker-compose restart
```

### ❌ Module "Project Service Pro" introuvable

**Cause** : Chemin modules custom incorrect

**Solution** :
```powershell
# Vérifier que le dossier est bien monté
docker exec -it odoo_app ls /mnt/extra-addons
# Doit afficher : project_service_pro/

# Si vide, vérifier docker-compose.yml :
volumes:
  - ../odoo_custom_modules:/mnt/extra-addons

# Relancer
docker-compose down
docker-compose up -d
```

### ❌ Odoo lent (Windows)

**Cause** : WSL2 et volumes Docker

**Solution** :
```
1. Docker Desktop > Settings > Resources
2. Augmenter RAM : 4 GB → 6 GB
3. Augmenter CPU : 2 cores → 4 cores
4. Apply & Restart
```

### ❌ Import CSV échoue

**Cause** : Format colonnes incorrect

**Solution** :
1. Télécharger template Odoo (bouton dans interface import)
2. Copier/coller vos données dans le template
3. Réimporter

---

## Désinstallation

```powershell
# Arrêter et supprimer conteneurs + volumes
cd configuration
docker-compose down -v

# Supprimer images (optionnel, libère ~2 GB)
docker rmi odoo:17.0
docker rmi postgres:15
docker rmi dpage/pgadmin4

# Supprimer dossier projet (si nécessaire)
cd ..
Remove-Item -Recurse -Force odoo-consultant-demo
```

---

## Prochaines étapes

Une fois l'installation terminée :

1. **Explorer la documentation**
   - `documentation/01_analyse_besoins/`
   - `documentation/02_specifications/`

2. **Tester les scénarios utilisateur**
   - Voir `demo_assets/presentation.md`

3. **Modifier le code**
   - Le dossier `odoo_custom_modules/` est synchronisé en temps réel
   - Après modification : `docker-compose restart odoo`

4. **Préparer votre démo**
   - Suivre le guide `presentation.md`
   - Créer vos propres données de test

---

## Support

### Ressources Odoo
- 📚 [Documentation Odoo 17](https://www.odoo.com/documentation/17.0/)
- 🎓 [Tutoriels YouTube](https://www.youtube.com/c/Odoo)
- 💬 [Forum Odoo](https://www.odoo.com/forum)
- 🐙 [GitHub Odoo](https://github.com/odoo/odoo)

### Contact
Pour questions sur ce projet démo :
- 📧 Email : [votre-email]
- 💼 LinkedIn : [votre-profil]
- 🐙 GitHub Issues : [lien-repo]/issues

---

**Temps total installation : 15-20 minutes** ⏱️

*Dernière mise à jour : 23 octobre 2025*
