# [x, y]; x = number of people getting on bus, y = number of people getting off bus
# return the number of people on the bus at the last stop

def number(bus_stops):
    people_on_bus = 0
    for stop in bus_stops:
        people_on_bus += stop[0] - stop[1]
    return people_on_bus

number([[10,0],[3,5],[5,8]])
number([[3,0],[9,1],[4,10],[12,2],[6,1],[7,10]])
number([[3,0],[9,1],[4,8],[12,2],[6,1],[7,8]])
