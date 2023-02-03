# ****************
# YELLOW SUBMARINE
# ****************
from pathlib import Path


def run(route_path: Path) -> tuple:

    with open(route_path, "r") as f:
        fuel = int(f.readline().strip())
        movements = f.readline().split(",")
        for movement in movements:
            dist_depth = movement.split(":")

    distance = depth = fuel = "output"

    return distance, depth, fuel


if __name__ == "__main__":
    run("data/submarine/route1.dat")
