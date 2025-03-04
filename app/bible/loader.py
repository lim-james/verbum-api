from csv import DictReader

def load_bible_from_csv(filepath):
    data = {}
    with open(filepath, mode="r", encoding="utf-8") as file:
        reader = DictReader(file)
        for row in reader:
            book = row["book"].lower()
            chapter = int(row["chapter"])
            verse = int(row["verse"])
            text = row["text"]

            if book not in data:
                data[book] = {}

            if chapter not in data[book]:
                data[book][chapter] = {}

            data[book][chapter][verse] = text

    return data
