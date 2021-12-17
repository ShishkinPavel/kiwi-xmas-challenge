import dataCollecter
import argparse

parser = argparse.ArgumentParser(
    prog="app.py",
    usage="%(prog)s csv_file FROM TO"
    "[--bags=count] [--return]",
)
parser.add_argument(
    "csv_file", type=str, help='Data file path. For example "example/example0.csv"'
)
parser.add_argument(
    "FROM", type=str, help="Departure station in IATA format, for example PRG"
)
parser.add_argument(
    "TO", type=str, help="Destination station in IATA format, for example VKO"
)

parser.add_argument(
    "--bags", type=int, required=False, default=0, help="Count of bags, default=0"
)
parser.add_argument(
    "--return",
    dest="back",
    type=bool,
    nargs="?",
    required=False,
    const=True,
    default=False,
    help="Entered if you need a return ticket",
)

args = parser.parse_args()


x = dataCollecter.get_data(
    args.FROM.upper(), args.TO.upper(), args.bags, args.csv_file, args.back
)
if x:
    print(*x)
else:
    print("There are no tickets for this parameters")
