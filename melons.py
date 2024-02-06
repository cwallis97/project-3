import csv

class Melon:

    def __init__(self, melon_id, common_name, price, image_url, color, seedless):
        self.melon_id = melon_id
        self.common_name = common_name
        self.price = price
        self.image_url = image_url
        self.color = color
        self.seedless = seedless

    def __repr__(self):
        return f"<Melon: {self.melon_id}, {self.common_name}>"

    def price_str(self):
        return f"${self.price:.2f}"


melon_dict = {}

with open("melons.csv") as csvfile:
    rows = csv.DictReader(csvfile)
    for row in rows:
        row['price'] = float(row['price'])
        row['seedless'] = row['seedless'].lower() == 'true'
        melon = Melon(
            row['melon_id'],
            row['common_name'],
            row['price'],
            row['image_url'],
            row['color'],
            row['seedless']
        )
        melon_dict[row['melon_id']] = melon


def get_melon_by_id(melon_id):
    return melon_dict.get(melon_id)


def get_all_melons():
    return list(melon_dict.values())


for melon_id, melon_object in melon_dict.items():
    print(melon_object)


melon_id_to_lookup = 'cren'
found_melon = get_melon_by_id(melon_id_to_lookup)
print(f"\nFound Melon: {found_melon}")


all_melons = get_all_melons()
print("\nAll Melons:")
for melon in all_melons:
    print(melon)
