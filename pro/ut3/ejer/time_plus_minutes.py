# *****************
# FICHO CUANDO TOCA
# *****************


def run(time: str, offset: int) -> str:
    time = time.split(":")
    total_hours = offset // 60 + int(time[0])
    hour = total_hours % 24
    total_minutes = offset % 60 + int(time[1])
    minutes = total_minutes % 60
    hour += total_minutes // 60

    final_time = f"{hour}:{minutes}"
    return final_time


if __name__ == "__main__":
    run("17:15", 240)
