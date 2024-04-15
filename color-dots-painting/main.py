import colorgram


def filtered_colors(colors):
    non_white_colors = []
    for color in colors:
        r, g, b = color.rgb.r, color.rgb.g, color.rgb.b
        if not (r == 255 and g == 255 and b == 255):
            non_white_colors.append(color)
    return non_white_colors


def main():
    colors = colorgram.extract('colorgram')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
