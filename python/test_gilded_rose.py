# -*- coding: utf-8 -*-
import unittest

from approvaltests.approvals import verify
from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    items = [
        Item(name="+5 Dexterity Vest", sell_in=10, quality=20),
        Item(name="Aged Brie", sell_in=2, quality=0),
        Item(name="Elixir of the Mongoose", sell_in=5, quality=7),
        Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80),
        Item(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=80),
        Item(name="Backstage passes to a TAFKAL80ETC concert",
             sell_in=15, quality=20),
        Item(name="Backstage passes to a TAFKAL80ETC concert",
             sell_in=10, quality=49),
        Item(name="Backstage passes to a TAFKAL80ETC concert",
             sell_in=5, quality=49),
        Item(name="Conjured Mana Cake", sell_in=3, quality=6),  # <-- :O
    ]

    def test_verify_update_quality(self):
        GildedRose(self.items).update_quality()
        verify(self.items)

    def test_verify_update_quality_multiple_days(self):
        days = 15
        for day in range(days):
            GildedRose(self.items).update_quality()
        verify(self.items)

    def test_concert_passes(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 10, 48)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(
            "Backstage passes to a TAFKAL80ETC concert", items[0].name)
        self.assertEquals(50, items[0].quality)
        self.assertEquals(9, items[0].sell_in)

    def test_concert_passes_in_five_days(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 5, 47)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(
            "Backstage passes to a TAFKAL80ETC concert", items[0].name)
        self.assertEquals(50, items[0].quality)
        self.assertEquals(4, items[0].sell_in)

    def test_concert_passes_in_six_days(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 6, 47)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(
            "Backstage passes to a TAFKAL80ETC concert", items[0].name)
        self.assertEquals(49, items[0].quality)
        self.assertEquals(5, items[0].sell_in)

    def test_concert_passes_in_eleven_days(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 11, 47)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(
            "Backstage passes to a TAFKAL80ETC concert", items[0].name)
        self.assertEquals(48, items[0].quality)
        self.assertEquals(10, items[0].sell_in)


if __name__ == '__main__':
    unittest.main()
