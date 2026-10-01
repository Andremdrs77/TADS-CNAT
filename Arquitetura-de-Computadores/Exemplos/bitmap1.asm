.text
main: 
	lui $8, 0x1001   # $8 <= 0x10010000

      	lui $9, 0x0f0f   # $9 <= 0x00ff0000
      	srl $9, $9, 4
      	addi $10, $0, 128
      
      
laco: 
	beq $10, $0, fim
      	lui $9, 0x0f0f   # $9 <= 0x00ff0000
      	srl $9, $9, 4
      	sw $9, 0($8)
     
      	srl $9, $9, 8
      	sw $9, 32256($8)
      	addi $8, $8, 4
      	addi $10, $10, -1
      	j laco
     
     
      lui $8, 0x1001   # $8 <= 0x10010000
      
      
fim:  
	addi $10, $0, 0
	
	
laco2: 
	beq $10, $0, fim2
      	sw $9, 0($8)
      	sw $9, 124($8)
      	addi $8, $8, 128
      	addi $10, $10, -1
      	j laco2


fim2:            
      	addi $2, $0, 10
      	syscall