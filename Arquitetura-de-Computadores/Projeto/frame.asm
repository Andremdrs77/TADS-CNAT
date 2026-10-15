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

    # Posicionar o jogador na penultima linha, coluna inicial 64
    lui $8, 0x1001
    addi $8, $8, 31744
    addi $8, $8, 256

    # Endereco do Keyboard and Display MMIO
    lui $16, 0xffff

    lw $12, 0($8)
    sw $22, 0($8)
plrGo:
    # Esperar uma tecla
    lw $17, 0($16)
    beq $17, $0, plrGo

    lw $17, 4($16)

    # Espaco encerra
    addi $13, $0, 32
    beq $17, $13, fim

    # Tecla A: mover para a esquerda
    addi $13, $0, 'a'
    beq $17, $13, digA

    # Tecla D: mover para a direita
    addi $13, $0, 'd'
    beq $17, $13, digD

    j plrGo

digA:
    # Primeira coluna: nao mover mais para a esquerda
    lui $13, 0x1001
    addi $13, $13, 31744
    beq $8, $13, plrGo

    addi $14, $0, -4
    j moverPlayer
digD:
    # Ultima coluna: nao mover mais para a direita
    lui $13, 0x1001
    addi $13, $13, 32252
    beq $8, $13, plrGo

    addi $14, $0, 4
    j moverPlayer

moverPlayer:
    add $15, $8, $14
    lw $13, 0($15)
    sw $12, 0($8)
    add $8, $15, $0
    add $12, $13, $0
    sw $22, 0($8)

    j plrGo

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
