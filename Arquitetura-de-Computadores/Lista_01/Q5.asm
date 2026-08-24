.text
main:
	addi $5, $0, 100
	addi $6, $0, 10
	
	addi $2, $0, 5
	syscall
	
	div $2, $5
	mfhi $2
	mflo $7
	
	div $2, $6
	mflo $8
	mfhi $9
	
	add $4, $0, $7
	add $7, $8, $9
	add $4, $4, $7
	
	addi $2, $0, 1
	syscall
	
	addi $2, $0, 10
	syscall
