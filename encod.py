def encod(txt, file=open("untilteled.gks"), mode="a"):
    open(file, mode)
    minusc = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
              "v", "w", "x", "y", "z"]
    majusc = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
              "V", "W", "X", "Y", "Z"]
    symb_num = [" ", "!", "?", ".", ",", ":", "/", "(", ")", "'", "é", "è", "à", "@", "#", "ê", "0", "1", "2", "3", "4",
                "5", "6", "7", "8", "9", ";", "=", "*", "-", "+", "_"]

    ascii_minusc = ["97", "98", "99", "100", "101", "102", "103", "104", "105", "106", "107", "108", "109", "110",
                    "111", "112", "113", "114", "115", "116", "117", "118", "119", "120", "121", "122"]
    ascii_majusc = ["65", "66", "67", "68", "69", "70", "71", "72", "73", "74", "75", "76", "77", "78", "79", "80",
                    "81", "82", "83", "84", "85", "86", "87", "88", "89", "90"]
    ascii_symb_num = ["32", "33", "63", "46", "44", "58", "47", "40", "41", "39", "233", "232", "224", "64", "35",
                      "234", "48", "49", "50", "51", "52", "53", "54", "55", "56", "57", "59", "61", "42", "45", "43",
                      "95"]

    numb_ajout = 0
    txt_list = list(txt.strip())
    numb_caract = int(len(txt_list))
    str_conv = []

    comte = 0
    conv = True

    while conv:
        caract = txt_list[comte]

        if caract.isupper() == True:
            caract_pos = majusc.index(caract)
            # print(ascii_majusc[caract_pos])
            str_conv.append(ascii_majusc[caract_pos])
            numb_ajout += 1

        elif caract.islower() == True:
            caract_pos = minusc.index(caract)
            # print(ascii_minusc[caract_pos])
            str_conv.append(ascii_minusc[caract_pos])
            numb_ajout += 1

        else:
            caract_pos = symb_num.index(caract)
            # print(ascii_symb_num[caract_pos])
            str_conv.append(ascii_symb_num[caract_pos])
            numb_ajout += 1

        comte += 1
        if comte > numb_caract:
            conv = False

        if numb_ajout >= 8:
            for i in range(0, 8):
                file.write(str_conv[i])
                file.write(" ")
                if i == 7:
                    file.write("\n")

            numb_ajout = 0
            str_conv = []

        if comte == numb_caract:
            nomb_rest = len(str_conv)
            for i in range(0, nomb_rest):
                file.write(str_conv[i])
                file.write(" ")
                if i == 7:
                    file.write("\n")


encod("bonjour", "test.gks")