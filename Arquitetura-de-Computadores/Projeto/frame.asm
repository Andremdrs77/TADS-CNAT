.text
main:
    lui $8, 0x1001

    # Gradiente do céu: 56 linhas, 128 unidades por linha
    addi $10, $0, 56
    addi $18, $0, 0

desenharCeu:
    beq $10, $0, redefinirDesenho

    # R = 80 + linha * 3
    addi $19, $0, 80
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

linhaCeu:
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

desenharGrama:
    beq $10, $0, player

    sw $4, 0($8)
    addi $8, $8, 4
    addi $10, $10, -1
    j desenharGrama

player:
    lui $11, 0x00ff
    ori $11, $11, 0xffff

    lui $8, 0x1001
    addi $8, $8, 576
    lui $16, 0xffff

    lw $12, 0($8)
    sw $11, 0($8)

    addi $14, $0, 4

plrGo:
    add $15, $8, $14
    lw $13, 0($15)
    sw $12, 0($8)
    add $8, $15, $0
    add $12, $13, $0
    sw $11, 0($8)

    jal nulltime

    lw $17, 0($16)
    beq $17, $0, plrGo

    lw $17, 4($16)

    addi $13, $0, 32
    beq $17, $13, fim

    addi $13, $0, 'a'
    beq $13, $17, digA

    addi $13, $0, 'd'
    beq $13, $17, digD

    addi $13, $0, 's'
    beq $13, $17, digS

    addi $13, $0, 'w'
    beq $13, $17, digW

    j plrGo

digA:
    addi $14, $0, -4
    j plrGo

digD:
    addi $14, $0, 4
    j plrGo

digS:
    addi $14, $0, 128
    j plrGo

digW:
    addi $14, $0, -128
    j plrGo

fim:
    addi $2, $0, 10
    syscall

# Rotina para gastar tempo
nulltime:
    addi $25, $0, 200

ntfor:
    beq $25, $0, ntfim
    nop
    nop
    addi $25, $25, -1
    j ntfor

ntfim:
    jr $31