def userInput():
    print("Enter the input string:")
    userInput=input().strip()
    mapping={}
    if not userInput: return mapping
    pairs=userInput.split(";")
    for pair in pairs:
        pair=pair.strip()
        if not pair: continue
        if ":" not in pair:
            print(f"Skipping invalid pair'{pair}'")
            continue
        key,value=pair.split(":",1)
        key=key.strip()
        value=[v.strip() for v in value.split(",")]
        if key: mapping[key]=value
        else: print(f"Skip empty key'{pair}'")
    return mapping

def combine(mapping, input_str):
    if not input_str:
        return mapping
    result = []
    def backtrack(index,currentpath):
        if index==len(input_str):
            result.append("".join(currentpath))
            return
        for length in [1,2]:
            if index+length<=len(input_str):
                key=input_str[index:index+length]
                if key in mapping:
                    for char in mapping[key]:
                        currentpath.append(char)
                        backtrack(index+length,currentpath)
                        currentpath.pop()
    backtrack(0,[])
    return result

dict=userInput()
input_string=input("Enter the input string:")
print(combine(dict, input_string))

