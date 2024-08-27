@echo off
echo Inizio pull

:: Esegui il pull dall'upstream
git pull
echo Pull completato
:: Aggiungi tutti i file modificati all'area di staging
git add .

:: Chiedi all'utente di inserire un messaggio di commit
set /p commitMessage="Inserisci il messaggio di commit: "

:: Esegui il commit con il messaggio fornito
git commit -m "%commitMessage%"

:: Esegui il push verso l'upstream
git push

echo Operazione completata!
pause