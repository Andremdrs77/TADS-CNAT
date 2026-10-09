.text
main: 
	lui $8, 0x1001   # $8 <= 0x10010000

      	lui $9, 0x0f0f   # $9 <= 0x00ff0000
      	srl $9, $9, 4
      	addi $10, $0, 512
     
      	addi $4, $0, 0
      	addi $5, $0, 0x00ffffff
      	
      	
laco: 
	beq $10, $0, player
     
     
      	addi $2, $0, 42
      	syscall
     
     
      	sw $4, 0($8)
      	sw $4, 2048($8)
     
     
      	addi $8, $8, 4
      	addi $10, $10, -1
      	j laco
     
 #     lui $8, 0x1001   # $8 <= 0x10010000
     
player:  
	addi $11, $0, 0x00ffffff
      	lui $8, 0x1001   # $8 <= 0x10010000
      	addi $8, $8, 256
      	sw $11, 0($8)
      	addi $14, $0, -4
     
     
# rotina para gastar tempo      
# usado: $25

nulltime:
        addi $25, $0, 4000
ntfor:  beq $25, $0, ntfim
        nop
        nop
        addi $25, $25, -1
        j ntfor        
ntfim: 
	jr $31
