import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Main {
    Run|Debug
    public static void main(String[] args) {
        List<Student> students = new ArrayList<>();
        Scanner scanner = new Scanner(System.in);

        while (true) {
            Student.out.println(x:"1. Adicionar Aluno");
            Student.out.println(x:"2. Adicionar Nota");
            Student.out.println(x:"3. verificar aprovação");
            Student.out.println(x:"4. Sair");
            int choice = scanner.nextInt();

        switch(choice)`{
            case 1:
                System.out.print(s:"Digite o nome do aluno:");
                String name = scanner.next();
                System.out.print(s:"Idade do aluno:");
                int age = scanner.nextInt();
                Student student = new Student(name, age);
                Student.add(student);
                System.out.println(s:"Aluno adicionado");
                break;

        }


        }
    }
}

