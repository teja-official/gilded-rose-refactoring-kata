# -*- coding: utf-8 -*-


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class GildedRose:
    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            self.update_item(item)

    def handle_aged_brie(self, item):
        item.quality = min(50, item.quality + 1)

    def handle_backstage_passes(self, item):
        if item.sell_in < 0:
            item.quality = 0
        elif item.sell_in < 5:
            item.quality = min(50, item.quality + 3)
        elif item.sell_in < 10:
            item.quality = min(50, item.quality + 2)
        else:
            item.quality = min(50, item.quality + 1)

    def handle_conjured(self, item):
        item.quality = max(0, item.quality - 2)

    def handle_others(self, item):
        item.quality = max(0, item.quality - 1)

    def handle_sell_in_low(self, item):
        if item.name == "Aged Brie":
            item.quality = min(50, item.quality + 1)
        elif item.name == "Backstage passes to a TAFKAL80ETC concert":
            item.quality = 0
        elif item.name.startswith("Conjured"):
            item.quality = max(0, item.quality - 2)
        else:
            item.quality = max(0, item.quality - 1)

    def update_item(self, item: Item):
        if item.name == "Sulfuras, Hand of Ragnaros":
            return

        item.sell_in -= 1

        if item.name == "Aged Brie":
            self.handle_aged_brie(item)
        elif item.name == "Backstage passes to a TAFKAL80ETC concert":
            self.handle_backstage_passes(item)
        elif item.name.startswith("Conjured"):
            self.handle_conjured(item)
        else:
            self.handle_others(item)

        if item.sell_in < 0:
            self.handle_sell_in_low(item)
