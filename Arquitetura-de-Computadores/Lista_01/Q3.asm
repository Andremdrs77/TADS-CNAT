.text
main:
	addi $2, $0, 5
	syscall
	
	add $5, $0 $2
	
	addi $2, $0, 5
	syscall
	
	mult $2, $5
	mflo $4
	addi $2, $0, 1
	syscall
	