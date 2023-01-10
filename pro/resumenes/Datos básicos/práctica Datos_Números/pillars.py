# **********************
# POSTES EN LA CARRETERA
# **********************


def run(num_pillars: int, gap_pillars: float, pillar_width: float) -> float:
    total_gap_pillar_cm = gap_pillars * 100 * (num_pillars - 1)
    total_pillar_width = pillar_width * (num_pillars - 2)
    inter_distance = total_gap_pillar_cm + total_pillar_width
    return inter_distance


if __name__ == "__main__":
    run(10, 5, 30)
