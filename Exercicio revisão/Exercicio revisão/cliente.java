public class cliente {
    private String nome;
    private String email;
    private String senha;  

    public cliente(String nome, String email, String senha) {
        this.nome = nome;
        this.email = email;
        this.senha = senha;
    }

    public void exibirInformacoes() {
        System.out.println("Nome: " + nome + "\nEmail: " + email);
    }

    public void alterarSenha(String novaSenha) {
        this.senha = novaSenha;
        System.out.println("Senha alterada com sucesso.");
    }

    public boolean verificarSenha(String senha) {
        return this.senha.equals(senha);
    }

    public static cliente criarCliente(String nome, String email, String senha) {
        return new cliente(nome, email, senha);
    }

    public static void main(String[] args) {
        cliente cliente1 = cliente.criarCliente("Rafael", "rafael@gmail.com", "123");
        cliente1.exibirInformacoes();
        System.out.println(cliente1.verificarSenha("senha123")); 
        cliente1.alterarSenha("456");  
    }
    
}
