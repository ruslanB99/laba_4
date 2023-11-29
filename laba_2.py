# TODO импортировать необходимые молули
import csv
import json


INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    ...  # TODO считать содержимое csv файла
    with open(INPUT_FILENAME,encoding='utf-8') as f:
        reader=csv.DictReader(f,delimiter = ",", lineterminator="\r")
        results=list()

        #в каждой строчке line в reader  в формате
        # {название столбца1:значение из первой строки1,
        # название столбца2:значение из первой строки2}
        # в results все делаем в общий ключ
        for line in reader:
            results.append(line)



    ...  # TODO Сериализовать в файл с отступами равными 4
    return json.dumps(results,indent=4)

if __name__ == '__main__':
    # Нужно для проверки
    to_json=task()

    with open(OUTPUT_FILENAME,'w') as output_f:
        output_f.write(to_json)
    print(to_json,end="")

