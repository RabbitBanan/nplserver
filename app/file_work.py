import json

# создание json файла по указаному пути (path) c информацие (data)
def create_json(path: str, data: dict):
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    return 1

# чтение json файла по указаному пути (path) и возращает словарь
def write_json(path: str) -> dict:
    with open(path, 'r', encoding="utf8") as f:
        return json.load(f)

# удаления json файла по указаному пути (path)
def delete_json(path: str):
    pass