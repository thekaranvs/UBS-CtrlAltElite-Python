import json

def runCode(code, cases):

    outcomes = []

    for case in cases:
        variables = case.copy()
        is_solvable = True
        flag1 = True
        whitelist = case.copy().keys()

        print(variables)

        try:
            for line in code:
                # print(line, {var: value for var, value in variables.items() if var in whitelist})
                if line.startswith('if'):
                    condition = line[3:].strip()
                    flag1 = eval(condition, variables)                        
                        
                elif line.startswith('endif'):
                    flag1 = True
                    continue
                elif flag1:
                    # print("entered")
                    if line == "fail":
                        is_solvable = False
                        break
                    exec(line, variables)

        except Exception:
            is_solvable = False

        variables = {var: int(value) for var, value in variables.items() if var in whitelist}

        outcome = {
            'is_solvable': is_solvable,
            'variables': variables
        }
        outcomes.append(outcome)

    return {"outcomes": outcomes}