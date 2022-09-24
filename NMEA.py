indexLen = [6, 2, 30, 4, 8, 10, 1, 28, 27, 12, 9, 6, 4, 1, 1, 19]  #

conversion_table = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                    ':', ';', '<', '=', '>', '?', '@',
                    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                    'U' 'V', 'W',
                    "'",
                    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                    'u', 'v', 'w']  # 필요없는듯


def six_bit_binary(n):
    #
    n += 40
    if n > 128:
        return bin(n + 32)[-6:]
    else:
        return bin(n + 40)[-6:]


def separate(input):
    tmp = input.split('*')
    tmp = tmp[0].split(',')
    return tmp[5]


def conversion_six_bit(input):
    result = ''
    for i in input:
        # tmp = conversion_table.index(i)
        tmp = str(six_bit_binary(ord(i)))
        result += tmp
    return result


def slicing(bin_list):
    '''캡슐화된 문자열 디코딩 및 해석을 위한 워크시ㄷ트'''
    result = []
    index = 0
    for i in range(len(indexLen)):
        result.append(bin_list[index:index + indexLen[i]])
        index += indexLen[i]
    return result


def Trans_digit(sliced):
    result = [0] * 16
    for i in [0, 1, 2, 3, 6, 10, 11, 12, 13, 14]:
        result[i] = int('0b' + sliced[i], 2)
    result[4] = [int(sliced[4][0]), (int('0b' + sliced[4][1:], 2) * 4.733) ** 2]  # [부호(0:양수, 1:음수), 값]
    result[5] = int('0b' + sliced[5], 2) / 10
    result[7] = [int(sliced[7][0]), int('0b' + sliced[7][1:], 2) / 10000 // 60,
                 int('0b' + sliced[7][1:], 2) / 10000 % 60]
    result[8] = [int(sliced[8][0]), int('0b' + sliced[8][1:], 2) / 10000 // 60,
                 int('0b' + sliced[8][1:], 2) / 10000 % 60]
    # [부호, degrees, minutes]
    result[9] = int('0b' + sliced[9], 2) / 10
    result[15] = [int('0b' + sliced[15][:2], 2), int('0b' + sliced[15][2:5], 2), int('0b' + sliced[15][5:10], 2),
                  int('0b' + sliced[15][10:17], 2)]  # result[17]:result[18] UTC
    return result


def show_info(input):
    print("Message ID:", input[0])
    print("Message repeated:", input[1])
    print("User ID:", input[2])
    print("Navigational status:", input[3])
    print("ROT", end='')
    if input[4][0] == 0:
        print("-turning right:", input[4][1])
    else:
        print("-turning left:", input[4][1])
    print("SOG:", input[5])
    print("Position accuracy:", input[6])
    print("Longitude(degree.minute):", end=' ')
    print("%d.%d" % (input[7][1], input[7][2]), end=' ')
    if input[7][0] == 0:
        print("E")
    else:
        print("W")
    print("Latitude(degree.minute):", end=' ')
    print("%d.%d" % (input[8][1], input[8][2]), end=' ')
    if input[8][0] == 0:
        print("N")
    else:
        print("S")
    print("COG:", input[9])
    print("True Heading:", input[10])
    print("Time Stamp:", input[11])
    print("Reserved for regional applications:", input[12])
    print("Spare:", input[13])
    print("RAIM-Flag:", input[14], end=', ')
    if input[14] == 0:
        print("RAIM not in use")
    else:
        print("RAIM in use")
    print("Communication State: UTC Direct -", input[15][0], ", remain frame -", input[15][1], ", UTC -", input[15][2],
          ":", input[15][3])


def NMEA(input):
    tmp = separate(input)
    bin_list = conversion_six_bit(tmp)
    sliced = slicing(bin_list)
    trans_digit = Trans_digit(sliced)
    show_info(trans_digit)


input = '!AIVDM,1,1,,1,1P000Oh1IT1svTP2r:43grwb05q4,0*01<CR><LF>'
NMEA(input)
