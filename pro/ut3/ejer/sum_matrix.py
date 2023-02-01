# ****************
# SUMANDO MATRICES
# ****************
import filecmp
from pathlib import Path


def run(matrix1_path: Path, matrix2_path: Path) -> bool:
    result_path = "data/sum_matrix/result.dat"
    with open(matrix1_path, "r") as f1, open(matrix2_path, "r") as f2, open(
        result_path, "w"
    ) as r:
        for line1, line2 in zip(f1, f2):
            result_line = ""
            for value1, value2 in zip(line1.split(), line2.split()):
                sum = int(value1) + int(value2)
                result_line += f"{sum} "
            r.write(result_line[:-1] + "\n")

    return filecmp.cmp(result_path, "data/sum_matrix/.expected", shallow=False)


if __name__ == "__main__":
    run("data/sum_matrix/matrix1.dat", "data/sum_matrix/matrix2.dat")
