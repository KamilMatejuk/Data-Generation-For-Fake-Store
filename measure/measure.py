import os
import oracledb
import numpy as np
import cProfile
import pstats
import io
import re


QUERIES = ["test"]
REPETITIONS = 10
FILENAME = "results.csv"


def measure_all(cursor, queries):
    for query in queries:
        times = []
        for _ in range(REPETITIONS):
            times.append(measure(cursor, query))
        save(times, query)


def measure(cursor, query):
    pr = cProfile.Profile()
    pr.enable()
    # cursor.execute(query)
    np.ones((100, 1000, 1000))
    pr.disable()
    s = io.StringIO()
    ps = pstats.Stats(pr, stream=s).sort_stats(pstats.SortKey.CUMULATIVE)
    ps.print_stats()
    return parse_results(s.getvalue(), 1)


def parse_results(pstats_str, n, show=False):
    found_result = False
    results = []
    for line in pstats_str.split("\n"):
        if 'cumtime' in line:
            found_result = True
            continue
        if not found_result:
            continue
        re_int = r'([0-9]+)'
        re_float = r'([0-9]+\.[0-9]+)'
        re_space = r' *'
        re_file = r'(.+)'
        regex = re_space + re_space.join([re_int] + [re_float] * 4 + [re_file])
        values = re.match(regex, line)
        if not values: continue
        ncalls = values.group(1)
        tottime = values.group(2)
        tottime_percall = values.group(3)
        cumtime = values.group(4)
        cumtime_percall = values.group(5)
        info = values.group(6)
        
        info_match = re.match(r'([^:]+):([0-9]+)\((.+)\)', info)
        if info_match:
            filename = info_match.group(1)
            lineno = info_match.group(2)
            function = info_match.group(3)
        info_match = re.match(r'\{built-in method (.+)\}', info)
        if info_match:
            filename = 'build-in'
            lineno = 0
            function = info_match.group(1)
        info_match = re.match(r'\{method \'(.+)\' of \'(.+)\' objects\}', info)
        if info_match:
            filename = info_match.group(2)
            lineno = 0
            function = info_match.group(1)

        results.append((ncalls, tottime, tottime_percall, cumtime, cumtime_percall, filename, lineno, function))
    if show:
        print('\t'.join(["ncalls", "tottime", "tottime_percall", "cumtime", "cumtime_percall", "filename", "lineno", "function"]))
        for r in results:
            print('\t'.join(map(str, r)))
    return float(results[n-1][3])


def save(times, query):
    file_exists = os.path.exists(FILENAME)
    with open(FILENAME, "a+") as f:
        if not file_exists:
            header = 'query,min_time_s,max_time_s,avg_time_s,median_time_s,std_time_s,std_to_median_percent,'
            header += ','.join(f'time_{i}' for i in range(len(times))) + '\n'
            f.write(header)
        f.write(query.replace('\n', ' ') + ',')
        f.write(f'{min(times):.5f},')
        f.write(f'{max(times):.5f},')
        f.write(f'{np.mean(times):.5f},')
        f.write(f'{np.median(times):.5f},')
        f.write(f'{np.std(times):.5f},')
        f.write(f'{(100 * np.std(times) / np.median(times)):.5f},')
        f.write(','.join(f'{t:.5f}' for t in times) + '\n')


def check_line(cursor, query):
    pr = cProfile.Profile()
    pr.enable()
    # cursor.execute(query)
    np.ones((100, 1000, 1000))
    pr.disable()
    s = io.StringIO()
    ps = pstats.Stats(pr, stream=s).sort_stats(pstats.SortKey.CUMULATIVE)
    ps.print_stats()
    return parse_results(s.getvalue(), 1, show=True)
    
        
if __name__ == '__main__':
    check_line(None, QUERIES)
    exit(0)
    with oracledb.connect(
        user="user_zsbd",
        password="password",
        host="localhost",
        port=1521,
        service_name="XEPDB1",
    ) as connection:
        with connection.cursor() as cursor:
            measure_all(cursor, QUERIES)
