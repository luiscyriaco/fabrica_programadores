programa {
  funcao inicio() {
    
    // Criação das variáveis
    real peso
    real altura
    real imc

    // Solicitando os dados ao usuário
    escreva("Digite o peso (em kg): ")
    leia(peso)
    escreva("Digite a altura (em metros): ")
    leia(altura)

    // Realizando cálculo do imc=peso/altura²
    imc = peso / (altura * altura)
    
    // Apresentando resultado ao usuário    
    escreva("Seu IMC é: ", imc)
  }
}
