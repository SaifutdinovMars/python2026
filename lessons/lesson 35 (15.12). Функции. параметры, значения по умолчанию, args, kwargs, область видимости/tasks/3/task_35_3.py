"""Практическое задание 35.3: профили студентов."""


def create_student_profile(name, student_id, *args, **kwargs):
    """Собирает профиль студента.

    Ожидаемая структура словаря:
    {
        "name": str,
        "id": str,
        "test_scores": tuple,
        "attributes": dict,
    }
    """
    profile = {
        "name": name,
        "id": student_id,
        "test_scores": tuple(args),
        "attributes": dict(kwargs),
    }
    return profile


def print_profile(profile_dict):
    """Печатает профиль студента в требуемом формате."""
    name = profile_dict["name"]
    student_id = profile_dict["id"]
    test_scores = profile_dict["test_scores"]
    attributes = profile_dict["attributes"]

    print(f"Студент: {name} (ID: {student_id})")
    print(f"Оценки за тесты: {test_scores}")
    print(f"Дополнительно: {attributes}")


if __name__ == "__main__":
    # TODO: добавить примеры вызовов с разными наборами аргументов
    pass
