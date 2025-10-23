# 🚀 Project Service Pro - Module Odoo Custom

## Description
Module custom Odoo pour la gestion de services professionnels (ESN, consulting, agences).

### Fonctionnalités principales
✅ **Jalons de projet** : Découpez vos projets en phases facturables  
✅ **Suivi budgétaire** : Alertes automatiques si dépassement >90%  
✅ **Calcul rentabilité** : Analysez marge par projet et jalon  
✅ **Facturation automatique** : Générez factures depuis jalons terminés  
✅ **Dashboard chef de projet** : Vue consolidée de vos projets actifs  

## Architecture technique

### Nouveaux modèles
- `project.milestone` : Jalon de projet avec budget et facturation
- `project.milestone.type` : Types de jalons (Analyse, Dev, Recette, etc.)
- `project.budget.alert` : Historique des alertes de dépassement

### Extensions de modèles existants
- `project.project` : Ajout relation jalons, calcul rentabilité
- `account.analytic.line` : Lien vers jalon (`milestone_id`)
- `project.task` : Lien vers jalon
- `sale.order` : Génération automatique jalons

## Installation

### 1. Prérequis
- Odoo Community 17.0
- Modules dépendants (installés automatiquement) :
  - `project`
  - `hr_timesheet`
  - `sale_management`
  - `sale_timesheet`
  - `account`

### 2. Installation du module
```bash
# 1. Copier le module dans le dossier addons
cp -r project_service_pro /path/to/odoo/addons/

# 2. Redémarrer Odoo
docker-compose restart odoo

# 3. Mettre à jour la liste des applications
# Dans Odoo : Apps > Update Apps List (en mode développeur)

# 4. Installer le module
# Rechercher "Project Service Pro" et cliquer Install
```

### 3. Configuration initiale
```
1. Paramètres > Projet > Activer "Jalons" (si nécessaire)
2. Projet > Configuration > Types de jalons (vérifier données de base)
3. Ventes > Configuration > Liste de prix (configurer TJM)
```

## Utilisation

### Scénario 1 : Créer un projet avec jalons

1. **Créer un devis** (Ventes > Devis > Créer)
   - Sélectionner client
   - Ajouter lignes de service (1 ligne = 1 jalon)
   - Confirmer le devis

2. **Le projet est créé automatiquement**
   - Projet > Mes Projets
   - Les jalons sont créés depuis les lignes de commande

3. **Affecter des consultants**
   - Ouvrir le projet
   - Onglet Jalons
   - Assigner consultants à chaque jalon

### Scénario 2 : Suivre l'avancement

1. **Saisir du temps** (Feuilles de temps > Saisie)
   - Sélectionner Projet > Jalon
   - Saisir heures travaillées
   - Enregistrer

2. **Consulter dashboard**
   - Projet > Dashboard
   - Voir progression par jalon
   - Alertes rouges si dépassement budget

### Scénario 3 : Facturer un jalon

1. **Terminer le jalon**
   - Ouvrir le jalon
   - Bouton "Marquer comme terminé"

2. **Générer la facture**
   - Bouton "Créer facture"
   - Vérifier montant calculé :
     - **Forfait** : montant fixe du jalon
     - **Régie** : heures réelles × TJM
   - Valider et envoyer au client

## Structure du code

```
project_service_pro/
├── __init__.py
├── __manifest__.py
├── README.md
├── models/
│   ├── __init__.py
│   ├── project_milestone.py      # Modèle principal
│   ├── project_project.py         # Extension projet
│   ├── hr_timesheet.py            # Extension timesheet
│   └── sale_order.py              # Extension ventes
├── views/
│   ├── project_milestone_views.xml
│   ├── project_project_views.xml
│   ├── project_dashboard_views.xml
│   └── project_service_menus.xml
├── security/
│   ├── project_service_security.xml
│   └── ir.model.access.csv
├── data/
│   ├── project_milestone_type_data.xml
│   ├── mail_template_data.xml
│   └── ir_cron_data.xml           # Tâches planifiées (alertes)
├── wizards/
│   ├── project_milestone_invoice_wizard.py
│   └── project_profitability_report_wizard.py
├── reports/
│   ├── project_milestone_report_templates.xml
│   └── project_profitability_report_templates.xml
├── static/
│   ├── description/
│   │   ├── icon.png
│   │   └── banner.png
│   └── src/
│       ├── css/
│       └── js/
└── demo/
    ├── res_partner_demo.xml
    ├── project_project_demo.xml
    └── project_milestone_demo.xml
```

## Démonstration des compétences consultant

Ce module démontre :

### 1. Analyse fonctionnelle
✅ Compréhension besoins métier ESN  
✅ Modélisation processus (devis → projet → facturation)  
✅ Identification KPI clés (budget, rentabilité, charge)  

### 2. Expertise technique Odoo
✅ Création modèles custom avec héritage  
✅ Champs calculés avec `@api.depends`  
✅ Relations complexes (Many2one, One2many, Many2many)  
✅ Actions automatiques et workflows  
✅ Vues personnalisées (form, tree, kanban, dashboard)  
✅ Rapports PDF/Excel  
✅ Sécurité et droits d'accès  

### 3. Bonnes pratiques
✅ Code documenté (docstrings)  
✅ Validation données (constraints)  
✅ Traçabilité (`mail.thread`)  
✅ Séparation concerns (modèles, vues, data)  
✅ Données de démo (tests)  

### 4. Méthodologie projet
✅ Documentation complète (README, cahier charges)  
✅ User stories détaillées  
✅ Processus métier modélisés (diagrammes)  
✅ Matrice de décision technique  

## Roadmap / Évolutions possibles

### Phase 2 (court terme)
- [ ] Planning ressources interactif (drag & drop)
- [ ] Prévisionnel trésorerie basé sur jalons
- [ ] Portail client avec suivi temps réel
- [ ] Export Excel avancé (pivot tables)

### Phase 3 (moyen terme)
- [ ] IA : Estimation automatique budget heures
- [ ] Intégration calendrier (Google Calendar, Outlook)
- [ ] Gestion compétences consultants
- [ ] Matching automatique consultant/projet

### Phase 4 (long terme)
- [ ] Module RH complet (recrutement, évaluations)
- [ ] CRM avancé avec scoring opportunités
- [ ] Business Intelligence (BI) avec prédictions
- [ ] API REST pour intégrations externes

## Support et Contact

**Auteur** : Elo - Consultant Fonctionnel Odoo  
**Email** : [votre-email]  
**LinkedIn** : [votre-profil]  
**GitHub** : https://github.com/votre-username/odoo-consultant-demo

## Licence
LGPL-3 (compatible Odoo Community)

---

*Module développé dans le cadre d'une démonstration de compétences consultant Odoo*
