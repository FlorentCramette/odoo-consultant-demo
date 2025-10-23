# Script PowerShell - Gestion Odoo Demo
# Usage: .\odoo-demo.ps1 [start|stop|restart|logs|shell|clean]

param(
    [Parameter(Position=0)]
    [ValidateSet('start', 'stop', 'restart', 'logs', 'shell', 'psql', 'clean', 'status', 'help')]
    [string]$Command = 'help'
)

$ConfigPath = ".\configuration"

function Show-Help {
    Write-Host "=== Odoo Consultant Demo - Aide ===" -ForegroundColor Cyan
    Write-Host ""
    Write-Host "Commandes disponibles:" -ForegroundColor Yellow
    Write-Host "  start      - Démarrer les conteneurs Odoo" -ForegroundColor Green
    Write-Host "  stop       - Arrêter les conteneurs" -ForegroundColor Green
    Write-Host "  restart    - Redémarrer Odoo (après modif code)" -ForegroundColor Green
    Write-Host "  logs       - Afficher les logs Odoo (temps réel)" -ForegroundColor Green
    Write-Host "  shell      - Accéder au shell du conteneur Odoo" -ForegroundColor Green
    Write-Host "  psql       - Accéder à PostgreSQL" -ForegroundColor Green
    Write-Host "  status     - Voir le statut des conteneurs" -ForegroundColor Green
    Write-Host "  clean      - Arrêter et supprimer volumes (ATTENTION: perte données)" -ForegroundColor Red
    Write-Host "  help       - Afficher cette aide" -ForegroundColor Green
    Write-Host ""
    Write-Host "Exemples:" -ForegroundColor Yellow
    Write-Host "  .\odoo-demo.ps1 start"
    Write-Host "  .\odoo-demo.ps1 logs"
    Write-Host ""
}

function Start-Odoo {
    Write-Host "🚀 Démarrage des conteneurs Odoo..." -ForegroundColor Cyan
    Set-Location $ConfigPath
    docker-compose up -d
    Set-Location ..
    Write-Host ""
    Write-Host "✅ Odoo démarré !" -ForegroundColor Green
    Write-Host "   Accès: http://localhost:8069" -ForegroundColor Yellow
    Write-Host "   PgAdmin: http://localhost:8080" -ForegroundColor Yellow
    Write-Host ""
}

function Stop-Odoo {
    Write-Host "⏸️  Arrêt des conteneurs..." -ForegroundColor Cyan
    Set-Location $ConfigPath
    docker-compose down
    Set-Location ..
    Write-Host "✅ Conteneurs arrêtés" -ForegroundColor Green
}

function Restart-Odoo {
    Write-Host "🔄 Redémarrage Odoo..." -ForegroundColor Cyan
    Set-Location $ConfigPath
    docker-compose restart odoo
    Set-Location ..
    Write-Host "✅ Odoo redémarré" -ForegroundColor Green
}

function Show-Logs {
    Write-Host "📋 Logs Odoo (Ctrl+C pour quitter)..." -ForegroundColor Cyan
    Set-Location $ConfigPath
    docker-compose logs -f odoo
    Set-Location ..
}

function Open-Shell {
    Write-Host "🐚 Accès au shell Odoo..." -ForegroundColor Cyan
    docker exec -it odoo_app bash
}

function Open-Psql {
    Write-Host "🗄️  Accès PostgreSQL..." -ForegroundColor Cyan
    docker exec -it odoo_db psql -U odoo
}

function Show-Status {
    Write-Host "📊 Statut des conteneurs:" -ForegroundColor Cyan
    Set-Location $ConfigPath
    docker-compose ps
    Set-Location ..
}

function Clean-All {
    Write-Host "⚠️  ATTENTION: Cette commande va supprimer TOUTES les données !" -ForegroundColor Red
    $confirmation = Read-Host "Êtes-vous sûr ? (tapez 'OUI' pour confirmer)"
    
    if ($confirmation -eq 'OUI') {
        Write-Host "🗑️  Suppression conteneurs et volumes..." -ForegroundColor Yellow
        Set-Location $ConfigPath
        docker-compose down -v
        Set-Location ..
        Write-Host "✅ Nettoyage terminé" -ForegroundColor Green
    } else {
        Write-Host "❌ Annulé" -ForegroundColor Yellow
    }
}

# Exécution de la commande
switch ($Command) {
    'start'   { Start-Odoo }
    'stop'    { Stop-Odoo }
    'restart' { Restart-Odoo }
    'logs'    { Show-Logs }
    'shell'   { Open-Shell }
    'psql'    { Open-Psql }
    'status'  { Show-Status }
    'clean'   { Clean-All }
    'help'    { Show-Help }
    default   { Show-Help }
}
