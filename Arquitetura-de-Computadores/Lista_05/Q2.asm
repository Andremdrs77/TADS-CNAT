.data #0x10010000
.text 
main:
	lui $8, 0x1001 #endereco na memoria
	addi $21, $0, 6 #contador
	#add $22, $0, $0 #indice
	
	
loopInputs:
	addi $2, $0, 5
	syscall
	
	sw $2, 0($8)
	addi $8, $8, 4
	
	addi $21, $21, -1
	addi $22, $22, 1
	
	beq $21, $0, loopLeitura
	
	j loopInputs

loopLeitura: 
	j main