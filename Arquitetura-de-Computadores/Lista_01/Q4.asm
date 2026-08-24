.text
main:
	addi $5, $0, 2 # Peso da nota 1
	addi $6, $0, 3 # Peso da nota 2
	addi $7, $0, 5 # Soma dos pesos das notas
	
	addi $2, $0, 5 
	syscall
	
	mult $2, $5
	mflo $8
	
	addi $2, $0, 5
	syscall
	
	mult $2, $6
	mflo $9
	
	add $4, $8, $9
	div $4, $7
	
	addi $2, $0, 1
	mflo $4
	syscall