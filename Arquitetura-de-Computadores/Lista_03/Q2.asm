.text
main:
	# número referência
	addi $2, $0, 5 
	syscall
	
	add $5, $0, $2
	add $7, $0, $2
	
	# vezes
	addi $2, $0, 5 
	syscall 
	
	addi $2, $2, 1
	
	# tratar 0
	add $8, $0, $2
	addi $9, $0, 1
	beq $2, 1, fim
	beq $0, $7, for0
	
	mult $5, $2
	mflo $6
	
	j for1
	
	
	for0:
		addi $9, $9, 1
		
		addi $4, $0, 0
		addi $2, $0, 1
		syscall
		
		addi $4, $0, ' '
		addi $2, $0, 11
		syscall
		
		beq $9, $8, fim
		
		j for0
		
		
	for1:
		add $4, $0, $5
		addi $2, $0, 1
		syscall
		
		add $5, $5, $7
		
		addi $4, $0, ' '
		addi $2, $0, 11
		syscall
		
		beq $5, $6, fim
		
		j for1
		
		
	fim:
		addi $2, $0, 10
		syscall
