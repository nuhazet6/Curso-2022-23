import sys

import pycheck

CHECK_CASES = [
    [["🟢"], "🟠"],
    [["🟠"], "🔴"],
    [["🔴"], "🟢"],
]


def run(color: str) -> str:

    match color:
        case "🟢":
            new_color = "🟠"
        case "🟠":
            new_color = "🔴"
        case "🔴":
            new_color = "🟢"

    return new_color


if __name__ == "__main__":
    pycheck.check(run, CHECK_CASES, sys.argv)
