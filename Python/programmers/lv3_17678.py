def make_time(j, t):
    h_int = 9 + j * t // 60 
    m_int = 0 + j * t % 60
    if h_int < 10:
        h = '09'
    else:
        h = str(h_int)
    if m_int < 10:
        m = '0' + str(m_int)
    else:
        m = str(m_int)
    return h, m

def solution(n, t, m, timetable):
    answer = ''
    timetable_ = sorted(timetable)
    cnt = [[] for i in range(n)] # [0] -> <= 9:00 ~ 9:00 + t < [n] <= 9:00 + t * n
    j = 0
    hour, minute = make_time(j, t)
    timeset = []
    timeset.append('09:00')
    for crew in timetable_:
        while j < n and (crew > timeset[j] or len(cnt[j]) >= m):
            j += 1
            hour, minute = make_time(j, t)
            timeset.append(f"{hour}:{minute}")
        if j < n:
            cnt[j].append(crew)
    print(cnt)
    while len(timeset) != n:
        timeset.pop()
    if len(cnt[-1]) == m:
        print(cnt[-1][-1])
        h_int = int(cnt[-1][-1][:2])
        m_int = int(cnt[-1][-1][3:5])
        print(h_int, m_int)
        if m_int == 0:
            m_int = 59
            h_int -= 1
        else:
            m_int -= 1
        if h_int < 10:
            h_str = '0' + str(h_int)
        else:
            h_str = str(h_int)
        if m_int< 10:
            m_str = '0' + str(m_int)
        else:
            m_str = str(m_int)
        return f"{h_str}:{m_str}"
    else:
        return timeset[-1]

    return answer