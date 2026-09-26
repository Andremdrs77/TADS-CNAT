.text
main:
	addi $5, $0, 3
	addi $6, $0, 33
	
	j for1
	
	for1:
		add $4, $0, $5
		addi $2, $0, 1
		syscall
		
		addi $5, $5, 3
		
		addi $4, $0, ' '
		addi $2, $0, 11
		syscall
		
		beq $5, $6, fim
		
		j for1
		
	fim:
		addi $2, $0, 10
		syscall