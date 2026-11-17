
# Helpdesk Ticket System

**Helpdesk Ticket System** – prosty, konsolowy system do zarządzania zgłoszeniami (tickets) napisany w języku Python.

Aplikacja zapisuje dane w pliku `tickets.json` i pozwala na:

- Dodawanie nowych zgłoszeń.
- Wyświetlanie listy wszystkich zgłoszeń.
- Zamykanie istniejących zgłoszeń.
- Wyświetlanie statystyk (otwarte / zamknięte / wszystkie).

## 📦 Instalacja

### 1. Pobierz repozytorium

```bash
git clone https://github.com/<twoje-konto>/helpdesk-ticket-system.git
cd helpdesk-ticket-system
```

### 2. Sprawdź wersję Pythona

Upewnij się, że masz zainstalowanego Pythona w wersji 3.8 lub nowszej.

```bash
python --version
```

### 3. (Opcjonalnie) Utwórz wirtualne środowisko

**Windows:**
```bash
python -m venv .venv
.\.venv\Scripts\activate
```

**Linux / macOS:**
```bash
python -m venv .venv
source .venv/bin/activate
```

### 4. Uruchom aplikację

```bash
python main.py
```

## 📖 Użytkowanie

Po uruchomieniu programu pojawi się następujące menu:

```text
=== HELPDESK TICKET SYSTEM ===
1. Dodaj zgłoszenie
2. Pokaż zgłoszenia
3. Zamknij zgłoszenie
4. Statystyki
5. Wyjście

Wybierz opcję:
```

### Dostępne opcje

| Numer | Akcja | Opis |
|:---:|---|---|
| 1 | Dodaj zgłoszenie | Wprowadź tytuł zgłoszenia. System przypisze mu unikalne ID oraz status `Open`. |
| 2 | Pokaż zgłoszenia | Wyświetla listę wszystkich zgłoszeń wraz z ich ID, tytułem i statusem. |
| 3 | Zamknij zgłoszenie | Wprowadź ID zgłoszenia. Jeśli istnieje, jego status zostanie zmieniony na `Closed`. |
| 4 | Statystyki | Wyświetla liczbę otwartych, zamkniętych oraz wszystkich zgłoszeń. |
| 5 | Wyjście | Zamyka aplikację. |

## 🗂️ Struktura projektu

```text
helpdesk-ticket-system/
│
├── main.py          # Główny skrypt zawierający logikę aplikacji
├── tickets.json     # Plik przechowujący zgłoszenia (tworzony automatycznie)
└── README.md        # Dokumentacja projektu
```

### Przykładowa struktura danych

Plik `tickets.json` przechowuje zgłoszenia w formacie JSON.

```json
[
    {
        "id": 1,
        "title": "Problem z drukarką",
        "status": "Open"
    },
    {
        "id": 2,
        "title": "Problem z logowaniem",
        "status": "Closed"
    }
]
```

## ⚙️ Technologie

- **Python 3.8+** – język programowania.
- **JSON** – przechowywanie danych zgłoszeń.
- **os** – obsługa operacji systemowych.

Projekt nie wymaga instalowania dodatkowych bibliotek zewnętrznych.

## 🤝 Współpraca

Jeśli chcesz rozwijać projekt, możesz zaproponować nowe funkcjonalności, takie jak:

- Interfejs graficzny lub webowy.
- Integracja z bazą danych.
- System logowania i autoryzacji użytkowników.
- Priorytety zgłoszeń.
- Kategorie i przypisywanie zgłoszeń do użytkowników.
- Testy jednostkowe.

Pull requesty i sugestie dotyczące rozwoju projektu są mile widziane!

## 📄 Licencja

Projekt jest dostępny na licencji **MIT**.

Szczegółowe informacje znajdują się w pliku `LICENSE`.
