import json
from datetime import datetime, timedelta
from flights import find_fly


def get_csv_from_file(path):
    data = []
    with open(path) as file:
        head = file.readline().strip().split(",")
        lines = [i.strip().split(",") for i in file.readlines()]
        for i in lines:
            act = {}
            for j in range(len(i)):
                try:  # try get int for bag price and bag allowed
                    act[head[j]] = int(i[j])
                except ValueError:
                    try:  # try get float for price
                        act[head[j]] = float(i[j])
                    except ValueError:  # get other values as string
                        act[head[j]] = i[j]
            data.append(act)
    return data


# Just a function to change the output format, nothing special
def to_output_data(flight, bags, destination, dest_const):
    total_price = 0
    start_time = flight[0]["departure"]
    travel_time = timedelta(0)
    origin = flight[0]["origin"]
    bags_allowed = 999
    for i in flight:
        total_price += i["base_price"] + i["bag_price"] * bags
        if i["bags_allowed"] < bags_allowed:
            bags_allowed = i["bags_allowed"]
        if i["origin"] == destination:
            destination = origin
            start_time = i["departure"]
        if i["destination"] == destination:
            travel_time += datetime.fromisoformat(
                i["arrival"]
            ) - datetime.fromisoformat(start_time)

    result = json.dumps(
        {
            "flight": flight,
            "bags_allowed": bags_allowed,
            "bags_count": bags,
            "destination": dest_const,
            "origin": origin,
            "total_price": total_price,
            "travel_time": str(travel_time),
        },
        indent=4,
    )
    return result


def get_data(original, destination, bags, path, back):
    data = get_csv_from_file(path)
    start = datetime.fromisoformat(data[0]["departure"])

    result = []
    # for ind, i in enumerate(date_generated):
    res = find_fly(original, destination, bags, data, start, back)
    result += [
        to_output_data(json.loads(i)["flight"], bags, destination, destination)
        for i in res
    ]
    return result
