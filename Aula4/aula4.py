#tabela verdade
print(f'Tabela AND:\n|a\t|b\t|a . b\t|') #tabula cabeçalho
for a in [True, False]: #for dentro de for
    for b in [True, False]: #estudar mais função for
        print(f'|{a}\t|{b}\t|{a and b}\t|') #faz a operação e tabula, nesse caso OR
print(' ')
print(f'Tabela OR:\n|a\t|b\t|a . b\t|') #tabula cabeçalho
for a in [True, False]: #for dentro de for
    for b in [True, False]: #estudar mais função for
        print(f'|{a}\t|{b}\t|{a or b}\t|')
print(' ')
print(f'Tabela XOR:\n|a\t|b\t|a . b\t|') #tabula cabeçalho
for a in [True, False]: #for dentro de for
    for b in [True, False]: #estudar mais função for
        print(f'|{a}\t|{b}\t|{a ^ b}\t|')