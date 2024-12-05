class interfone{
    String modelo;
    String endereco;
    
    public Interfone(String modelo, String endereco){
        this.modelo = modelo;
        this.endereco = endereco;
    }
    public abstract void ligarPara();
    
    public abstract void registrarChamadas();
}

class InterfoneResidencial extends Interfone{
    String proprietario;
    String numero;


    public InterfoneResidencial(String endereco, String proprietario, String numero){
        super(endereco);
        this.proprietario1 = proprietario;
        this.numero = numero;
    }
    @Override
    public void ligarPara(){
        System.out.println("ligando para o/(a): "+nome+" e numero "+numero);
    }
    @Override
    public void registrarChamadas(String nome, String horario, String duracao){
        System.out.println("registrando a chamada: "+nome+" as "+horario+" com duracao "+duracao);
    }


}
