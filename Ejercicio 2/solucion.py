def calculate_champions(number_of_races, race_results, scoring_systems):
    champions = []
    for scoring in scoring_systems:
        points = [0] * (len(race_results[0]))
        for race in race_results:
            for position, pilot in enumerate(race):
                if position < len(scoring):
                    points[pilot - 1] += scoring[position]

        max_points = max(points)
        winners = [pilot_id + 1 for pilot_id, pilot_points in enumerate(points) if pilot_points == max_points]
        champions.append(winners)

    return champions


def main():
    while True:
        G, P = map(int, input().split())
        if G == P == 0:
            break
        race_results = [list(map(int, input().split())) for _ in range(G)]
        S = int(input())
        scoring_systems = [list(map(int, input().split()))[1:] for _ in range(S)]
        for winners in calculate_champions(G, race_results, scoring_systems):
            print(' '.join(map(str, winners)))


if __name__ == '__main__':
    main()