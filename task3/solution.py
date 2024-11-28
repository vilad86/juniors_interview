








def get_intervals(times: list[int]) -> list[tuple[int, int]]:
    """Список с временем переводим в список интервалов."""
    return sorted([(start, end) for start, end in zip(times[0::2], times[1::2])])

def merge_intervals(intervals: list[tuple[int, int]]) -> list[tuple[int, int]]:
    """Слияние интервалов. Если они могут себе это позволить..."""
    if (not intervals): return []
    
    merged = [intervals[0]]
    for current in intervals[1:]:
        c_start, c_end = current[0], current[1]
        l_start, l_end = last = (merged[-1][0], merged[-1][1])

        
        if (l_end >= c_start): #: Если труться друг об друга, мы их склеим ПВА.
            merged[-1] = (l_start, max(c_end, l_end))
        else:
            merged.append(current)
    return merged

def find_intersections(intervals_1: list[tuple[int, int]], intervals_2: list[tuple[int, int]]) -> list[tuple[int, int]]:
    """Поиск пересечений."""
    intersections = []
    for start_1, end_1 in intervals_1:
        for start_2, end_2 in intervals_2:
            #: Ищем, какая из двух точек старта интервалов, находится дальше, чтобы от неё отталкиваться.
            max_start = max(start_1, start_2)
            
            #: Ищем, какая из двух точек конца интервалов, находится ближе, чтобы на неё ориентироваться.
            min_end = min(end_1, end_2)

            #: Это на случай, если интервали не соприкасаются. Важная штука.
            if (max_start >= min_end): continue

            intersections.append((max_start, min_end))
    return intersections

def appearance(intervals: dict[str, list[int]]) -> int:
    
    lesson = intervals['lesson']
    pupil  = intervals['pupil']
    tutor  = intervals['tutor']

    lesson_intervals = merge_intervals(get_intervals(lesson))
    pupil_intervals  = merge_intervals(get_intervals(pupil))
    tutor_intervals  = merge_intervals(get_intervals(tutor))

    pupil_tutor = find_intersections(pupil_intervals, tutor_intervals)
    lesson_pt   = find_intersections(pupil_tutor, lesson_intervals)

    return sum([(end - start) for start, end in lesson_pt])


#: -------------------------------------------------------------------------------------------------------------------------------------
tests = [
    {'intervals': {'lesson': [1594663200, 1594666800],
                   'pupil':  [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
                   'tutor':  [1594663290, 1594663430, 1594663443, 1594666473]},
     'answer': 3117
    },
    {'intervals': {'lesson': [1594702800, 1594706400],
                   'pupil':  [1594702789, 1594704500, 1594702807, 1594704542, 1594704512, 1594704513, 1594704564, 1594705150, 1594704581, 1594704582, 1594704734, 1594705009, 1594705095, 1594705096, 1594705106, 1594706480, 1594705158, 1594705773, 1594705849, 1594706480, 1594706500, 1594706875, 1594706502, 1594706503, 1594706524, 1594706524, 1594706579, 1594706641],
                   'tutor':  [1594700035, 1594700364, 1594702749, 1594705148, 1594705149, 1594706463]},
    'answer': 3577
    },
    {'intervals': {'lesson': [1594692000, 1594695600],
                   'pupil':  [1594692033, 1594696347],
                   'tutor':  [1594692017, 1594692066, 1594692068, 1594696341]},
    'answer': 3565
    },
]

if __name__ == '__main__':
    for i, test in enumerate(tests):
       test_answer = appearance(test['intervals'])
       assert test_answer == test['answer'], f'Error on test case {i}, got {test_answer}, expected {test["answer"]}'

    print('ПОЗДРАВЛЯЕМ! Вы сквозь пот и слезы, а еще остывшие пелемени, справились с этой... штукой!\nПриятного вам аппетита!')