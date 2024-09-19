#tabela verdade
print(f'|a\t|b\t|a . b\t|') #tabula cabeçalho
for a in [True, False]: #for dentro de for
    for b in [True, False]: #estudar mais função for
        print(f'|{a}\t|{b}\t|{a and b}\t|') #faz a operação e tabula, nesse caso OR
        print(f'|{a}\t|{b}\t|{a or b}\t|')
        print(f'|{a}\t|{b}\t|{a ^ b}\t|')
