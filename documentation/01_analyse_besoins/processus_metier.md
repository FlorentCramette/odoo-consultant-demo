# 📊 Processus Métier - TechServices Pro

## Vue d'ensemble des processus

Ce document présente les principaux processus métier de l'entreprise TechServices Pro et leur implémentation dans Odoo.

---

## 🔄 Processus 1 : Cycle Commercial → Projet → Facturation

### Diagramme de flux

```mermaid
graph TD
    A[🎯 Opportunité détectée] --> B{Qualification}
    B -->|Qualifié| C[📝 Création devis]
    B -->|Non qualifié| Z[❌ Abandon]
    
    C --> D{Montant > 10k€?}
    D -->|Oui| E[👔 Approbation manager]
    D -->|Non| F[✅ Validation automatique]
    
    E -->|Approuvé| F
    E -->|Refusé| C
    
    F --> G[📧 Envoi au client]
    G --> H{Réponse client}
    
    H -->|Accepté| I[✅ Devis confirmé]
    H -->|Refusé| Z
    H -->|Négociation| C
    
    I --> J[🗂️ Création projet]
    J --> K[📋 Définition jalons]
    K --> L[👥 Affectation consultants]
    
    L --> M[⏱️ Saisie temps]
    M --> N{Jalon terminé?}
    
    N -->|Non| M
    N -->|Oui| O[✓ Validation jalon]
    
    O --> P{Tous jalons terminés?}
    P -->|Non| M
    P -->|Oui| Q[💰 Génération facture]
    
    Q --> R[📨 Envoi facture client]
    R --> S[💳 Paiement]
    S --> T[✅ Clôture projet]
```

### Acteurs impliqués
- **Commercial** : qualification, création devis
- **Manager** : approbation devis >10k€
- **Chef de projet** : création projet, gestion jalons
- **Consultant** : réalisation, saisie temps
- **Comptable** : facturation, suivi paiements

### Règles de gestion
1. Tout devis >10k€ nécessite validation manager sous 48h
2. Un projet ne peut démarrer que si devis signé
3. La facturation se fait au jalon (livrable terminé + validé)
4. Les consultants doivent saisir leur temps quotidiennement

---

## 🕐 Processus 2 : Gestion du Temps

### Diagramme de flux

```mermaid
graph TD
    A[📅 Début journée consultant] --> B[🔍 Consultation planning]
    B --> C[⏱️ Saisie feuille de temps]
    
    C --> D{Temps saisi}
    D --> E[Projet A - Jalon 1]
    D --> F[Projet B - Jalon 3]
    D --> G[Tâche interne]
    
    E --> H{Alerte dépassement?}
    F --> H
    G --> H
    
    H -->|Oui| I[⚠️ Notification chef de projet]
    H -->|Non| J[✅ Validation temps]
    
    I --> K{Action manager}
    K -->|Augmenter budget| J
    K -->|Stopper affectation| L[🔄 Réaffectation consultant]
    
    J --> M[📊 Agrégation données]
    M --> N[💼 Facturation client]
    M --> O[📈 Reporting direction]
```

### Fréquence
- **Quotidienne** : saisie temps par consultants
- **Hebdomadaire** : revue chef de projet
- **Mensuelle** : facturation et reporting

### Indicateurs clés (KPI)
- Taux de saisie temps J+1 : >95%
- Écart budget/réel par jalon : <10%
- Taux d'occupation consultant : 70-85%

---

## 💰 Processus 3 : Facturation Automatisée

### Diagramme BPMN simplifié

```mermaid
graph LR
    A[⏰ Fin de jalon] --> B{Type contrat?}
    
    B -->|Forfait| C[💵 Facturation 100% jalon]
    B -->|Régie| D[⏱️ Calcul heures réelles]
    
    D --> E[💵 Heures × TJM]
    
    C --> F[📝 Brouillon facture]
    E --> F
    
    F --> G[👁️ Revue comptable]
    G --> H{Corrections?}
    
    H -->|Oui| I[✏️ Ajustements manuels]
    H -->|Non| J[✅ Validation facture]
    
    I --> J
    J --> K[📧 Envoi automatique client]
    K --> L[📆 Échéance paiement]
    
    L --> M{Paiement reçu?}
    M -->|Oui| N[✅ Lettrage]
    M -->|Non J+30| O[📞 Relance niveau 1]
    
    O --> P{Paiement reçu?}
    P -->|Oui| N
    P -->|Non J+15| Q[⚠️ Relance niveau 2]
    
    Q --> R{Paiement reçu?}
    R -->|Oui| N
    R -->|Non| S[🚨 Contentieux]
```

### Automatisations Odoo
1. **Trigger jalon terminé** → génération brouillon facture
2. **J+30 après échéance** → email relance automatique
3. **Validation facture** → mise à jour trésorerie prévisionnelle
4. **Paiement reçu** → lettrage automatique et notification

---

## 👥 Processus 4 : Affectation des Ressources

### Workflow

```mermaid
graph TD
    A[📋 Nouveau projet confirmé] --> B[📊 Analyse besoins compétences]
    
    B --> C[🔍 Recherche consultants disponibles]
    C --> D{Compétences requises}
    
    D --> E[🏷️ Filtre par tags: Java]
    D --> F[🏷️ Filtre par tags: Python]
    D --> G[🏷️ Filtre par tags: SAP]
    
    E --> H[📅 Vérification disponibilité]
    F --> H
    G --> H
    
    H --> I{Disponible?}
    I -->|Oui| J[✅ Affectation consultant]
    I -->|Non| K[⏰ Ajout en liste d'attente]
    
    J --> L[📧 Notification consultant]
    L --> M[📝 Mise à jour planning]
    
    K --> N{Projet urgent?}
    N -->|Oui| O[🔄 Réaffectation autre projet]
    N -->|Non| P[⏳ Planification ultérieure]
    
    O --> J
    
    M --> Q[📊 Calcul taux occupation]
    Q --> R{Taux > 100%?}
    
    R -->|Oui| S[⚠️ Alerte surcharge]
    R -->|Non| T[✅ Planning validé]
```

### Règles d'affectation
- Priorité 1 : Compétence technique requise
- Priorité 2 : Disponibilité immédiate
- Priorité 3 : Historique avec le client (continuité)
- Priorité 4 : Taux d'occupation (équilibrage charge)

### Contraintes
- Un consultant ne peut pas être affecté à >120% sur une semaine
- Les consultants seniors doivent accompagner les juniors (max 2 juniors/senior)
- Rotation tous les 6 mois pour éviter la lassitude

---

## 📈 Processus 5 : Reporting et Pilotage

### Cycle de reporting

```mermaid
graph TD
    A[📊 Collecte données] --> B{Source}
    
    B --> C[⏱️ Feuilles de temps]
    B --> D[💰 Factures]
    B --> E[📋 Projets]
    
    C --> F[🔄 Agrégation quotidienne]
    D --> F
    E --> F
    
    F --> G[📈 Calcul indicateurs]
    
    G --> H[KPI 1: CA mensuel]
    G --> I[KPI 2: Taux occupation]
    G --> J[KPI 3: Rentabilité/projet]
    G --> K[KPI 4: Délai paiement moyen]
    
    H --> L[📊 Dashboard direction]
    I --> L
    J --> L
    K --> L
    
    L --> M{Alertes?}
    M -->|Oui| N[⚠️ Notification manager]
    M -->|Non| O[✅ Publication rapport]
    
    N --> P[💼 Réunion action]
    O --> Q[📧 Diffusion stakeholders]
```

### Fréquence des rapports
- **Temps réel** : Dashboard Odoo (consultants, chefs de projet)
- **Quotidien** : Alertes dépassement budget
- **Hebdomadaire** : Rapport avancement projets actifs
- **Mensuel** : Compte de résultat + prévisions
- **Trimestriel** : Revue stratégique direction

---

## 🔑 Points clés d'implémentation Odoo

### Modules standards utilisés
| Processus | Modules Odoo |
|-----------|--------------|
| Commercial → Projet | `sale`, `project`, `sale_project` |
| Gestion temps | `hr_timesheet`, `project_timesheet` |
| Facturation | `account`, `sale_timesheet` |
| Ressources | `hr`, `project_forecast` (Enterprise) ou custom |
| Reporting | `board`, dashboards custom |

### Personnalisations nécessaires
1. **Workflow approbation** : Champs custom + actions serveur (ou Odoo Studio)
2. **Alertes dépassement** : Actions automatiques basées sur règles
3. **Dashboard direction** : Vues personnalisées + graphiques
4. **Calcul rentabilité** : Champs calculés custom dans `project.project`

---

## 🎯 Bénéfices attendus

### Gains de temps
- ⏱️ **-60% temps facturation** : automatisation vs saisie manuelle
- ⏱️ **-40% temps reporting** : dashboards vs Excel
- ⏱️ **-30% temps administratif** : workflows vs emails

### Amélioration pilotage
- 📊 **Visibilité temps réel** sur tous les projets
- 🎯 **Anticipation** des dépassements budgétaires
- 💰 **Optimisation** affectation ressources

### Satisfaction client
- ✅ **Transparence** : accès client au portail projet
- 📧 **Réactivité** : facturation rapide et précise
- 📈 **Qualité** : meilleur respect des délais

---

*Modélisation réalisée par : Consultant Fonctionnel Odoo*  
*Dernière mise à jour : 23 octobre 2025*
