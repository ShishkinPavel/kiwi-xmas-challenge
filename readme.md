# Solved python weekend entry task

This code allows you to find tickets from point A to point B with all possible transfers using information from a CSV file

## Usage examples

Help:
```
python3 -m solution -h
```
Output:
```
usage: app.py csv_file FROM TO[--bags=count] [--return]

positional arguments:
  csv_file         Data file path. For example "example/example0.csv"
  FROM             Departure station in IATA format, for example PRG
  TO               Destination station in IATA format, for example VKO

options:
  -h, --help       show this help message and exit
  --bags BAGS      Count of bags, default=0
  --return [BACK]  Entered if you need a return ticket

```
If you don't need a ticket back:

```
python3 -m solution example/example0.csv ECV RFZ --bags=1
```
Output:
```
{
    "flight": [
        {
            "flight_no": "ZH665",
            "origin": "ECV",
            "destination": "RFZ",
            "departure": "2021-09-01T12:10:00",
            "arrival": "2021-09-01T14:40:00",
            "base_price": 58.0,
            "bag_price": 12,
            "bags_allowed": 2
        }
    ],
    "bags_allowed": 2,
    "bags_count": 1,
    "destination": "RFZ",
    "origin": "ECV",
    "total_price": 70.0,
    "travel_time": "2:30:00"
} {
    "flight": [
        {
            "flight_no": "ZH151",
            "origin": "ECV",
            "destination": "WIW",
            "departure": "2021-09-01T15:35:00",
            "arrival": "2021-09-01T20:45:00",
            "base_price": 245.0,
            "bag_price": 12,
            "bags_allowed": 2
        },
        {
            "flight_no": "ZH214",
            "origin": "WIW",
            "destination": "RFZ",
            "departure": "2021-09-01T23:20:00",
            "arrival": "2021-09-02T03:50:00",
            "base_price": 168.0,
            "bag_price": 12,
            "bags_allowed": 2
        }
    ],
    "bags_allowed": 2,
    "bags_count": 1,
    "destination": "RFZ",
    "origin": "ECV",
    "total_price": 437.0,
    "travel_time": "12:15:00"
} {
    "flight": [
        {
            "flight_no": "ZH665",
            "origin": "ECV",
            "destination": "RFZ",
            "departure": "2021-09-02T12:10:00",
            "arrival": "2021-09-02T14:40:00",
            "base_price": 58.0,
            "bag_price": 12,
            "bags_allowed": 2
        }
    ],
    "bags_allowed": 2,
    "bags_count": 1,
    "destination": "RFZ",
    "origin": "ECV",
    "total_price": 70.0,
    "travel_time": "2:30:00"
} {
    "flight": [
        {
            "flight_no": "ZH665",
            "origin": "ECV",
            "destination": "RFZ",
            "departure": "2021-09-05T12:10:00",
            "arrival": "2021-09-05T14:40:00",
            "base_price": 58.0,
            "bag_price": 12,
            "bags_allowed": 2
        }
    ],
    "bags_allowed": 2,
    "bags_count": 1,
    "destination": "RFZ",
    "origin": "ECV",
    "total_price": 70.0,
    "travel_time": "2:30:00"
} {
    "flight": [
        {
            "flight_no": "ZH665",
            "origin": "ECV",
            "destination": "RFZ",
            "departure": "2021-09-09T12:10:00",
            "arrival": "2021-09-09T14:40:00",
            "base_price": 58.0,
            "bag_price": 12,
            "bags_allowed": 2
        }
    ],
    "bags_allowed": 2,
    "bags_count": 1,
    "destination": "RFZ",
    "origin": "ECV",
    "total_price": 70.0,
    "travel_time": "2:30:00"
} {
    "flight": [
        {
            "flight_no": "ZH665",
            "origin": "ECV",
            "destination": "RFZ",
            "departure": "2021-09-15T12:10:00",
            "arrival": "2021-09-15T14:40:00",
            "base_price": 58.0,
            "bag_price": 12,
            "bags_allowed": 2
        }
    ],
    "bags_allowed": 2,
    "bags_count": 1,
    "destination": "RFZ",
    "origin": "ECV",
    "total_price": 70.0,
    "travel_time": "2:30:00"
}

```

If you need a ticket back:
```
python3 -m solution example/example0.csv ECV RFZ --bags=1 --return
```
Output:
```
{
    "flight": [
        {
            "flight_no": "ZH665",
            "origin": "ECV",
            "destination": "RFZ",
            "departure": "2021-09-01T12:10:00",
            "arrival": "2021-09-01T14:40:00",
            "base_price": 58.0,
            "bag_price": 12,
            "bags_allowed": 2
        },
        {
            "flight_no": "ZH665",
            "origin": "RFZ",
            "destination": "ECV",
            "departure": "2021-09-01T17:40:00",
            "arrival": "2021-09-01T20:10:00",
            "base_price": 58.0,
            "bag_price": 12,
            "bags_allowed": 2
        }
    ],
    "bags_allowed": 2,
    "bags_count": 1,
    "destination": "RFZ",
    "origin": "ECV",
    "total_price": 140.0,
    "travel_time": "5:00:00"
} {
    "flight": [
        {
            "flight_no": "ZH665",
            "origin": "ECV",
            "destination": "RFZ",
            "departure": "2021-09-01T12:10:00",
            "arrival": "2021-09-01T14:40:00",
            "base_price": 58.0,
            "bag_price": 12,
            "bags_allowed": 2
        },
        {
            "flight_no": "ZH665",
            "origin": "RFZ",
            "destination": "ECV",
            "departure": "2021-09-02T17:40:00",
            "arrival": "2021-09-02T20:10:00",
            "base_price": 58.0,
            "bag_price": 12,
            "bags_allowed": 2
        }
    ],
    "bags_allowed": 2,
    "bags_count": 1,
    "destination": "RFZ",
    "origin": "ECV",
    "total_price": 140.0,
    "travel_time": "5:00:00"
} {
    "flight": [
        {
            "flight_no": "ZH665",
            "origin": "ECV",
            "destination": "RFZ",
            "departure": "2021-09-01T12:10:00",
            "arrival": "2021-09-01T14:40:00",
            "base_price": 58.0,
            "bag_price": 12,
            "bags_allowed": 2
        },
        {
            "flight_no": "ZH665",
            "origin": "RFZ",
            "destination": "ECV",
            "departure": "2021-09-05T17:40:00",
            "arrival": "2021-09-05T20:10:00",
            "base_price": 58.0,
            "bag_price": 12,
            "bags_allowed": 2
        }
    ],
    "bags_allowed": 2,
    "bags_count": 1,
    "destination": "RFZ",
    "origin": "ECV",
    "total_price": 140.0,
    "travel_time": "5:00:00"
} {
    "flight": [
        {
            "flight_no": "ZH665",
            "origin": "ECV",
            "destination": "RFZ",
            "departure": "2021-09-01T12:10:00",
            "arrival": "2021-09-01T14:40:00",
            "base_price": 58.0,
            "bag_price": 12,
            "bags_allowed": 2
        },
        {
            "flight_no": "ZH665",
            "origin": "RFZ",
            "destination": "ECV",
            "departure": "2021-09-09T17:40:00",
            "arrival": "2021-09-09T20:10:00",
            "base_price": 58.0,
            "bag_price": 12,
            "bags_allowed": 2
        }
    ],
    "bags_allowed": 2,
    "bags_count": 1,
    "destination": "RFZ",
    "origin": "ECV",
    "total_price": 140.0,
    "travel_time": "5:00:00"
} {
    "flight": [
        {
            "flight_no": "ZH665",
            "origin": "ECV",
            "destination": "RFZ",
            "departure": "2021-09-01T12:10:00",
            "arrival": "2021-09-01T14:40:00",
            "base_price": 58.0,
            "bag_price": 12,
            "bags_allowed": 2
        },
        {
            "flight_no": "ZH665",
            "origin": "RFZ",
            "destination": "ECV",
            "departure": "2021-09-15T17:40:00",
            "arrival": "2021-09-15T20:10:00",
            "base_price": 58.0,
            "bag_price": 12,
            "bags_allowed": 2
        }
    ],
    "bags_allowed": 2,
    "bags_count": 1,
    "destination": "RFZ",
    "origin": "ECV",
    "total_price": 140.0,
    "travel_time": "5:00:00"
} {
    "flight": [
        {
            "flight_no": "ZH151",
            "origin": "ECV",
            "destination": "WIW",
            "departure": "2021-09-01T15:35:00",
            "arrival": "2021-09-01T20:45:00",
            "base_price": 245.0,
            "bag_price": 12,
            "bags_allowed": 2
        },
        {
            "flight_no": "ZH214",
            "origin": "WIW",
            "destination": "RFZ",
            "departure": "2021-09-01T23:20:00",
            "arrival": "2021-09-02T03:50:00",
            "base_price": 168.0,
            "bag_price": 12,
            "bags_allowed": 2
        },
        {
            "flight_no": "ZH665",
            "origin": "RFZ",
            "destination": "ECV",
            "departure": "2021-09-02T17:40:00",
            "arrival": "2021-09-02T20:10:00",
            "base_price": 58.0,
            "bag_price": 12,
            "bags_allowed": 2
        }
    ],
    "bags_allowed": 2,
    "bags_count": 1,
    "destination": "RFZ",
    "origin": "ECV",
    "total_price": 507.0,
    "travel_time": "14:45:00"
} {
    "flight": [
        {
            "flight_no": "ZH151",
            "origin": "ECV",
            "destination": "WIW",
            "departure": "2021-09-01T15:35:00",
            "arrival": "2021-09-01T20:45:00",
            "base_price": 245.0,
            "bag_price": 12,
            "bags_allowed": 2
        },
        {
            "flight_no": "ZH214",
            "origin": "WIW",
            "destination": "RFZ",
            "departure": "2021-09-01T23:20:00",
            "arrival": "2021-09-02T03:50:00",
            "base_price": 168.0,
            "bag_price": 12,
            "bags_allowed": 2
        },
        {
            "flight_no": "ZH665",
            "origin": "RFZ",
            "destination": "ECV",
            "departure": "2021-09-05T17:40:00",
            "arrival": "2021-09-05T20:10:00",
            "base_price": 58.0,
            "bag_price": 12,
            "bags_allowed": 2
        }
    ],
    "bags_allowed": 2,
    "bags_count": 1,
    "destination": "RFZ",
    "origin": "ECV",
    "total_price": 507.0,
    "travel_time": "14:45:00"
} {
    "flight": [
        {
            "flight_no": "ZH151",
            "origin": "ECV",
            "destination": "WIW",
            "departure": "2021-09-01T15:35:00",
            "arrival": "2021-09-01T20:45:00",
            "base_price": 245.0,
            "bag_price": 12,
            "bags_allowed": 2
        },
        {
            "flight_no": "ZH214",
            "origin": "WIW",
            "destination": "RFZ",
            "departure": "2021-09-01T23:20:00",
            "arrival": "2021-09-02T03:50:00",
            "base_price": 168.0,
            "bag_price": 12,
            "bags_allowed": 2
        },
        {
            "flight_no": "ZH665",
            "origin": "RFZ",
            "destination": "ECV",
            "departure": "2021-09-09T17:40:00",
            "arrival": "2021-09-09T20:10:00",
            "base_price": 58.0,
            "bag_price": 12,
            "bags_allowed": 2
        }
    ],
    "bags_allowed": 2,
    "bags_count": 1,
    "destination": "RFZ",
    "origin": "ECV",
    "total_price": 507.0,
    "travel_time": "14:45:00"
} {
    "flight": [
        {
            "flight_no": "ZH151",
            "origin": "ECV",
            "destination": "WIW",
            "departure": "2021-09-01T15:35:00",
            "arrival": "2021-09-01T20:45:00",
            "base_price": 245.0,
            "bag_price": 12,
            "bags_allowed": 2
        },
        {
            "flight_no": "ZH214",
            "origin": "WIW",
            "destination": "RFZ",
            "departure": "2021-09-01T23:20:00",
            "arrival": "2021-09-02T03:50:00",
            "base_price": 168.0,
            "bag_price": 12,
            "bags_allowed": 2
        },
        {
            "flight_no": "ZH665",
            "origin": "RFZ",
            "destination": "ECV",
            "departure": "2021-09-15T17:40:00",
            "arrival": "2021-09-15T20:10:00",
            "base_price": 58.0,
            "bag_price": 12,
            "bags_allowed": 2
        }
    ],
    "bags_allowed": 2,
    "bags_count": 1,
    "destination": "RFZ",
    "origin": "ECV",
    "total_price": 507.0,
    "travel_time": "14:45:00"
} {
    "flight": [
        {
            "flight_no": "ZH665",
            "origin": "ECV",
            "destination": "RFZ",
            "departure": "2021-09-02T12:10:00",
            "arrival": "2021-09-02T14:40:00",
            "base_price": 58.0,
            "bag_price": 12,
            "bags_allowed": 2
        },
        {
            "flight_no": "ZH665",
            "origin": "RFZ",
            "destination": "ECV",
            "departure": "2021-09-02T17:40:00",
            "arrival": "2021-09-02T20:10:00",
            "base_price": 58.0,
            "bag_price": 12,
            "bags_allowed": 2
        }
    ],
    "bags_allowed": 2,
    "bags_count": 1,
    "destination": "RFZ",
    "origin": "ECV",
    "total_price": 140.0,
    "travel_time": "5:00:00"
} {
    "flight": [
        {
            "flight_no": "ZH665",
            "origin": "ECV",
            "destination": "RFZ",
            "departure": "2021-09-02T12:10:00",
            "arrival": "2021-09-02T14:40:00",
            "base_price": 58.0,
            "bag_price": 12,
            "bags_allowed": 2
        },
        {
            "flight_no": "ZH665",
            "origin": "RFZ",
            "destination": "ECV",
            "departure": "2021-09-05T17:40:00",
            "arrival": "2021-09-05T20:10:00",
            "base_price": 58.0,
            "bag_price": 12,
            "bags_allowed": 2
        }
    ],
    "bags_allowed": 2,
    "bags_count": 1,
    "destination": "RFZ",
    "origin": "ECV",
    "total_price": 140.0,
    "travel_time": "5:00:00"
} {
    "flight": [
        {
            "flight_no": "ZH665",
            "origin": "ECV",
            "destination": "RFZ",
            "departure": "2021-09-02T12:10:00",
            "arrival": "2021-09-02T14:40:00",
            "base_price": 58.0,
            "bag_price": 12,
            "bags_allowed": 2
        },
        {
            "flight_no": "ZH665",
            "origin": "RFZ",
            "destination": "ECV",
            "departure": "2021-09-09T17:40:00",
            "arrival": "2021-09-09T20:10:00",
            "base_price": 58.0,
            "bag_price": 12,
            "bags_allowed": 2
        }
    ],
    "bags_allowed": 2,
    "bags_count": 1,
    "destination": "RFZ",
    "origin": "ECV",
    "total_price": 140.0,
    "travel_time": "5:00:00"
} {
    "flight": [
        {
            "flight_no": "ZH665",
            "origin": "ECV",
            "destination": "RFZ",
            "departure": "2021-09-02T12:10:00",
            "arrival": "2021-09-02T14:40:00",
            "base_price": 58.0,
            "bag_price": 12,
            "bags_allowed": 2
        },
        {
            "flight_no": "ZH665",
            "origin": "RFZ",
            "destination": "ECV",
            "departure": "2021-09-15T17:40:00",
            "arrival": "2021-09-15T20:10:00",
            "base_price": 58.0,
            "bag_price": 12,
            "bags_allowed": 2
        }
    ],
    "bags_allowed": 2,
    "bags_count": 1,
    "destination": "RFZ",
    "origin": "ECV",
    "total_price": 140.0,
    "travel_time": "5:00:00"
} {
    "flight": [
        {
            "flight_no": "ZH665",
            "origin": "ECV",
            "destination": "RFZ",
            "departure": "2021-09-05T12:10:00",
            "arrival": "2021-09-05T14:40:00",
            "base_price": 58.0,
            "bag_price": 12,
            "bags_allowed": 2
        },
        {
            "flight_no": "ZH665",
            "origin": "RFZ",
            "destination": "ECV",
            "departure": "2021-09-05T17:40:00",
            "arrival": "2021-09-05T20:10:00",
            "base_price": 58.0,
            "bag_price": 12,
            "bags_allowed": 2
        }
    ],
    "bags_allowed": 2,
    "bags_count": 1,
    "destination": "RFZ",
    "origin": "ECV",
    "total_price": 140.0,
    "travel_time": "5:00:00"
} {
    "flight": [
        {
            "flight_no": "ZH665",
            "origin": "ECV",
            "destination": "RFZ",
            "departure": "2021-09-05T12:10:00",
            "arrival": "2021-09-05T14:40:00",
            "base_price": 58.0,
            "bag_price": 12,
            "bags_allowed": 2
        },
        {
            "flight_no": "ZH665",
            "origin": "RFZ",
            "destination": "ECV",
            "departure": "2021-09-09T17:40:00",
            "arrival": "2021-09-09T20:10:00",
            "base_price": 58.0,
            "bag_price": 12,
            "bags_allowed": 2
        }
    ],
    "bags_allowed": 2,
    "bags_count": 1,
    "destination": "RFZ",
    "origin": "ECV",
    "total_price": 140.0,
    "travel_time": "5:00:00"
} {
    "flight": [
        {
            "flight_no": "ZH665",
            "origin": "ECV",
            "destination": "RFZ",
            "departure": "2021-09-05T12:10:00",
            "arrival": "2021-09-05T14:40:00",
            "base_price": 58.0,
            "bag_price": 12,
            "bags_allowed": 2
        },
        {
            "flight_no": "ZH665",
            "origin": "RFZ",
            "destination": "ECV",
            "departure": "2021-09-15T17:40:00",
            "arrival": "2021-09-15T20:10:00",
            "base_price": 58.0,
            "bag_price": 12,
            "bags_allowed": 2
        }
    ],
    "bags_allowed": 2,
    "bags_count": 1,
    "destination": "RFZ",
    "origin": "ECV",
    "total_price": 140.0,
    "travel_time": "5:00:00"
} {
    "flight": [
        {
            "flight_no": "ZH665",
            "origin": "ECV",
            "destination": "RFZ",
            "departure": "2021-09-09T12:10:00",
            "arrival": "2021-09-09T14:40:00",
            "base_price": 58.0,
            "bag_price": 12,
            "bags_allowed": 2
        },
        {
            "flight_no": "ZH665",
            "origin": "RFZ",
            "destination": "ECV",
            "departure": "2021-09-09T17:40:00",
            "arrival": "2021-09-09T20:10:00",
            "base_price": 58.0,
            "bag_price": 12,
            "bags_allowed": 2
        }
    ],
    "bags_allowed": 2,
    "bags_count": 1,
    "destination": "RFZ",
    "origin": "ECV",
    "total_price": 140.0,
    "travel_time": "5:00:00"
} {
    "flight": [
        {
            "flight_no": "ZH665",
            "origin": "ECV",
            "destination": "RFZ",
            "departure": "2021-09-09T12:10:00",
            "arrival": "2021-09-09T14:40:00",
            "base_price": 58.0,
            "bag_price": 12,
            "bags_allowed": 2
        },
        {
            "flight_no": "ZH665",
            "origin": "RFZ",
            "destination": "ECV",
            "departure": "2021-09-15T17:40:00",
            "arrival": "2021-09-15T20:10:00",
            "base_price": 58.0,
            "bag_price": 12,
            "bags_allowed": 2
        }
    ],
    "bags_allowed": 2,
    "bags_count": 1,
    "destination": "RFZ",
    "origin": "ECV",
    "total_price": 140.0,
    "travel_time": "5:00:00"
} {
    "flight": [
        {
            "flight_no": "ZH665",
            "origin": "ECV",
            "destination": "RFZ",
            "departure": "2021-09-15T12:10:00",
            "arrival": "2021-09-15T14:40:00",
            "base_price": 58.0,
            "bag_price": 12,
            "bags_allowed": 2
        },
        {
            "flight_no": "ZH665",
            "origin": "RFZ",
            "destination": "ECV",
            "departure": "2021-09-15T17:40:00",
            "arrival": "2021-09-15T20:10:00",
            "base_price": 58.0,
            "bag_price": 12,
            "bags_allowed": 2
        }
    ],
    "bags_allowed": 2,
    "bags_count": 1,
    "destination": "RFZ",
    "origin": "ECV",
    "total_price": 140.0,
    "travel_time": "5:00:00"
}
```

If there are no tickets for this parameters:
```
python3 -m solution example/example3.csv ECV RFZ
```
Output:
```
There are no tickets for this parameters
```

## Contributing
The code doesn't look perfect, but it works, any code review or tips will make me better!
