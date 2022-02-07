
def GemartraPrimus(ciphertext,type): # takes two parameters, ciphertext to be solved, type e.g decimal|english output
    '''first the page must be convered to its decimal counterpart'''
    output=""
    pageDecDict={"ᚫ":101,"ᛄ":37,"ᛟ":83,"ᛋ":53,"ᚱ":11,"ᛗ":71,"ᚣ":103,
                 "ᛚ":73,"ᚩ":7,"ᚻ":23,"ᚳ":13,"ᚦ":5,"ᚷ":17,"ᚹ":19,"ᛉ":47,
                 "ᚪ":97,"ᛈ":43,"ᛞ":89,"ᚢ":3,"ᚾ":29,"ᚠ":2,"ᛡ":107,"ᛏ":59,
                 "ᛇ":41,"ᛖ":67,"ᛝ":79,"ᛁ":31,"ᛠ":109,"ᛒ":61}

    pageDecDictLet = {"ᚫ": "AE", "ᛄ": "J", "ᛟ": "OE", "ᛋ": "S", "ᚱ": "R", "ᛗ": "M", "ᚣ": "Y",
                   "ᛚ": "L", "ᚩ": "O", "ᚻ": "H", "ᚳ": "C", "ᚦ": "TH", "ᚷ": "G", "ᚹ": "W", "ᛉ": "X",
                   "ᚪ": "A", "ᛈ": "P", "ᛞ": "D", "ᚢ": "U", "ᚾ": "N", "ᚠ": "F", "ᛡ": "IA", "ᛏ": "T",
                   "ᛇ": "EO", "ᛖ": "E", "ᛝ": "NG", "ᛁ": "I", "ᛠ": "EA", "ᛒ": "B"}

    if type=="dec":
        for let in ciphertext:
            if let in pageDecDict:
                output+=str(pageDecDict[let])+" "
    elif type=="letter":
        for let in ciphertext:
            if let in pageDecDictLet:
                output+=str(pageDecDictLet[let])
    output=[x for x in output]
    return output

if __name__=="__main__":
    output_Solver =GemartraPrimus("","letter") #enter the respective runes here from the ttf file
    print(output_Solver)
