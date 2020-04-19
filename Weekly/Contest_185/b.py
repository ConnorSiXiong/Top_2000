from typing import List


def displayTable(orders: List[List[str]]) -> List[List[str]]:

    result = []
    foods = []
    tables = []

    for order in orders:
        _, table, food = order
        if food not in foods:
            foods.append(food)
        if int(table) not in tables:
            tables.append(int(table))
    foods.sort()
    result.append(foods)

    tables.sort()

    dic = {}

    for table1 in tables:
        table1_order = []
        table1_order.append(table1)
        for dish in sorted(foods):
            dic[dish] = 0
        for order in orders:
            _, table2, food = order
            if table1 == int(table2):
                dic[food] += 1
        table1_order = table1_order + list(dic.values())
        table1_order = [str(i) for i in table1_order]
        result.append(table1_order)
    result[0].insert(0, "Table")
    return result





# orders = [["David","3","Ceviche"],["Corina","10","Beef Burrito"],["David","3","Fried Chicken"],["Carla","5","Water"],["Carla","5","Ceviche"],["Rous","3","Ceviche"]]
# orders = [["Laura","2","Bean Burrito"],["Jhon","2","Beef Burrito"],["Melissa","2","Soda"]]


# orders = [["James","12","Fried Chicken"],["Ratesh","12","Fried Chicken"],["Amadeus","12","Fried Chicken"],["Adam","1","Canadian Waffles"],["Brianna","1","Canadian Waffles"]]

orders = [["David","3","Ceviche"],
          ["Corina","10","Beef Burrito"],["David","3","Fried Chicken"],["Carla","5","Water"],["Carla","5","Ceviche"],["Rous","3","Ceviche"]]
print(displayTable(orders))