.text
main:
    addi $5, $0, 100
    addi $6, $0, 10
    
    addi $2, $0, 5
    syscall
    
    div $2, $5
    mflo $4
    mfhi $7
    
    addi $2, $0, 1
    syscall
    
    div $7, $6
    mflo $4
    
    syscall
    
    mfhi $4
    syscall
