import json
import os

FILE_NAME = "tickets.json"


def load_tickets():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            return json.load(file)
    return []


def save_tickets(tickets):
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        json.dump(tickets, file, indent=4, ensure_ascii=False)


def next_id(tickets):
    if not tickets:
        return 1
    return max(ticket["id"] for ticket in tickets) + 1


def add_ticket(tickets):
    title = input("Tytuł zgłoszenia: ")

    ticket = {
        "id": next_id(tickets),
        "title": title,
        "status": "Open"
    }

    tickets.append(ticket)
    save_tickets(tickets)

    print("Zgłoszenie dodane.")


def show_tickets(tickets):
    if not tickets:
        print("Brak zgłoszeń.")
        return

    print("\n=== ZGŁOSZENIA ===")

    for ticket in tickets:
        print(
            f'ID: {ticket["id"]} | '
            f'{ticket["title"]} | '
            f'{ticket["status"]}'
        )


def close_ticket(tickets):
    try:
        ticket_id = int(input("Podaj ID zgłoszenia: "))
    except ValueError:
        print("Nieprawidłowe ID.")
        return

    for ticket in tickets:
        if ticket["id"] == ticket_id:
            ticket["status"] = "Closed"
            save_tickets(tickets)
            print("Zgłoszenie zamknięte.")
            return

    print("Nie znaleziono zgłoszenia.")


def show_stats(tickets):
    open_count = sum(
        1 for ticket in tickets
        if ticket["status"] == "Open"
    )

    closed_count = sum(
        1 for ticket in tickets
        if ticket["status"] == "Closed"
    )

    print("\n=== STATYSTYKI ===")
    print(f"Otwarte: {open_count}")
    print(f"Zamknięte: {closed_count}")
    print(f"Wszystkie: {len(tickets)}")


def main():
    tickets = load_tickets()

    while True:
        print("\n=== HELPDESK TICKET SYSTEM ===")
        print("1. Dodaj zgłoszenie")
        print("2. Pokaż zgłoszenia")
        print("3. Zamknij zgłoszenie")
        print("4. Statystyki")
        print("5. Wyjście")

        choice = input("Wybierz opcję: ")

        if choice == "1":
            add_ticket(tickets)

        elif choice == "2":
            show_tickets(tickets)

        elif choice == "3":
            close_ticket(tickets)

        elif choice == "4":
            show_stats(tickets)

        elif choice == "5":
            print("Do widzenia!")
            break

        else:
            print("Nieprawidłowa opcja.")


if __name__ == "__main__":
    main()