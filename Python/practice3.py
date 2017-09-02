# filter by type 
def FilterByType():
    print "enter any data"
    response = input()
    if isinstance(response, int) and response > 50:
        return  "that's a big number"
    elif  isinstance(response, int) and response < 50:
        return "that's a small number"
    elif isinstance(response, str) and len(response)<50:
        return "short sentence"
    elif isinstance(response, str) and response > 50:
        return "long sentence"
    elif isinstance(response, list) and len(response) <10:
        return "short list"
    elif isinstance(response, list) and len(response) > 10:
        return "long list"
print FilterByType()
