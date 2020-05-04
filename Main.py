import requests
import csv
import xml.etree.ElementTree as ET

class Item:
    def __init__(self, id, name, buyvol, sellvol, buymax, sellmin, buyavg, sellavg, buymed, sellmed):
        self.id = id
        self.name = name
        self.buyvol = buyvol
        self.sellvol = sellvol
        self.buymax = buymax
        self.sellmin = sellmin
        self.buyavg = buyavg
        self.sellavg = sellavg
        self.buymed = buymed
        self.sellmed = sellmed

def main():
    itemlist = []
    csvdata = {}
    with open('invTypes.csv', 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            for line in csv_reader:
                value = {line[0] : line[1]}
                csvdata.update(value)
    count = 0
    many = 0
    elements = {}
    for key in csvdata:
        x = {key: csvdata.get(key)}
        elements.update(x)
        count += 1
        many += 1
        if count == 199:
            itemlist = getData(elements, itemlist, csvdata)
            count = 0
            elements.clear()
    if count != 0:
        itemlist = getData(elements, itemlist, csvdata)
        elements.clear()

    with open('outputdata.csv', 'w', newline='') as output:
        writer = csv.writer(output)
        writer.writerow(["id", "name", "buy volume", "sell volume", "buy max", "sell min", "buy avg", "sell avg", "buy median", "sell median"])
        for i in itemlist:
            datalist = [i.id, i.name, i.buyvol, i.sellvol, i.buymax, i.sellmin, i.buyavg, i.sellavg, i.buymed, i.sellmed]
            writer.writerow(datalist)

def getData(elements, itemlist, csvdata):
    baseurl = "https://api.evemarketer.com/ec"
    mstat = "/marketstat?"
    typeid = "typeid="
    system = "usesystem=30000142"

    getUrl = baseurl + mstat

    for key in elements:
        getUrl += typeid + key + "&"
    getUrl += system

    x = requests.get(getUrl)
    root = ET.fromstring(x.content)

    #Todo, create objects and populate CSV
    #id, name, buyvol, sellvol, buymax, sellmin, buyavg, sellavg, buymed, sellmed
    ids = root.findall('marketstat/type')

    for i in ids:
        id = i.get('id')
        b = i.find('buy')
        s = i.find('sell')

        buyvol = b.find('volume').text
        buymax = b.find('max').text
        buyavg = b.find('avg').text
        buymed = b.find('median').text

        sellvol = s.find('volume').text
        sellmin = s.find('min').text
        sellavg = s.find('avg').text
        sellmed = s.find('median').text

        name = csvdata.get(id)

        itemlist.append(Item(id, name, buyvol, sellvol, buymax, sellmin, buyavg, sellavg, buymed, sellmed))
    return itemlist



main()