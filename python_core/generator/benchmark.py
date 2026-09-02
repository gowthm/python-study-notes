"""
Compare a generator-based streaming reader against loading everything
into a list, using tracemalloc for peak-memory and time.perf_counter
for wall-clock time.

Self-contained: generates its own 1M-line CSV on first run if one
isn't found, so you can just `python3 benchmark.py`.
"""
import os
import random
import string
import time
import tracemalloc
from dataclasses import dataclass

N_LINES = 1_000_000
PATH = "records.csv"


def ensure_data_file(path=PATH, n=N_LINES):
    if os.path.exists(path):
        return
    random.seed(42)
    with open(path, "w") as f:
        for i in range(n):
            name = "".join(random.choices(string.ascii_lowercase, k=8))
            value = round(random.uniform(0, 1000), 3)
            ts = 1_700_000_000 + i
            f.write(f"{i},{name},{value},{ts}\n")


@dataclass
class Record:
    __slots__ = ("id", "name", "value", "ts")
    id: int
    name: str
    value: float
    ts: int


def parse_line(line: str) -> Record:
    id_, name, value, ts = line.rstrip("\n").split(",")
    return Record(int(id_), name, float(value), int(ts))


# ---------- Generator version: one line, one record, at a time ----------
def read_records_gen(path):
    """Lazily yields one Record per call. Never holds more than one
    line + one Record in memory at a time, regardless of file size."""
    with open(path, "r") as f:
        for line in f:
            yield parse_line(line)


# ---------- List version: materializes every record up front ----------
def read_records_list(path):
    """Eagerly builds the full list of Records before returning."""
    with open(path, "r") as f:
        return [parse_line(line) for line in f]


def measure(fn, *args):
    tracemalloc.start()
    t0 = time.perf_counter()

    total_value = 0.0
    count = 0
    for record in fn(*args):
        total_value += record.value
        count += 1

    elapsed = time.perf_counter() - t0
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    return {
        "count": count,
        "avg_value": total_value / count,
        "elapsed_s": elapsed,
        "current_mb": current / 1024 / 1024,
        "peak_mb": peak / 1024 / 1024,
    }


if __name__ == "__main__":
    ensure_data_file()

    gen_stats = measure(read_records_gen, PATH)
    list_stats = measure(read_records_list, PATH)

    print(f"{'metric':<12}{'generator':>14}{'list':>14}")
    print(f"{'records':<12}{gen_stats['count']:>14,}{list_stats['count']:>14,}")
    print(f"{'time (s)':<12}{gen_stats['elapsed_s']:>14.3f}{list_stats['elapsed_s']:>14.3f}")
    print(f"{'peak MB':<12}{gen_stats['peak_mb']:>14.2f}{list_stats['peak_mb']:>14.2f}")
    print(f"{'current MB':<12}{gen_stats['current_mb']:>14.2f}{list_stats['current_mb']:>14.2f}")

    print(f"\nsame avg_value? {abs(gen_stats['avg_value'] - list_stats['avg_value']) < 1e-9}")