.text
main:
	addi $8, $0, 1
	addi $9, $0, 101
	
	
mainFor:
	add $4, $0, $8
	addi $2, $0, 1
	syscall
	
	addi $4, $0, '\n'
	addi $2, $0, 11
	syscall
	
	addi $8, $8, 1
	
	beq $8, $9, endFor
	
	j mainFor
	
	
endFor:
	addi $2, $0, 10
	syscall