
def SpeechCalcTotal(string_split):
    numbers = [str(t) for t in range(11)]
    number_strings = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]
    
    numd = {k: int(k) for k in numbers}
    number_strd = {number_strings[i]: i for i in range(len(number_strings))}
    numd.update(number_strd)
    calc = [numd[k] for k in string_split if k in numd.keys()]
    return calc
