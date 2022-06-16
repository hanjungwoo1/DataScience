fuel = 100
power = [100, 150]
distances = [1, 1000000]


def solution(fuel, powers, distances):
    check = False
    if fuel == len(powers):
        check = True

    print(fuel)
    print(powers)
    print(distances)

    barrel = [0] * len(powers)
    times = [0] * len(powers)
    # visited = [0] * len(powers)

    # 배분 초기화
    equal_size = fuel // len(powers)

    for i, power in enumerate(powers):
        if i + 1 == len(powers):
            barrel[i] = fuel
        else:
            barrel[i] = equal_size
            fuel -= equal_size

    print("배분 초기화: ", barrel)

    result = 1e9

    while (True):
        count = 0

        times = [0] * len(powers)

        while (True):
            count += 1
            if 0 in times:
                #print(barrel)
                #print(times)
                for i, data in enumerate(barrel):
                    if times[i] != 0:
                        continue
                    else:
                        if count > data:
                            dist = ((data * data * powers[i]) / 2) + ((count - data) * data * powers[i])
                        else:
                            dist = (count * count * powers[i]) / 2

                        if dist >= distances[i]:
                            times[i] = count

            else:
                break

        if check:
            break

        print("times : ", times)

        temp_result = max(times)
        print("result : ", result, temp_result)
        print("barrel : ", barrel)
        if result == temp_result:
            #print("nothing change")
            break
        else:
            result = min(temp_result, result)

        if max(times) - min(times) > 1:
            maxi = max(times)
            index1 = times.index(maxi)

            mini = min(times)
            index2 = times.index(mini)

            barrel[index1] += 1

            if barrel[index2] == 1:
                sorted_list = sorted(times)
                next_small = sorted_list[1]
                index2 = times.index(next_small)
                barrel[index2] -= 1
            else:
                barrel[index2] -= 1
        else:
            break


    return max(times)

print(solution(fuel, power, distances))