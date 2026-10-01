.text 
main: 	# codigo para 16x16

	lui $8, 0x1001   # $8 <= 0x10010000

      	lui $9, 0x0f0f   # $9 <= 0x00ff0000
      	srl $9, $9, 4
      	addi $10, $0, 512
     
      	addi $4, $0, 0	# valor aleatorio minimo
      	addi $5, $0, 0x00ffffff	# valor aleatorio maximo 
      	
      	
laco: 
	beq $10, $0, fim
     
      	addi $2, $0, 42
      	syscall
     
     
     	sw $4, 0($8)
     
     
     	addi $8, $8, 4
      	addi $10, $10, -1
      	j laco
     
     
      	lui $8, 0x1001   # $8 <= 0x10010000
      	
      	
fim:  
      	addi $2, $0, 10
      	syscall