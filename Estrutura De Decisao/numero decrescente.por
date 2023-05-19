programa {
  funcao inicio() {
    real maior, meio, menor
    inteiro n1, n2, n3
    escreva("Numero 1: ")
    leia(n1)
    escreva("Numero 2: ")
    leia(n2)
    escreva("Numero 3: ")
    leia(n3)
///Espaco Livre

/// numero 1
    se n1 > n2 e n1 > n3 {
      maior = n1
    }
    senao se n1 < n2 e n1 < n3{
      menor = n1
    }
    senao{
      meio = n1
    }
/// numero 2 

    se n2 > n1 e n2 > n3 {
      maior = n2
    }
    senao se n2 < n1 e n2 < n3{
      menor = n2
    }
    senao{
      meio = n2
    }

///numero 3
    se n3 > n1 e n3 > n2 {
      maior = n3
    }
    senao se n3 < n1 e n3 < n2{
      menor = n3
    }
    senao{
      meio = n3
    }

    escreva("Maior: ", maior)
    escreva("Meio: ", meio)
    escreva("Menor: ", menor)
  }
}