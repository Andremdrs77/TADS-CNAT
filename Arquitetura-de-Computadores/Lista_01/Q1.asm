.text
main: 
	addi $2, $0, 5
      	syscall
      	
      	
      	addi $5, $0, 2
      	mult $2, $5

      	addi $2, $0, 1
      	mflo $4
      	syscall