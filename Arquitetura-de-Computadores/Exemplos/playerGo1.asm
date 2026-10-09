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
     
     
 	#lui $8, 0x1001   # $8 <= 0x10010000
     
     
player: 
	lui $11, 0x00ff  
      	ori $11, $11, 0xffff
      	lui $8, 0x1001   # $8 <= 0x10010000
      	addi $8, $8, 576
      	lui $16, 0xffff
     
     
     	sw $11, 0($8)
      	addi $14, $0, 4
     
     
plrGo:    
      	#testar se chegou em uma das bordas e, caso verdadeiro, multiplicar $14 por -1
      	lw $12, 2048($8)
      	sw $12, 0($8)
      	add $15, $8, $14
      	sw $11, 0($15)

      	add $8, $8, $14
     
      	jal nulltime
     
      	lw $17, 0($16)
      	beq $17, $0, plrGo
     
      	lw $17, 4($16)
      	addi $13, $0, 32
      	beq $17, $13, fim
     
      	addi $13, $0, 'a'
      	beq $13, $17, digA
     
      	addi $13, $0, 'd'
     	beq $13, $17, digD
     
      	addi $13, $0, 's'
     	beq $13, $17, digS
     
      	addi $13, $0, 'w'
      	beq $13, $17, digW
     
      	j plrGo            
                                              
digA: 
	addi $14, $0, -4
      	j plrGo
     
digD: 	
	addi $14, $0, 4
      	j plrGo  
     
digS: 
	addi $14, $0, 128
      	j plrGo
digW: 
	addi $14, $0, -128
      	j plrGo                    


fim:  
	addi $2, $0, 10
      	syscall
      	
      	
# rotina para gastar tempo      
# usado: $25
nulltime:
        addi $25, $0, 8800
ntfor:  beq $25, $0, ntfim
        nop
        nop
        addi $25, $25, -1
        j ntfor        
ntfim: jr $31