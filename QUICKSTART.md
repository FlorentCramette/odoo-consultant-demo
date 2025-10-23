# ⚡ Quick Start - 5 Minutes

Lancez votre démo Odoo en 5 minutes !

## Étape 1 : Prérequis (si pas déjà fait)
```powershell
# Installer Docker Desktop depuis https://www.docker.com/products/docker-desktop/
# Redémarrer Windows après installation
```

## Étape 2 : Lancer Odoo
```powershell
# Ouvrir PowerShell dans le dossier du projet
cd C:\Users\flore\Desktop\odoo-consultant-demo

# Lancer avec le script PowerShell
.\odoo-demo.ps1 start

# OU directement avec Docker Compose
cd configuration
docker-compose up -d
```

**Attendre 2-3 minutes** ⏳ (téléchargement images la première fois)

## Étape 3 : Créer la base de données
1. Ouvrir http://localhost:8069
2. Cliquer "Créer une base de données"
3. Remplir :
   - Database Name: `odoo_demo`
   - Email: `admin`
   - Password: `admin`
   - Language: Français
   - Country: France
   - ☑️ Demo data
4. Cliquer "Create database"

**Attendre 2-3 minutes** ⏳

## Étape 4 : Activer mode développeur
```
1. Cliquer sur l'icône ⚙️ Paramètres (en haut à droite)
2. Scroll en bas
3. Cliquer "Activer le mode développeur"
```

## Étape 5 : Installer le module
```
1. Menu Apps (applications)
2. Cliquer ⋮ (trois points verticaux) > "Update Apps List"
3. Confirmer "Update"
4. Rechercher "Project Service Pro"
5. Cliquer "Install" (ou "Activate")
```

**Attendre 1-2 minutes** ⏳

## ✅ C'est prêt !

Vous pouvez maintenant :
- Créer un projet : Menu **Projet** > Projets
- Créer un jalon : Menu **Projet** > Jalons > Créer
- Saisir du temps : Menu **Feuilles de temps**

## 🎯 Parcours de démo rapide

### 1. Créer un client
```
Menu : Contacts > Créer
- Nom : TechCorp SA
- Type : Société
- Enregistrer
```

### 2. Créer un projet
```
Menu : Projet > Projets > Créer
- Nom : Migration CRM TechCorp
- Client : TechCorp SA
- Enregistrer
```

### 3. Créer un jalon
```
Menu : Projet > Jalons > Créer
- Nom : Phase 1 - Analyse
- Projet : Migration CRM TechCorp
- Budget heures : 40
- Montant : 24000€
- Type : Forfait
- Enregistrer
- Bouton "Démarrer"
```

### 4. Saisir du temps
```
Menu : Feuilles de temps > Créer
- Date : Aujourd'hui
- Projet : Migration CRM TechCorp
- Jalon : Phase 1 - Analyse
- Heures : 7.5
- Description : Ateliers utilisateurs
- Enregistrer
```

### 5. Voir la progression
```
Retour dans le jalon :
- Progress : 18.75% (7.5h / 40h)
- Heures consommées : 7.5h
- Heures restantes : 32.5h
```

### 6. Terminer et facturer
```
Dans le jalon :
- Bouton "Marquer comme terminé"
- Bouton "Créer facture"
- Vérifier montant : 24 000€
- Valider la facture
```

## 🛑 Arrêter Odoo

```powershell
# Avec le script
.\odoo-demo.ps1 stop

# OU avec Docker Compose
cd configuration
docker-compose down
```

## 🔧 Commandes utiles

```powershell
# Voir les logs
.\odoo-demo.ps1 logs

# Redémarrer Odoo (après modif code)
.\odoo-demo.ps1 restart

# Voir le statut
.\odoo-demo.ps1 status

# Accéder au shell Odoo
.\odoo-demo.ps1 shell
```

## ❓ Problèmes ?

### "Port 8069 already in use"
→ Un autre programme utilise le port. Modifier dans `docker-compose.yml` : `8070:8069`

### "Module introuvable"
→ Vérifier que le dossier `odoo_custom_modules/` existe

### "Odoo ne démarre pas"
→ Vérifier les logs : `.\odoo-demo.ps1 logs`

---

**Pour plus de détails, voir `INSTALL.md`**
