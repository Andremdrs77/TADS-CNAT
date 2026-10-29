.text
main:
    lui $8, 0x1001

    # Gradiente do ceu: 56 linhas, 128 unidades por linha
    addi $10, $0, 56
    addi $18, $0, 0

desenharCeu: # Registradores usados: $9, $10, $18, $19, $20, $21
    beq $10, $0, redefinirDesenho

    # R = 80 + linha * 3
    addi $20, $0, 3
    mult $18, $20
    mflo $19
    addi $19, $19, 80

    # G = 185 + linha
    addi $20, $18, 185

    # B = 235 + linha / 3
    addi $21, $18, 0
    srl $21, $21, 2
    addi $21, $21, 235

    # Montar cor RGB: 0x00RRGGBB
    sll $19, $19, 16
    sll $20, $20, 8
    or $4, $19, $20
    or $4, $4, $21

    addi $9, $0, 128

linhaCeu: # Registradores usados: $9, $10, $18
    sw $4, 0($8)
    addi $8, $8, 4
    addi $9, $9, -1
    bne $9, $0, linhaCeu

    addi $18, $18, 1
    addi $10, $10, -1
    j desenharCeu

redefinirDesenho:
    addi $10, $0, 1024

    # Verde da grama: 0x004CAF50
    lui $4, 0x004c
    ori $4, $4, 0xaf50

desenharGrama: # Registradores usados: $10
    beq $10, $0, redefinirPlataforma
    
    sw $4, 0($8)
    addi $8, $8, 4
    addi $10, $10, -1
    j desenharGrama

redefinirPlataforma:
    lui $8, 0x1001
    addi $8, $8, 5632

    lui $4, 0x008b
    ori $4, $4, 0x5a2b

    addi $10, $0, 512

desenharPlataforma:
    beq $10, $0, desenharGalinhas
    
    sw $4, 0($8)
    
    addi $8, $8, 4
    addi $10, $10, -1
    j desenharPlataforma

desenharGalinhas:
    # Cores
    lui $22, 0x00ff
    ori $22, $22, 0xffff       # Branco

    lui $23, 0x00ff
    ori $23, $23, 0x0000       # Vermelho

    lui $24, 0x00ff
    ori $24, $24, 0xff00       # Amarelo

    lui $25, 0x008b
    ori $25, $25, 0x5a2b       # Marrom

    addi $26, $0, 0            # Preto

    lui $28, 0x00d9
    ori $28, $28, 0xa441       # Dourado do ninho

    # Galinha 1
    lui $27, 0x1001
    addi $27, $27, 2608
    jal desenharGalinha

    # Galinha 2
    lui $27, 0x1001
    addi $27, $27, 2704
    jal desenharGalinha

    # Galinha 3
    lui $27, 0x1001
    addi $27, $27, 2800
    jal desenharGalinha

    # Galinha 4
    lui $27, 0x1001
    addi $27, $27, 2896
    jal desenharGalinha

    # Galinha 5
    lui $27, 0x1001
    addi $27, $27, 2992
    jal desenharGalinha

    j player


# Galinha compacta com ninho
# $27 = endereco inicial do sprite

desenharGalinha:
    # Linha 0: crista vermelha
    sw $23, 28($27)
    sw $23, 32($27)

    # Linha 1: topo
    sw $23, 536($27)
    sw $22, 540($27)
    sw $22, 544($27)
    
    sw $22, 1032($27)
    sw $22, 1036($27)
    sw $22, 1040($27)
    sw $22, 1044($27)
    sw $22, 1048($27)

    # Linha 2: corpo e olho
    sw $22, 1020($27)
    sw $22, 1024($27)
    sw $22, 1028($27)
    sw $22, 1032($27)
    sw $22, 1036($27)
    sw $22, 1040($27)
    sw $22, 1044($27)
    sw $22, 1048($27)
    sw $22, 1044($27)
    sw $22, 1052($27)
    sw $26, 1056($27)

    # Linha 3: mais corpo e bico
    sw $22, 1532($27)
    sw $22, 1536($27)
    sw $22, 1540($27)
    sw $22, 1544($27)
    sw $22, 1548($27)
    sw $22, 1552($27)
    sw $22, 1556($27)
    sw $22, 1560($27)
    sw $22, 1564($27)
    sw $24, 1568($27)
    sw $24, 1572($27)

    # Linha 4: parte inferior do corpo
    sw $22, 2048($27)
    sw $22, 2052($27)
    sw $22, 2056($27)
    sw $22, 2060($27)
    sw $22, 2064($27)
    sw $22, 2068($27)
    sw $22, 2072($27)
    sw $22, 2076($27)
    sw $22, 2080($27)

    # Linha 5: ninho dourado
    sw $28, 2552($27)
    sw $28, 2556($27)
    sw $28, 2560($27)
    sw $28, 2564($27)
    sw $28, 2568($27)
    sw $28, 2572($27)
    sw $28, 2576($27)
    sw $28, 2580($27)
    sw $28, 2584($27)
    sw $28, 2588($27)
    sw $28, 2592($27)
    sw $28, 2596($27)

    jr $31
    
    
player:
    # Endereco inicial da cesta
    lui $8, 0x1001
    addi $8, $8, 30932

    # Endereco do teclado MMIO
    lui $16, 0xffff

    # Reservar memoria para salvar o cenario sob a cesta
    addi $4, $0, 640
    addi $2, $0, 9
    syscall
    add $30, $2, $0

    # Salvar o fundo original e desenhar a cesta
    jal salvarCenario
    jal desenharCesto

        # Inicializar o sistema de ovos
    addi $3, $0, 0        # Indice da proxima galinha
    addi $11, $0, 20000   # Intervalo entre movimentos do ovo

    jal iniciarOvo
    
plrGo:
 # Controlar a velocidade da queda
    addi $11, $11, -1
    bne $11, $0, verificarTeclado

    addi $11, $0, 20000
    jal atualizarOvo

verificarTeclado:
    # Verificar se existe uma tecla disponivel
    lw $17, 0($16)
    andi $17, $17, 1
    beq $17, $0, continuarCiclo

    # Verificar se existe uma tecla disponivel
    lw $17, 0($16)
    andi $17, $17, 1
    beq $17, $0, continuarCiclo

    # Ler o codigo da tecla
    lw $17, 4($16)

    # Espaco encerra
    addi $13, $0, 32
    beq $17, $13, fim

    # Tecla A
    addi $13, $0, 'a'
    beq $17, $13, digA

    # Tecla D
    addi $13, $0, 'd'
    beq $17, $13, digD

    j continuarCiclo

digA:
    # Limite esquerdo
    lui $13, 0x1001
    addi $13, $13, 30732
    slt $15, $8, $13
    bne $15, $0, continuarCiclo

    addi $14, $0, -8
    j moverCesto

digD:
    # Limite direito
    lui $13, 0x1001
    addi $13, $13, 31156
    slt $15, $13, $8
    bne $15, $0, continuarCiclo

    addi $14, $0, 8
    j moverCesto
    
moverCesto:
    # Restaurar o cenario na posicao antiga
    jal restaurarCenario

    # Atualizar a posicao da cesta
    add $8, $8, $14

    # Salvar o cenario na nova posicao
    jal salvarCenario

    # Desenhar a cesta na nova posicao
    jal desenharCesto

    j plrGo


continuarCiclo:
    j plrGo

# Criar um ovo abaixo da proxima galinha
# $3  = indice da proxima galinha (0 a 4)
# $29 = endereco atual do ovo
# $12 = endereco onde o ovo desaparece
# $7  = cor original do fundo

iniciarOvo:
escolherGalinha:
    # Gerar um numero aleatorio entre 0 e 4
    addi $4, $0, 0
    addi $5, $0, 5
    addi $2, $0, 42
    syscall

    # Evitar repetir a galinha do ovo anterior
    beq $4, $3, escolherGalinha

    # Guardar o indice da galinha escolhida
    add $3, $4, $0

    # Endereco inicial: galinha 1 + linha abaixo do ninho
    lui $29, 0x1001
    addi $29, $29, 5680

    # Cada galinha esta 96 bytes depois da anterior
    addi $13, $0, 96
    mult $3, $13
    mflo $13
    add $29, $29, $13

    # O ovo desaparece ao chegar a linha 55
    addi $12, $29, 22528

    # Guardar o fundo e desenhar o ovo branco
    lw $7, 0($29)
    sw $22, 0($29)

iniciarOvoFim:
    jr $31

# Avancar o ovo uma linha

atualizarOvo:
    # Preservar o endereco de retorno
    add $6, $31, $0

    # Restaurar o fundo na posicao anterior
    sw $7, 0($29)

    # Descer uma linha: 512 bytes
    addi $29, $29, 512

    # Verificar se chegou ao topo da cesta
    beq $29, $12, ovoChegou

    # Guardar o fundo da nova posicao
    lw $7, 0($29)

    # Desenhar o ovo
    sw $22, 0($29)

    jr $6

ovoChegou:
    # O proximo ovo surge imediatamente
    jal iniciarOvo

    jr $6
    
# Salvar o cenario sob a cesta
# $8  = endereco de referencia da cesta
# $30 = endereco da memoria reservada
# Regiao: 8 linhas x 18 unidades

# Salvar o cenario sob a cesta
salvarCenario:
    add $6, $31, $0
    addi $13, $8, -2568
    add $15, $30, $0
    addi $10, $0, 8

salvarLinha:
    addi $9, $0, 20

salvarUnidade:
    lw $5, 0($13)
    sw $5, 0($15)

    addi $13, $13, 4
    addi $15, $15, 4
    addi $9, $9, -1
    bne $9, $0, salvarUnidade

    addi $13, $13, 432
    addi $10, $10, -1
    bne $10, $0, salvarLinha

    jr $6


# Restaurar o cenario sob a cesta
restaurarCenario:
    add $6, $31, $0
    addi $13, $8, -2568
    add $15, $30, $0
    addi $10, $0, 8

restaurarLinha:
    addi $9, $0, 20

restaurarUnidade:
    lw $5, 0($15)
    sw $5, 0($13)

    addi $13, $13, 4
    addi $15, $15, 4
    addi $9, $9, -1
    bne $9, $0, restaurarUnidade

    addi $13, $13, 432
    addi $10, $10, -1
    bne $10, $0, restaurarLinha

    jr $6
    
# Cesto marrom: 7 unidades de largura x 3 de altura.
# $8 = endereco do canto superior esquerdo.
# $25 = cor marrom.
# Formato: laterais e fundo, com interior vazio.

desenharCesto:

    # Mais 4 linhas acima: duas colunas por linha
    sw $25, -1032($8)
    sw $25, -1028($8)
    sw $25, -1544($8)
    sw $25, -1544($8)
    sw $25, -1540($8)
    sw $25, -2056($8)
    sw $25, -2052($8)
    sw $25, -2568($8)
    sw $25, -2564($8)
    
    # Linha superior: laterais
    sw $25, -1032($8)
    sw $25, -1028($8)
    sw $25, -960($8)
    sw $25, -956($8)

    sw $25, -1544($8)
    sw $25, -1540($8)
    sw $25, -1472($8)
    sw $25, -1468($8)

    sw $25, -2056($8)
    sw $25, -2052($8)
    sw $25, -1984($8)
    sw $25, -1980($8)

    sw $25, -2568($8)
    sw $25, -2564($8)
    sw $25, -2496($8)
    sw $25, -2492($8)
    sw $25, -520($8)
    sw $25, -516($8)
    sw $25, -448($8)
    sw $25, -444($8)
    
    sw $25, -8($8)
    sw $25, -4($8)
    sw $25, 0($8)
    sw $25, 60($8)
    sw $25, 64($8)
    sw $25, 68($8)

    # Linha do meio: laterais
	sw $25, 508($8)
	sw $25, 512($8)
	sw $25, 516($8)
	sw $25, 520($8)
	sw $25, 524($8)
	sw $25, 528($8)
	sw $25, 532($8)
	sw $25, 536($8)
	sw $25, 540($8)
	sw $25, 544($8)
	sw $25, 548($8)
	sw $25, 552($8)
	sw $25, 556($8)
	sw $25, 560($8)
	sw $25, 564($8)
	sw $25, 568($8)
	sw $25, 572($8)
	sw $25, 576($8)
	
    # Linha inferior: fundo completo
    addi $9, $0, 16
    addi $13, $8, 1024

desenharFundoCesto:
    sw $25, 0($13)
    addi $13, $13, 4
    addi $9, $9, -1
    bne $9, $0, desenharFundoCesto

    jr $31


fim:
    addi $2, $0, 10
    syscall


nulltime: # Rotina para gastar tempo: $25
    addi $25, $0, 0

ntfor:
    beq $25, $0, ntfim
    nop
    nop
    addi $25, $25, -1
    j ntfor

ntfim:
    jr $31
