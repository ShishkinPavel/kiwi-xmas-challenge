import json
from datetime import datetime, timedelta


def find_fly(original, destination, bag, data, date, back=False):
    result, result_back = [], []
    count = 1  # I keep count for the list slice during recursion
    for i in data:
        if (
            i["origin"] == original and datetime.fromisoformat(i["departure"]) >= date
        ):  # check for departure point and departure date
            if (
                i["destination"] == destination and i["bags_allowed"] >= bag
            ):  # baggage check and arrival place

                if back:  # If need a return ticket, then run a recursion
                    x = find_fly(
                        destination,
                        original,
                        bag,
                        data[count:],
                        datetime.fromisoformat(i["arrival"]) + timedelta(hours=1),
                    )
                    if (
                        x
                    ):  # There may not be return tickets, so we do a check before adding a route
                        [
                            result.append(
                                json.dumps(
                                    {"flight": [i] + json.loads(j)["flight"]}, indent=4
                                )
                            )
                            for j in x
                        ]

                # If the ticket is direct and you don't need a return ticket, then just add it to the list
                else:
                    result.append(json.dumps({"flight": [i]}, indent=4))

            # If the departure point is the same, but the arrival point is not,
            # then need to check for transfers
            else:
                transfer_date = find_transfer(
                    data[count:],
                    i["destination"],
                    destination,
                    bag,
                    i["arrival"],
                    [original],
                    [],
                )

                # the principle is similar to a direct flight, but here we have several tickets
                if back:
                    if transfer_date:
                        recursive_find_fly = find_fly(
                            destination,
                            original,
                            bag,
                            data[count:],
                            datetime.fromisoformat(transfer_date[-1][-1]["arrival"])
                            + timedelta(hours=1),
                        )
                        for k in recursive_find_fly:
                            [
                                result.append(
                                    json.dumps(
                                        {"flight": [i] + j + json.loads(k)["flight"]},
                                        indent=4,
                                    )
                                )
                                for j in transfer_date
                            ]
                else:
                    [
                        result.append(json.dumps({"flight": [i] + j}, indent=4))
                        for j in transfer_date
                    ]
        count += 1
    return result


def find_transfer(dat, original, destination, bag, time, array_of_airports, routes):
    result = []
    count = 1
    for i in dat:
        time_different = datetime.fromisoformat(
            i["departure"]
        ) - datetime.fromisoformat(time)

        # in case, for example, arrival 02. 09.2021 at 00:30, and departure 01.09.2021 at 23:00,
        # need to check that the ticket is of the current date
        if time_different >= timedelta(days=0):
            if timedelta(hours=1) <= time_different <= timedelta(hours=6):
                if (
                    i["origin"] == original
                    and i["destination"] not in array_of_airports
                    and i["bags_allowed"] >= bag
                ):

                    # if the destination matches, I add to the list all the tickets
                    # leading to it and the final ticket
                    if i["destination"] == destination:
                        result.append([j for j in routes + [i]])

                    # if the destination did not match, but the departure point did, I call a recursion,
                    # adding the airports passed and theoretically valid tickets
                    else:
                        recursive_find_transfer = find_transfer(
                            dat[count:],
                            i["destination"],
                            destination,
                            bag,
                            i["arrival"],
                            array_of_airports + [i["origin"]],
                            routes + [i],
                        )
                        [result.append(j) for j in recursive_find_transfer]
            # if the time difference is more than 6 hours, I exit the function
            elif timedelta(hours=6) < time_different:
                return result
        count += 1
