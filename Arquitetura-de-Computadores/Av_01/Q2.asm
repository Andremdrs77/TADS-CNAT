.text
main:
	addi $5, $0, 30
    	addi $6, $0, 31

    	addi $2, $0, 5
    	syscall

   	add $7, $0, $2

  	addi $8, $0, 2
    	bne $7, $8, verificar4

    	add $4, $0, $5
    	bne $4, $0, imprimir


	verificar4:
    		add $8, $0, 4
    		bne $7, $8, verificar6

    		add $4, $0, $5
    		bne $4, $0, imprimir

	verificar6:
    		add $8, $0, 6
    		bne $7, $8, verificar9

    		add $4, $0, $5
		bne $4, $0, imprimir

	verificar9:
    		addi $8, $0, 9
    		bne $7, $8, verificar11

    		add $4, $0, $5
    		bne $4, $0, imprimir

	verificar11:
    		addi $8, $0, 11
    		bne $7, $8, trinta_e_um

    		add $4, $0, $5
    		bne $4, $0, imprimir

	trinta_e_um:
    		add $4, $0, $6


	imprimir:
    		addi $2, $0, 1
    		syscall


    	addi $2, $0, 10
    	syscall
	
	