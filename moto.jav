public Class Moto {
    String marca;
    String modelo;
    string cor;
    int year;
    boolean isRunning;
    int velocidade;
    int cilindradas;


    public Moto(String marca, String modelo, int year){
        this.marca = marca;
        this.modelo = modelo;
        this.cor = cor;
        this.cilindradas = cilindradas;
        this.year = year;
        this.isRunning = false;
        this.velocidade = 0;
    }

    public void start(){
        if (!isRunning){
            isRunning = true;
            System.out.println("Moto ligada");
        }
    }

    public void stop(){
        if (isRunning){
            isRunning = false;
            System.out.println("Moto desligada");
        }
    }

    public void drive(int distancia){
        if (isRunning){
            this.velocidade += distancia;
            System.out.println("A moto esta em uma velocidade de " +distancia+ "km/h");
        }
    }

    public static void main(String[] args){
        Moto moto = new Moto("Honda", "CBR", 2015);
        moto.start();
        moto.drive(100);
        moto.stop();
    }
}