import csv
from typing import List, Tuple

def edit_contact(contacts: List[Tuple[str, str, str, str, str, str]], index: int,
                 updated_info: Tuple[str, str, str, str, str, str]) -> List[Tuple[str, str, str, str, str, str]]:
    """
    Редактирует существующий контакт в списке контактов.

    Args:
    contacts (List[Tuple[str, str, str, str, str, str]]): Список кортежей, представляющих текущие контакты.
    index (int): Индекс контакта, который необходимо отредактировать.
    updated_info (Tuple[str, str, str, str, str, str]): Кортеж с обновленной информацией о контакте.

    Returns:
    List[Tuple[str, str, str, str, str, str]]: Обновленный список контактов после редактирования контакта.
    """
    contacts[index] = updated_info
    return contacts


def save_contacts(filename: str, contacts: List[Tuple[str, str, str, str, str, str]]) -> None:
    """
    Сохраняет контакты в файл CSV.

    Args:
    filename (str): Имя файла для сохранения контактов.
    contacts (List[Tuple[str, str, str, str, str, str]]): Список контактов для сохранения.

    Returns:
    None
    """
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Last Name', 'First Name', 'Middle Name', 'Organization', 'Work Phone', 'Personal Phone']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for contact in contacts:
            writer.writerow({'Last Name': contact[0], 'First Name': contact[1], 'Middle Name': contact[2],
                             'Organization': contact[3], 'Work Phone': contact[4], 'Personal Phone': contact[5]})
    print(f"Контакты успешно сохранены в файл {filename}.")


def main() -> None:
    """
    Основная функция, управляющая функционалом программы.

    Returns:
    None
    """
    filename = 'contacts.csv'
    contacts = []  # Создание пустого списка контактов

    while True:
        print("Выберите действие:")
        print("1. Вывод контактов")
        print("2. Добавление контакта")
        print("3. Редактирование контакта")
        print("4. Поиск контакта")
        print("5. Выход")

        choice = input("Введите номер действия: ")
        if choice == "1":
            print("Список контактов:")
            for idx, contact in enumerate(contacts):
                print(
                    f"{idx + 1}. Фамилия: {contact[0]}, Имя: {contact[1]}, Отчество: {contact[2]}, Организация: {contact[3]}, Рабочий телефон: {contact[4]}, Личный телефон: {contact[5]}")

        elif choice == "2":
            last_name = input("Введите фамилию: ")
            first_name = input("Введите имя: ")
            middle_name = input("Введите отчество: ")
            organization = input("Введите название организации: ")
            work_phone = input("Введите рабочий телефон: ")
            personal_phone = input("Введите личный телефон (сотовый): ")
            new_contact = (last_name, first_name, middle_name, organization, work_phone, personal_phone)
            contacts.append(new_contact)
            print("Контакт успешно добавлен.")

        elif choice == "3":
            # Редактирование контакта
            index = int(input("Введите номер контакта, который необходимо отредактировать: ")) - 1
            if 0 <= index < len(contacts):
                last_name = input("Введите новую фамилию: ")
                first_name = input("Введите новое имя: ")
                middle_name = input("Введите новое отчество: ")
                organization = input("Введите новое название организации: ")
                work_phone = input("Введите новый рабочий телефон: ")
                personal_phone = input("Введите новый личный телефон (сотовый): ")
                updated_info = (last_name, first_name, middle_name, organization, work_phone, personal_phone)
                contacts = edit_contact(contacts, index, updated_info)
                print("Контакт успешно отредактирован.")
            else:
                print("Некорректный номер контакта.")

        elif choice == "4":
            search_term = input("Введите имя или номер телефона для поиска: ")
            found_contacts = [contact for contact in contacts if search_term in contact[0] or search_term in contact[5]]
            if found_contacts:
                print("Найденные контакты:")
                for idx, contact in enumerate(found_contacts):
                    print(
                        f"{idx + 1}. Фамилия: {contact[0]}, Имя: {contact[1]}, Отчество: {contact[2]}, Организация: {contact[3]}, Рабочий телефон: {contact[4]}, Личный телефон: {contact[5]}")
            else:
                print("Контакт не найден")

        elif choice == "5":
            # Сохранение и выход из программы
            save_contacts(filename, contacts)
            print("Данные сохранены. Программа завершена.")
            break

        else:
            print("Некорректный выбор. Пожалуйста, выберите существующий номер действия.")


if __name__ == "__main__":
    main()
