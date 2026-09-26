.text
main:  #inicializacao
       addi $8, $0, 1 #i
       addi $9, $0, 11 #max
       
       #teste
for1:  beq $8, $9, fimfor1
       #corpo
       
       add $4, $0, $8  #
       addi $2, $0, 1  # imprime i
       syscall         #
       
       add $4, $0, ' '  #
       addi $2, $0, 11  # imprime espaco vazio
       syscall         #      
       
       #incremento
       addi $8, $8, 1    
       j for1          
fimfor1:  
       addi $2, $0, 10
       syscall