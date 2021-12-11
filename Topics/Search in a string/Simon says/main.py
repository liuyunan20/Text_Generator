def what_to_do(instructions):
    if instructions.startswith("Simon says"):
        dosth = instructions.replace("Simon says ", '')
        return f'I {dosth}'
    elif instructions.endswith("Simon says"):
        dosth = instructions.replace(" Simon says", '')
        return f'I {dosth}'
    else:
        return "I won't do it!"
