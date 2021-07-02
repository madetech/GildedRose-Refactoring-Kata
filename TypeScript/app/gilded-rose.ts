const MAX_QUALITY = 50;

export class Item {
    name: string;
    sellIn: number;
    quality: number;

    constructor(name, sellIn, quality) {
        this.name = name;
        this.sellIn = sellIn;
        this.quality = quality;
    }
}

export class GildedRose {
    items: Array<Item>;

    constructor(items = [] as Array<Item>) {
        this.items = items;
    }

    updateQuality() {
        for (let i = 0; i < this.items.length; i++) {
            if (this.items[i].name == 'Sulfuras, Hand of Ragnaros') {
                continue;
            }
            if (this.items[i].name != 'Aged Brie' && this.items[i].name != 'Backstage passes to a TAFKAL80ETC concert') {
                this.reduceQuality(this.items[i]);
            } else {
                this.increaseQualityIfQualityUnderCap(this.items[i]);

                if (this.items[i].name == 'Backstage passes to a TAFKAL80ETC concert') {
                    if (this.items[i].sellIn < 11) {
                        this.increaseQualityIfQualityUnderCap(this.items[i]);
                    }
                    if (this.items[i].sellIn < 6) {
                        this.increaseQualityIfQualityUnderCap(this.items[i]);
                    }
                }

            }
            this.items[i].sellIn = this.items[i].sellIn - 1;
            if (this.items[i].sellIn < 0) {
                if (this.items[i].name != 'Aged Brie') {
                    if (this.items[i].name != 'Backstage passes to a TAFKAL80ETC concert') {
                        this.reduceQuality(this.items[i]);
                    } else {
                        this.items[i].quality = 0;
                    }
                } else {
                    this.increaseQualityIfQualityUnderCap(this.items[i]);
                }
            }
        }

        return this.items;
    }

    reduceQuality(item) {
        if (item.quality > 0) {
            item.quality = item.quality -1;
        }
    }

    increaseQualityIfQualityUnderCap(item) {
        if (item.quality < MAX_QUALITY) {
            item.quality = item.quality + 1;
        }
    }
}
