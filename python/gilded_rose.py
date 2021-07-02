# -*- coding: utf-8 -*-

class GildedRose(object):

    QUALITY_THRESHOLD = 50
    QUALITY_FLOOR = 0

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:

            if item.name == "Sulfuras, Hand of Ragnaros":
                continue

            item.sell_in = item.sell_in - 1

            self.aged_brie(item)
            self.backstage_passes(item)
            self.others(item)

    def aged_brie(self, item):
        if item.name != "Aged Brie":
            return

        self.upgrade(item)
        if item.sell_in < 0:
            self.upgrade(item)

    def backstage_passes(self, item):
        if item.name != "Backstage passes to a TAFKAL80ETC concert":
            return

        self.upgrade(item)
        if item.quality <= self.QUALITY_THRESHOLD:
            if item.sell_in < 10:
                self.upgrade(item)
            if item.sell_in < 5:
                self.upgrade(item)
        if item.sell_in < 0:
            item.quality = self.QUALITY_FLOOR

    def others(self, item):
        if item.name == "Aged Brie" or item.name == "Backstage passes to a TAFKAL80ETC concert":
            return

        self.degrade(item)
        if item.sell_in < 0:
            self.degrade(item)

    def upgrade(self, item):
        if item.quality < self.QUALITY_THRESHOLD:
            item.quality = item.quality + 1

    def degrade(self, item):
        if item.quality > self.QUALITY_FLOOR:
            item.quality = item.quality - 1


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
