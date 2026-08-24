.text
main:
	addi $2, $0, 5
	syscall
	
	add $5, $0, $2
	mult $5, $5
	
	mflo $4
	addi $2, $0, 1
	syscall