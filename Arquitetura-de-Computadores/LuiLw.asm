.data #0x10010000


.word 12 #int a=12;
.word 24 #int b=24;
.word 3  #int c=3;
#.word, 12, 24, 3 => a=12, b=24, c=3;


.text
main: 	
	add $4, $0, $0
	lui $8, 0x1001
	addi $20, $0, 3
	
	
laco:
	beq $20, $0, terminou
	lw $21, 0($8)
	add $4, $4, $21
	addi $8, $8, 4
	addi $20, $20, -1
	j laco
	
	
terminou:
   	sw $4, 4($8)
   	addi $2, $0, 1
   	syscall
   	
   	addi $2, $0, 10
   	syscall