# Script de configuration Git et push vers GitHub
# Auteur : Florent Cramette
# Date : 23 octobre 2025

Write-Host "=== Configuration Git pour odoo-consultant-demo ===" -ForegroundColor Cyan
Write-Host ""

# Vérifier si Git est installé
try {
    $gitVersion = git --version
    Write-Host "✅ Git installé : $gitVersion" -ForegroundColor Green
} catch {
    Write-Host "❌ Git n'est pas installé !" -ForegroundColor Red
    Write-Host "   Télécharger depuis : https://git-scm.com/downloads" -ForegroundColor Yellow
    exit 1
}

Write-Host ""
Write-Host "📂 Dossier actuel : $PWD" -ForegroundColor Yellow

# Initialiser Git si pas déjà fait
if (-Not (Test-Path ".git")) {
    Write-Host ""
    Write-Host "🔧 Initialisation Git..." -ForegroundColor Cyan
    git init
    Write-Host "✅ Repository Git initialisé" -ForegroundColor Green
} else {
    Write-Host ""
    Write-Host "✅ Repository Git déjà initialisé" -ForegroundColor Green
}

# Configurer utilisateur Git (si pas déjà fait)
$gitUserName = git config user.name
$gitUserEmail = git config user.email

if (-Not $gitUserName) {
    Write-Host ""
    Write-Host "🔧 Configuration utilisateur Git..." -ForegroundColor Cyan
    git config user.name "Florent Cramette"
    git config user.email "votre-email@example.com"  # À MODIFIER
    Write-Host "✅ Utilisateur Git configuré" -ForegroundColor Green
} else {
    Write-Host ""
    Write-Host "✅ Utilisateur Git : $gitUserName <$gitUserEmail>" -ForegroundColor Green
}

# Ajouter tous les fichiers
Write-Host ""
Write-Host "📦 Ajout des fichiers..." -ForegroundColor Cyan
git add .

# Premier commit
Write-Host ""
Write-Host "💾 Création du commit initial..." -ForegroundColor Cyan
git commit -m "Initial commit - Odoo Consultant Demo Portfolio

- Documentation fonctionnelle complète (user stories, processus métier, matrices décision)
- Spécifications techniques (cahier des charges, mapping modules)
- Module Odoo custom Python (project_service_pro)
- Configuration Docker (Odoo 17 + PostgreSQL + PgAdmin)
- Guides installation et présentation
- Scripts PowerShell pour gestion environnement

Projet démontrant compétences consultant fonctionnel Odoo :
✅ Analyse fonctionnelle et user stories
✅ Spécifications techniques détaillées
✅ Développement module Python (modèles, vues, workflows)
✅ Architecture et déploiement Docker
✅ Documentation professionnelle
"

Write-Host "✅ Commit créé" -ForegroundColor Green

# Ajouter remote GitHub
Write-Host ""
Write-Host "🔗 Configuration remote GitHub..." -ForegroundColor Cyan

$remoteUrl = "https://github.com/FlorentCramette/odoo-consultant-demo.git"

# Vérifier si remote existe déjà
$existingRemote = git remote get-url origin 2>$null

if ($existingRemote) {
    Write-Host "⚠️  Remote 'origin' existe déjà : $existingRemote" -ForegroundColor Yellow
    $response = Read-Host "Voulez-vous le remplacer ? (O/N)"
    if ($response -eq 'O' -or $response -eq 'o') {
        git remote remove origin
        git remote add origin $remoteUrl
        Write-Host "✅ Remote mis à jour" -ForegroundColor Green
    }
} else {
    git remote add origin $remoteUrl
    Write-Host "✅ Remote configuré : $remoteUrl" -ForegroundColor Green
}

# Renommer branche en 'main' si nécessaire
$currentBranch = git branch --show-current
if ($currentBranch -ne "main") {
    Write-Host ""
    Write-Host "🔧 Renommage branche '$currentBranch' → 'main'..." -ForegroundColor Cyan
    git branch -M main
    Write-Host "✅ Branche renommée" -ForegroundColor Green
}

# Push vers GitHub
Write-Host ""
Write-Host "🚀 Push vers GitHub..." -ForegroundColor Cyan
Write-Host "   (Vous devrez peut-être vous authentifier)" -ForegroundColor Yellow
Write-Host ""

try {
    git push -u origin main
    Write-Host ""
    Write-Host "════════════════════════════════════════" -ForegroundColor Green
    Write-Host "✅ SUCCÈS ! Repository publié sur GitHub" -ForegroundColor Green
    Write-Host "════════════════════════════════════════" -ForegroundColor Green
    Write-Host ""
    Write-Host "🔗 Votre repo : https://github.com/FlorentCramette/odoo-consultant-demo" -ForegroundColor Cyan
    Write-Host ""
    Write-Host "Prochaines étapes :" -ForegroundColor Yellow
    Write-Host "  1. Vérifier le repo sur GitHub" -ForegroundColor White
    Write-Host "  2. Ajouter description et topics sur GitHub" -ForegroundColor White
    Write-Host "  3. Mettre le lien dans votre CV/LinkedIn" -ForegroundColor White
    Write-Host ""
} catch {
    Write-Host ""
    Write-Host "❌ Erreur lors du push" -ForegroundColor Red
    Write-Host "   Vérifier que le repository existe sur GitHub :" -ForegroundColor Yellow
    Write-Host "   https://github.com/FlorentCramette/odoo-consultant-demo" -ForegroundColor Yellow
    Write-Host ""
    Write-Host "   Si le repo n'existe pas encore :" -ForegroundColor Yellow
    Write-Host "   1. Aller sur https://github.com/new" -ForegroundColor White
    Write-Host "   2. Créer 'odoo-consultant-demo'" -ForegroundColor White
    Write-Host "   3. Relancer ce script" -ForegroundColor White
    Write-Host ""
}
