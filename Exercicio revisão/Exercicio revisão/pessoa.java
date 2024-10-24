public class pessoa {
    private String origem;
    private int idade;
    private String genero;
    private String cor;
    private String profissao;


    public pessoa(String origem, int idade, String genero, String cor, String profissao) {
        this.origem = origem;
        this.idade = idade;
        this.genero = genero;
        this.cor = cor;
        this.profissao = profissao;
    }

    public String apresentacao() {
        return "Olá, sou do " + origem + ", tenho " + idade + " anos, "
                + "meu gênero é " + genero + ", minha etinía é " + cor + " e trabalho como " + profissao + ".";
    }

    public static void main(String[] args) {
        pessoa pessoa1 = new pessoa("Rio de Janeiro", 21, "masculino", "branco", "professor");
        System.out.println(pessoa1.apresentacao());
    }
}
