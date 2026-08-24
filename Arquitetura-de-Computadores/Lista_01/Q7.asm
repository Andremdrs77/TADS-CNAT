.text
main:
    addi $5, $0, 10
    addi $6, $0, 100
    addi $7, $0, 1000
    
    addi $2, $0, 5
    syscall
    
    div $2, $7
    mflo $8
    mfhi $2
    
    div $2, $6
    mflo $7
    mfhi $2
    
    div $2, $5
    mflo $6
    mfhi $2
    
    div $2, $5
    mfhi $5
    
    add $4, $0, $5
    addi $2, $0, 1
    syscall
    
    addi $2, $0, 11
    addi $4, $0, '\n'
    syscall
    
    addi $2, $0, 1
    add $4, $0, $6
    syscall
    
    addi $2, $0, 11
    addi $4, $0, '\n'
    syscall
    
    addi $2, $0, 1
    add $4, $0, $7
    syscall
    
    addi $2, $0, 11
    addi $4, $0, '\n'
    syscall
    
    addi $2, $0, 1
    add $4, $0, $8
    syscall
    
    addi $2, $0, 10
    syscall
