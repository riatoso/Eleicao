def valida_cpf(cpf):
    for i in cpf:
        try:
            i = int(i)
            continue
        except:
            return 0
