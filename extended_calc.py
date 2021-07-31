def calc(string):
    try:
        string = string.lower().replace(' ', '')
        parts = string.split('+')

        for plus in range(len(parts)):
            if '-' in parts[plus]:
                parts[plus] = parts[plus].split('-')

        print(parts)


        for plus in range(len(parts)):
            parts[plus] = precalc(parts[plus])

        print(parts) 
        result = sum(parts)
    except ValueError:
        result = 'Value warning'
    
    except ZeroDivisionError:
        result = 'Zero warning'
    return result        

def precalc(part):

    if type(part) is str:

        if '*' in part:
            result = 1
            for subpart in part.split('*'):
                result *= precalc(subpart)
            return result

        elif '/' in part:
            parts = list(map(precalc, part.split('/')))
            result = parts[0]
            for subpart in parts[1:]:
                result /= subpart
            return result
        else:
            return float(part)
    
    
    elif type(part) is list:

        for i in range(len(part)):
            part[i] = precalc(part[i])
        return part[0] - sum(part[1:])

    return part


if __name__ == '__main__':
    print(calc('2 + 1 - 3 / 10'))



