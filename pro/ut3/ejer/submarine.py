# ****************
# YELLOW SUBMARINE
# ****************
from pathlib import Path


def run(route_path: Path) -> tuple:

    with open(route_path, "r") as f:
        fuel = int(f.readline().strip())
        movements = f.readline().split(",")
        distance = 0
        depth = 0
        for movement in movements:
            dist_depth = movement.split(":")
            distance += int(dist_depth[0])
            depth += int(dist_depth[1])
            fuel -= abs(int(dist_depth[0]) * 3)
            if fuel <= 0 or 600 < depth or depth < 0:
                break

    return distance, depth, fuel


if __name__ == "__main__":
    run("data/submarine/route1.dat")
