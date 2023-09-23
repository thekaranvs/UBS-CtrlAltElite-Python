def runCode(code, cases):

    outcomes = []

    for case in cases:
        variables = case.copy()
        is_solvable = True
        flag1 = True
        endIfList = []
        whitelist = case.copy().keys()

        # print(variables)

        try:
            for line in code:
                # print(line, {var: value for var, value in variables.items() if var in whitelist})
                if  line.startswith('if'):
                    if flag1:
                        condition = line[3:].strip()
                        flag1 = eval(condition, variables)
                    else:
                        endIfList.append(0)                
                        
                elif line.startswith('endif'):
                    if len(endIfList) != 0:
                        endIfList.pop()
                    else:
                        flag1 = True
                    continue
                elif flag1:
                    # print("entered")
                    if line == "fail":
                        is_solvable = False
                        break
                    exec(line, variables)

        except Exception:
            print("testing if entered")
            is_solvable = False

        variables = {var: int(value) for var, value in variables.items() if var in whitelist}

        outcome = {
            'is_solvable': is_solvable,
            'variables': variables
        }
        outcomes.append(outcome)

    return {"outcomes": outcomes}