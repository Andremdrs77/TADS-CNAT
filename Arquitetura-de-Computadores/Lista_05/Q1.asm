.data #0x10010000
.word 1, 0, 5, -2, -5, 7


.text
main:
    	add  $4, $0, $0 #$4 = soma = 0
    	lui  $8, 0x1001 #$8 = endereço inicial do vetor
    	addi $20, $0, 6 #$20 = quantidade de elementos
	add $22, $0, $0
	
	
laco:
	beq $20, $0, terminou
	
	lw $21, 0($8) #$21 = elemento atual
	
	#Verifica se é 0
	beq $22, $0, adiciona
	
	#Verifica se é 1
	addi $10, $0, 1
	beq $22, $10, adiciona
	
	#Verifica se é 5
	addi $10, $0, 5
	beq $22, $10, adiciona
	
	#Se não for 0, 1 nem 5
	j continua
	
	
adiciona:
	add $4, $4, $21 #soma += elemento
	
	
continua:
	addi $8, $8, 4 #próximo elemento (4 bytes)
	addi $22, $22, 1 # próximo índice
	addi $20, $20, -1 #decrementa contador
	
	j laco
	
	
terminou:	
	sw $4, 4($8) #guarda resultado
	addi $2, $0, 1
	syscall
	
	addi $2, $0, 10
	syscall