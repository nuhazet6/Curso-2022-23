# ****************
# YELLOW SUBMARINE
# ****************
from pathlib import Path


def run(route_path: Path) -> tuple:

    with open(route_path, "r") as f:
        fuel = int(f.readline().strip())
        moves_str = f.readline().split(",")
        distance = 0
        depth = 0
        for movement in moves_str:
            dist_depth = [int(num) for num in movement.split(":")]
            actual_dist = dist_depth[0]
            distance += actual_dist
            depth += int(dist_depth[1])
            fuel -= abs(actual_dist * 3)
            if fuel <= 0 or 600 < depth or depth < 0:
                break

    return distance, depth, fuel


if __name__ == "__main__":
    run("data/submarine/route1.dat")
