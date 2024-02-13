def solution(genres, plays):
    genre = {}
    cnt = {}

    for i in range(len(genres)):
        if genres[i] in genre.keys():
            genre[genres[i]] += plays[i]
            cnt[genres[i]].append((plays[i], i))
        else:
            genre[genres[i]] = plays[i]
            cnt[genres[i]] = [(plays[i], i)]

    genre = sorted(genre.items(), key=lambda x: x[1], reverse=True)

    answer = []
    for j, _ in genre:
        for _, k in sorted(cnt[j], key=lambda x: (x[0],-x[1]), reverse=True)[:2]:
            answer.append(k)

    return answer
