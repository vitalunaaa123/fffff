class Task:
    def __init__(self, title, description, deadline, status=False):
        self.title = title
        self.description = description
        self.deadline = deadline
        self.status = status  # False - не виконано, True - виконано

    def mark_as_done(self):
        self.status = True

    def __str__(self):
        status = "✓" if self.status else "✗"
        return f"{status} {self.title} (до {self.deadline})\n   {self.description}"


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, description, deadline):
        new_task = Task(title, description, deadline)
        self.tasks.append(new_task)
        print(f"\n Завдання '{title}' додано!")

    def remove_task(self, title):
        for task in self.tasks:
            if task.title.lower() == title.lower():
                self.tasks.remove(task)
                print(f"\n🗑️ Завдання '{title}' видалено!")
                return
        print(f"\n Завдання '{title}' не знайдено!")

    def mark_task_as_done(self, title):
        for task in self.tasks:
            if task.title.lower() == title.lower():
                task.mark_as_done()
                print(f"\n Завдання '{title}' виконано!")
                return
        print(f"\n Завдання '{title}' не знайдено!")

    def show_all_tasks(self, filter_status=None):
        if not self.tasks:
            print("\n Список завдань порожній")
            return

        print("\n Список завдань:")
        for i, task in enumerate(self.tasks, 1):
            if filter_status is None or task.status == filter_status:
                print(f"{i}. {task}")

    def show_pending_tasks(self):
        self.show_all_tasks(filter_status=False)


def main():
    manager = TaskManager()

    while True:
        print("\n" + "=" * 40)
        print("  Менеджер завдань")
        print("=" * 40)
        print("1. Додати завдання")
        print("2. Показати всі завдання")
        print("3. Показати невиконані завдання")
        print("4. Відзначити завдання як виконане")
        print("5. Видалити завдання")
        print("0. Вийти")

        choice = input("\nВиберіть дію: ")

        if choice == "1":
            title = input("Назва завдання: ")
            description = input("Опис: ")
            deadline = input("Дедлайн (напр. 2023-12-31): ")
            manager.add_task(title, description, deadline)

        elif choice == "2":
            manager.show_all_tasks()

        elif choice == "3":
            manager.show_pending_tasks()

        elif choice == "4":
            title = input("Назва завдання для відмітки: ")
            manager.mark_task_as_done(title)

        elif choice == "5":
            title = input("Назва завдання для видалення: ")
            manager.remove_task(title)

        elif choice == "0":
            print("\n До побачення!")
            break

        else:
            print("\n Невірний вибір, спробуйте ще раз!")


if __name__ == "__main__":
    main()