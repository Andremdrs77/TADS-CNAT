.text
main: 
	addi $3, $0, 10
	addi $1, $0, 2
	
	addi $2, $0, 5
	syscall
	
	add $5, $0, $2
	
	addi $2, $0, 5
	syscall
	
	add $6, $5, $2
	div $6, $1
	mfhi $5
	
	mflo $4
	addi $2, $0, 1
	syscall
	
	addi $4, $0, 46
	addi $2, $0, 11
	syscall
	
	mult $5, $3
	mflo $3
	div $3, $1 #se $3 for 0, vai simplesmente dar 0
	
	mflo $4
	addi $2, $0, 1
	syscall