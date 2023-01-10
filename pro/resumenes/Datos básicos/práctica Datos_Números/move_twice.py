# *******************
# TIRO PORQUE ME TOCA
# *******************


def run(current_pos: int, dice: int) -> int:
    final_pos = current_pos + dice * 2
    return final_pos


if __name__ == "__main__":
    run(3, 6)
