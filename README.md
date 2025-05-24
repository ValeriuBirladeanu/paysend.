# Teste automate Playwright pentru site-ul Paysend

## Descriere generală

Acest proiect conține teste automate E2E scrise cu **Playwright și Pytest**, 
care verifică afișarea corectă a **comisionului** și **cursului valutar** pe site-ul [https://paysend.com](https://paysend.com).

## Abordarea mea

- Am folosit arhitectura **Page Object Model (POM)** pentru o structură clară și scalabilă.
- Țările și valutele sunt alese **aleatoriu** pentru a testa mai multe combinații posibile.
- După selectarea valutei, testele așteaptă ca valorile afișate să fie actualizate complet.
- Verificările sunt făcute prin conversie și comparare atentă a numerelor (`float`), cu rotunjire la 2 zecimale.
- **Capturi de ecran automate:** După execuția fiecărui test, indiferent de rezultat (succes sau eșec), se generează 
- automat o captură de ecran care este atașată raportului Allure, ( dar si in proiect in folderul "screenshots", care se 
- genereaza automat, oferind o vizualizare completă a stării UI în momentul - finalizării testului.

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