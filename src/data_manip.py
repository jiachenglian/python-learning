dataset = [[0, '5ccsdsd'], [1, 'eljd'], [2, 'd2'], [3, 'a323'], [4, 'eljd'], [5, 'bss'], [6, '5ccsdsd'], [7, 'eljd'], [8, '5ccsdsd'], [9, 'a323'], [10, 'eljd'], [11, 'a323'], [12, '5ccsdsd'], [13, 'a323'], [14, 'a323'], [15, 'a323'], [16, 'eljd'], [17, 'eljd'], [18, '5ccsdsd'], [19, 'bss'], [20, 'bss'], [21, 'd2'], [22, '5ccsdsd'], [23, 'a323'], [24, 'bss'], [25, 'a323'], [26, 'bss'], [27, 'eljd'], [28, '5ccsdsd'], [29, 'bss'], [30, 'd2'], [31, 'd2'], [32, 'bss'], [33, 'bss'], [34, '5ccsdsd'], [35, '5ccsdsd'], [36, '5ccsdsd'], [37, 'bss'], [38, 'eljd'], [39, 'd2'], [40, 'bss'], [41, 'd2'], [42, 'bss'], [43, 'a323'], [44, 'bss'], [45, 'eljd'], [46, 'd2'], [47, 'd2'], [48, 'bss'], [49, 'bss'], [50, 'eljd'], [51, 'bss'], [52, 'bss'], [53, 'a323'], [54, 'd2'], [55, 'eljd'], [56, 'eljd'], [57, 'bss'], [58, '5ccsdsd'], [59, '5ccsdsd'], [60, 'bss'], [61, 'a323'], [62, 'eljd'], [63, '5ccsdsd'], [64, 'd2'], [65, 'eljd'], [66, 'd2'], [67, '5ccsdsd'], [68, 'bss'], [69, 'bss'], [70, '5ccsdsd'], [71, 'd2'], [72, 'a323'], [73, 'a323'], [74, 'bss'], [75, 'd2'], [76, 'bss'], [77, 'eljd'], [78, 'd2'], [79, '5ccsdsd'], [80, 'a323'], [81, '5ccsdsd'], [82, 'd2'], [83, 'eljd'], [84, 'bss'], [85, '5ccsdsd'], [86, 'a323'], [87, 'bss'], [88, 'd2'], [89, 'bss'], [90, 'd2'], [91, 'eljd'], [92, '5ccsdsd'], [93, 'a323'], [94, 'd2'], [95, 'a323'], [96, '5ccsdsd'], [97, 'eljd'], [98, '5ccsdsd'], [99, 'a323']]

dict = {}

for data in dataset:
    if data[1] in dict.keys():
        dict[data[1]] += 1
    else:
        dict[data[1]] = 1
print(dict.items())
