public class Car{
    string marca;
    string modelo;
    int year;
    boolean isRunning;
    int velocidade ;

    public Car(string marca, string modelo, int year){
        this.marca = marca;
        this.modelo = modelo;
        this.year = year;
        this.lsRunning = false;
        this.velocidade = 0;
    }
    // definindo os metodos
    // ligar o carro
    public void start(){
        if (!isRunning){
            lsRunning = True;
            System.out.println("Carro ligado");
        }
    }

    // desligar o carro
    public void stop(){
        if (isRunning){
            isRunning = false;
            System.out.println('Carro desligado');
        }
    }
}