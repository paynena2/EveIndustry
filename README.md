# EveIndustry
TL:DR
Python program to scrape the market data for use in other applications

Why?
My friend and I wanted a reliable way to scrape the most up-to-date market information for the online MMO "Eve Online" in order to be used in deciding what to produce for profit, and where we can make good trade deals.

How?
I created this application to interface with the evemarketer API that tracks the real time statistics in the eve market. The program takes in a csv file with the ID's of all the marketable objects in game, as well as the name. The program stores these, and then uses the typeID's to perform a GET request on evemarketer's REST API. The request returns an xml file with all of the necessary information about each item that can be sold on the market. All that is left is to put that information into a csv file and pass it in to another application in order to analyze the data.

How to use this program?

Download the exe file and the input csv file, store them in the same directory. Run the exe, and it will output a csv that stores various attributes about each item.

Exapandability:

If Eve Online ever adds new items to the game, the input csv file can be updated with the id and the name of each item, and will produce an output for the new items.
