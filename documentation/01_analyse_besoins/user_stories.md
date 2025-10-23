# 📝 User Stories - Gestion de Services Professionnels

## Contexte projet
**Client** : TechServices Pro  
**Secteur** : Services IT et consulting  
**Effectif** : 25 consultants  
**Besoin** : Gérer projets clients, suivi temps, facturation automatisée

---

## 🎯 Epic 1 : Gestion des Projets Client

### US-001 : Créer un projet client avec jalons
**En tant que** Chef de projet  
**Je veux** créer un projet avec plusieurs jalons/phases  
**Afin de** structurer la livraison et suivre l'avancement par étape

**Critères d'acceptation :**
- [ ] Je peux créer un projet lié à un client existant
- [ ] Je peux définir des jalons avec dates de début/fin
- [ ] Chaque jalon a un budget estimé en heures
- [ ] Je peux assigner des consultants à chaque jalon
- [ ] Le statut du jalon se met à jour automatiquement (Non commencé / En cours / Terminé / Facturé)

**Priorité** : 🔴 Haute  
**Estimation** : 5 points  
**Module Odoo** : Project (standard) + customisation

---

### US-002 : Suivi du temps par jalon
**En tant que** Consultant  
**Je veux** saisir mon temps de travail sur un jalon spécifique  
**Afin de** assurer la facturation client et le suivi budgétaire

**Critères d'acceptation :**
- [ ] Je peux créer une feuille de temps quotidienne
- [ ] Je sélectionne le projet > jalon > tâche
- [ ] Je saisis les heures et une description courte
- [ ] Le temps est automatiquement lié au bon client
- [ ] Je vois un warning si je dépasse le budget estimé du jalon

**Priorité** : 🔴 Haute  
**Estimation** : 3 points  
**Module Odoo** : Timesheet (standard)

---

### US-003 : Rapport d'avancement projet
**En tant que** Chef de projet  
**Je veux** visualiser l'avancement global de mes projets  
**Afin de** piloter et anticiper les dépassements

**Critères d'acceptation :**
- [ ] Dashboard avec liste de mes projets actifs
- [ ] Pour chaque projet : % heures consommées vs budget
- [ ] Indicateur visuel (vert/orange/rouge) si dépassement
- [ ] Graphique évolution heures par semaine
- [ ] Export PDF du rapport pour le client

**Priorité** : 🟡 Moyenne  
**Estimation** : 5 points  
**Module Odoo** : Project + reporting custom

---

## 🎯 Epic 2 : Facturation et Devis

### US-004 : Créer un devis avec approbation
**En tant que** Commercial  
**Je veux** créer un devis basé sur un template  
**Afin de** standardiser les offres et accélérer le processus

**Critères d'acceptation :**
- [ ] Je peux créer un devis à partir d'un template (forfait ou régie)
- [ ] Les prix unitaires sont pré-remplis depuis la liste de prix
- [ ] Je peux ajouter des lignes personnalisées
- [ ] Le devis nécessite une approbation du responsable si >10k€
- [ ] Notification automatique au responsable

**Priorité** : 🔴 Haute  
**Estimation** : 5 points  
**Module Odoo** : Sales + Studio (workflow approbation)

---

### US-005 : Workflow d'approbation automatique
**En tant que** Responsable commercial  
**Je veux** recevoir une notification pour approuver les devis >10k€  
**Afin de** valider les conditions avant envoi client

**Critères d'acceptation :**
- [ ] Réception email automatique avec lien vers le devis
- [ ] Interface d'approbation avec boutons Approuver/Refuser/Demander modification
- [ ] Champ commentaire obligatoire en cas de refus
- [ ] Une fois approuvé, le commercial peut envoyer au client
- [ ] Historique des approbations visible dans le devis

**Priorité** : 🟡 Moyenne  
**Estimation** : 3 points  
**Module Odoo** : Sales + custom workflow

---

### US-006 : Facturation automatique des jalons
**En tant que** Comptable  
**Je veux** générer automatiquement les factures basées sur les jalons complétés  
**Afin de** gagner du temps et éviter les oublis

**Critères d'acceptation :**
- [ ] Un jalon marqué "À facturer" génère un brouillon de facture
- [ ] Les lignes de facture reprennent les heures réelles du jalon
- [ ] Le tarif est calculé selon le type de prestation (régie/forfait)
- [ ] Je peux ajuster manuellement avant validation
- [ ] Email automatique au client une fois validée

**Priorité** : 🔴 Haute  
**Estimation** : 8 points  
**Module Odoo** : Account + Sales + custom automation

---

## 🎯 Epic 3 : Gestion des Ressources

### US-007 : Planning consultant
**En tant que** Responsable RH  
**Je veux** visualiser la charge de travail de mes consultants  
**Afin de** équilibrer les affectations et éviter le surcharge

**Critères d'acceptation :**
- [ ] Vue calendrier avec tous les consultants
- [ ] Affichage des projets/jalons assignés par consultant
- [ ] Code couleur selon taux d'occupation (vert <80%, orange 80-100%, rouge >100%)
- [ ] Possibilité de drag & drop pour réaffecter
- [ ] Filtre par compétence (Java, Python, SAP, etc.)

**Priorité** : 🟡 Moyenne  
**Estimation** : 8 points  
**Module Odoo** : Planning ou HR Planning

---

### US-008 : Profil de compétences consultant
**En tant que** Responsable RH  
**Je veux** maintenir un profil de compétences pour chaque consultant  
**Afin de** affecter les bonnes ressources aux projets

**Critères d'acceptation :**
- [ ] Fiche consultant avec liste de compétences (tags)
- [ ] Niveau de compétence (Junior/Confirmé/Expert)
- [ ] Certifications et formations
- [ ] Taux journalier moyen (TJM) par compétence
- [ ] Historique des projets réalisés

**Priorité** : 🟢 Basse  
**Estimation** : 5 points  
**Module Odoo** : HR + custom fields

---

## 🎯 Epic 4 : Reporting et Analytics

### US-009 : Dashboard direction
**En tant que** Directeur  
**Je veux** avoir une vue consolidée de l'activité  
**Afin de** piloter l'entreprise et prendre des décisions

**Critères d'acceptation :**
- [ ] Chiffre d'affaires du mois vs objectif
- [ ] Nombre de projets actifs
- [ ] Taux d'occupation moyen des consultants
- [ ] Top 5 clients (CA)
- [ ] Projets en dépassement budgétaire
- [ ] Prévisionnel CA à 3 mois

**Priorité** : 🟡 Moyenne  
**Estimation** : 8 points  
**Module Odoo** : Dashboard custom + BI

---

### US-010 : Analyse rentabilité par projet
**En tant que** Contrôleur de gestion  
**Je veux** analyser la rentabilité de chaque projet  
**Afin de** identifier les projets profitables et optimiser les tarifs

**Critères d'acceptation :**
- [ ] Rapport listant tous les projets avec indicateurs :
  - Heures budgétées vs réalisées
  - CA facturé
  - Coût réel (heures × coût horaire consultant)
  - Marge (€ et %)
- [ ] Possibilité de filtrer par période, client, chef de projet
- [ ] Export Excel avec données détaillées
- [ ] Graphiques de comparaison

**Priorité** : 🟢 Basse  
**Estimation** : 8 points  
**Module Odoo** : Reporting custom

---

## 📊 Récapitulatif

| Epic | User Stories | Points totaux | Priorité dominante |
|------|-------------|---------------|-------------------|
| Gestion Projets | 3 | 13 | 🔴 Haute |
| Facturation | 3 | 16 | 🔴 Haute |
| Ressources | 2 | 13 | 🟡 Moyenne |
| Reporting | 2 | 16 | 🟡 Moyenne |
| **TOTAL** | **10** | **58** | - |

---

## 🔄 Priorisation pour MVP (Phase 1)

### Sprint 1 (Semaine 1-2) - Fondations
- ✅ US-001 : Créer projet avec jalons
- ✅ US-002 : Suivi temps par jalon
- ✅ US-004 : Créer devis avec template

### Sprint 2 (Semaine 3-4) - Facturation
- ✅ US-006 : Facturation automatique jalons
- ✅ US-005 : Workflow approbation devis

### Sprint 3 (Semaine 5-6) - Reporting
- ✅ US-003 : Rapport avancement projet
- ✅ US-007 : Planning consultant (version simple)

### Phase 2 (Ultérieur)
- US-008, US-009, US-010 : Features avancées

---

**Méthodologie** : Agile/Scrum  
**Durée sprint** : 2 semaines  
**Équipe** : 1 développeur Odoo + 1 consultant fonctionnel  
**Revue** : Démo client toutes les 2 semaines

---

*Document rédigé par : Consultant Fonctionnel Odoo*  
*Dernière mise à jour : 23 octobre 2025*
