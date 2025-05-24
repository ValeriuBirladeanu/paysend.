# Teste automate Playwright pentru site-ul Paysend

## Descriere generală

Acest proiect conține teste automate E2E scrise cu **Playwright și Pytest**, 
care verifică afișarea corectă a **comisionului** și **cursului valutar** pe site-ul [https://paysend.com](https://paysend.com).

Structura Proiectului și Abordarea Tehnică
Pentru a asigura un set de teste robuste, ușor de întreținut și scalabile, am adoptat următoarele principii și practici
în dezvoltarea acestui proiect:

Implementare cu Page Object Model (POM):
Am structurat codul conform principiilor Page Object Model. Această arhitectură disociază logica de interacțiune cu 
elementele de interfață (UI) de scenariile de testare. Astfel, orice modificare a UI-ului unei pagini necesită ajustări 
doar în fișierul corespunzător Page Object-ului (pages/), minimizând impactul asupra testelor și simplificând mentenanța
pe termen lung.

Diversitatea Scenariilor prin Date Aleatorii:
Pentru a spori acoperirea testelor și a asigura robustetea, țările și valutele utilizate în scenariile de testare sunt 
selectate aleatoriu. Această abordare permite verificarea unui număr mare de combinații posibile, depășind limitările 
testării cu date statice și identificând potențiale probleme legate de diverse perechi valutare sau regiuni.

Gestionarea Asincronă a Elementelor UI:
Recunoscând natura dinamică a aplicațiilor web, am implementat mecanisme de așteptare inteligente. După inițierea unei 
selecții de valută, testele așteaptă în mod explicit ca toate valorile afișate pe UI (cum ar fi comisionul și cursul 
valutar) să fie actualizate complet și stabilizate. Aceasta elimină erorile de tip "flaky tests" cauzate de elemente 
care nu sunt încă randate sau calculate corect.

Validări Numerice Riguroase:
Pentru a asigura acuratețea calculelor financiare, verificările sunt efectuate prin conversia valorilor din UI în
numere cu virgulă mobilă (float). Compararea acestor valori numerice este realizată cu o atenție sporită la precizie, 
rotunjind rezultatele la 2 zecimale. Această metodă evită erorile de comparație specifice tipurilor float și garantează
că valorile afișate sunt conforme cu calculele așteptate, chiar și în prezența unor mici diferențe de precizie.

Capturi de Ecran Automate pentru Depanare și Dovadă:
Am integrat o funcționalitate de generare automată a capturilor de ecran după execuția fiecărui test, indiferent de 
rezultatul său (succes sau eșec). Aceste screenshot-uri sunt atașate direct în raportul Allure, oferind o vizualizare 
contextuală valoroasă a stării interfeței utilizatorului în momentul finalizării testului. În plus, pentru o referință
rapidă și o depurare offline, toate aceste imagini sunt salvate și într-un folder dedicat (screenshots/) generat 
automat în structura proiectului.

---

## Rulare rapidă (Quick Start)

Pentru a instala dependențele, a rula testele și a genera raportul Allure, urmați pașii de mai jos în terminal:

```bash
# 1. Instalarea dependențelor
pip install -r requirements.txt

# 2. Rularea testelor și generarea rezultatelor Allure
pytest -sv tests/ --alluredir=allure-results

# 3. Generarea și deschiderea raportului Allure în browser
allure serve allure-results/