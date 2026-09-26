.text
main:
	addi $2, $0, 5
	syscall 
	add $5, $0, $2
	
	addi $6, $0, 19
	div $5, $6 # calcular a
	mfhi $7	
	
	addi $6, $0, 100
	div $5, $6 
	mflo $8 # valor de b
	
	div $5, $6
	mfhi $9 # valor de c
	
	addi $6, $0, 4
	div $8, $6 
	mflo $10 # valor de d
	
	div $8, $6
	mfhi $11 # valor de e
	
	addi $12, $8, 8
	addi $6, $0, 25
	div $12, $6
	mflo $13 # valor de f
	
	add $12, $8, $0
	sub $12, $12, $13
	addi $12, $12, 1
	addi $6, $0, 3
	div $12, $6
	mflo $14 # valor de g
	
	addi $6, $0, 19
	mult $7, $6
	mflo $12
	add $12, $12, $8
	sub $12, $12, $10
	sub $12, $12, $14
	addi $12, $12, 15
	addi $6, $0, 30
	div $12, $6
	mfhi $15 # valor de h
	
	addi $6, $0, 4
	div $9, $6
	mflo $16 # valor de i
	
	div $9, $6
	mfhi $17 # valor de k
	
	addi $6, $0, 2
	mult $11, $6
	mflo $12 # 2 * e
	
	mult $16, $6
	mflo $18 # 2 * i
	
	addi $12, $12, 32
	add $12, $12, $18
	sub $12, $12, $15
	sub $12, $12, $17
	
	addi $6, $0, 7
	div $12, $6
	mfhi $19 # valor de l
	
	addi $6, $0, 11
	mult $15, $6
	mflo $12 # 11 * h
	
	addi $6, $0, 22
	mult $19, $6
	mflo $18 # 22 * l
	
	add $12, $12, $7
	add $12, $12, $18
	
	addi $6, $0, 451
	div $12, $6
	mflo $20 # valor de m
	
	addi $6, $0, 7
	mult $20, $6
	mflo $12 # 7 * m
	
	add $18, $15, $19
	sub $18, $18, $12
	addi $18, $18, 114
	
	addi $6, $0, 31
	div $18, $6
	mflo $21 # valor do mes
	
	div $18, $6
	mfhi $22
	addi $22, $22, 1 # valor do dia
	
	# imprimir dia
	addi $6, $0, 10
	sub $23, $22, $6
	bltz $23, zero_dia
	
	add $4, $0, $22
	addi $2, $0, 1
	syscall
	j barra
	
zero_dia:
	addi $2, $0, 11
	addi $4, $0, 48
	syscall
	
	add $4, $0, $22
	addi $2, $0, 1
	syscall
	
barra:
	addi $2, $0, 11
	addi $4, $0, 47
	syscall
	
	# imprimir mes
	addi $6, $0, 10
	sub $23, $21, $6
	bltz $23, zero_mes
	
	add $4, $0, $21
	addi $2, $0, 1
	syscall
	j barra_ano
	
zero_mes:
	addi $2, $0, 11
	addi $4, $0, 48
	syscall
	
	add $4, $0, $21
	addi $2, $0, 1
	syscall
	
barra_ano:
	addi $2, $0, 11
	addi $4, $0, 47
	syscall
	
	add $4, $0, $5
	addi $2, $0, 1
	syscall
	
 addi $2, $0, 10
 syscall