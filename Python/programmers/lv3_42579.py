from collections import defaultdict


def solution(genres, plays):
    genres_cnt = defaultdict(int)
    plays_cnt = defaultdict(list)

    for i in range(len(genres)):
        genre = genres[i]
        play = plays[i]

        genres_cnt[genre] += play
        plays_cnt[genre].append([i, play])
    genre_arr = sorted(list(genres_cnt.items()), key=lambda x: -x[1])
    answer = []

    for genre, _ in genre_arr:
        arr = plays_cnt[genre]
        if len(arr) == 1:
            answer.append(arr[0][0])
            continue
        arr.sort(key=lambda x: -x[1])
        answer.append(arr[0][0])
        answer.append(arr[1][0])

    return answer
