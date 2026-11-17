Helpdesk Ticket System
Helpdesk Ticket System – prosty, konsolowy system do zarządzania zgłoszeniami w języku Python.

Aplikacja zapisuje dane w pliku tickets.json i pozwala na:

dodawanie nowych zgłoszeń,
wyświetlanie listy wszystkich zgłoszeń,
zamykanie istniejących zgłoszeń,
podgląd statystyk (otwarte/ zamknięte / wszystkie).
📦 Instalacja
Pobierz repozytorium


Copy
bash
git clone https://github.com/<twoje-konto>/helpdesk-ticket-system.git
cd helpdesk-ticket-system
Upewnij się, że masz zainstalowanego Pythona 3.8+


Copy
bash
python --version
(Opcjonalnie) Utwórz wirtualne środowisko:


Copy
bash
python -m venv .venv
source .venv/bin/activate      # Linux/macOS
.\.venv\Scripts\activate       # Windows
Uruchom aplikację


Copy
bash
python main.py
📖 Użytkowanie
Po uruchomieniu pojawi się menu:


Copy
=== HELPDESK TICKET SYSTEM ===
1. Dodaj zgłoszenie
2. Pokaż zgłoszenia
3. Zamknij zgłoszenie
4. Statystyki
5. Wyjście
Wybierz opcję:
Opcje
Numer	Akcja	Opis
1	Dodaj zgłoszenie	Wprowadź tytuł, a system przypisuje unikalny ID oraz status Open.
2	Pokaż zgłoszenia	Wyświetla listę wszystkich zgłoszeń z ID, tytułem i statusem.
3	Zamknij zgłoszenie	Wprowadź ID zgłoszenia – jeśli istnieje, status zmienia się na Closed.
4	Statystyki	Pokazuje liczbę otwartych, zamkniętych oraz wszystkich zgłoszeń.
5	Wyjście	Zakończenie programu.
🗂️ Struktura plików

Copy
helpdesk-ticket-system/
├── main.py          # Główny skrypt z logiką aplikacji
├── tickets.json     # Plik przechowujący dane (tworzy się automatycznie)
└── README.md        # Ten plik
tickets.json – JSON zawierający listę obiektów:

Copy
json
[
    {
        "id": 1,
        "title": "Problem z drukarką",
        "status": "Open"
    },
    ...
]
⚙️ Technologia
Python – wersja 3.8+
Brak dodatkowych zależności (tylko wbudowane moduły json i os).
🤝 Współpraca
Jeśli chcesz rozwinąć projekt, np. dodać interfejs webowy, bazy danych czy autoryzację – śmiało twórz pull request!

Zalecane jest dodanie testów jednostkowych oraz dokumentacji w formie docstringów.

📄 Licencja
Projekt jest dostępny na licencji MIT. Zobacz plik LICENSE dla pełnych szczegółów.
