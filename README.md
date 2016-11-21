# csv_parser_python
A quick python script to parse csv file to perform data manipulation on the parsed data

We have a csv file that looks like this

```csv
Id,Vendor,Product Name,Product Code,Unit,Weight,Price
1,Vendor1,Coriander Leaves (April-Nov),3736,Kg,3,90
2,Vendor1,Mint Leaves 500 Gm,4371,Grams,500,27.5
3,Vendor1,Ginger 500 Gm,4356,Grams,500,29.5
4,Vendor1,Lemon 500 Gm,4365,Grams,500,32.5
5,Vendor2,Coriander Leaves (April-Nov),3736,Kg,3,80
6,Vendor2,Mint Leaves 500 Gm,4371,Grams,500,27.5
7,Vendor2,Ginger 500 Gm,4356,Grams,500,30
8,Vendor2,Lemon 500 Gm,4365,Grams,500,31
9,Vendor3,Coriander Leaves (April-Nov),3736,Kg,3,88
10,Vendor3,Mint Leaves 500 Gm,4371,Grams,500,27.3
11,Vendor3,Ginger 500 Gm,4356,Grams,500,29.7
12,Vendor3,Lemon 500 Gm,4365,Grams,500,34.5
..
..
..

i.e., product list from multiple vendors and their price offerrings
```

Unfortunately, the file is consolidated and we need a better way to extract useful information.

We would like to be able to generate a product list based on:

    - cheapest prices
    - expensive prices
    - get cheapest price list only for given product IDs [3736, 4356, 3732, 3746, 3759, 3719, 3740, 4341]

For example, for cheapest prices, we would get a list like:
```code
    3,Vendor1,Ginger 500 Gm,4356,Grams,500,29.5
    5,Vendor2,Coriander Leaves (April-Nov),3736,Kg,3,80
    8,Vendor2,Lemon 500 Gm,4365,Grams,500,31
    10,Vendor3,Mint Leaves 500 Gm,4371,Grams,500,27.3
```

# Usage
```python
>>> python products.py
