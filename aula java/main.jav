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
                
                case 2:
                    if (students.isEmpty()) {
                        System.out.println(s:"Nenhum aluno cadastrado");
                        continue;
                    }
                    for(int i = 0; i < students.size(); i++) {
                        System.out.println((i + 1) + " - " + students.get(i).name);
                    }
                    System.out.println(s:"Escolha o número do aluno:");
                    int studentIdx = scanner.nextInt() - 1;
                    if (studentIdx >= 0 && studentIdx < students.size()) {
                        System.out.print(s:"nota do Aluno");
                        double grade = scanner.nextDouble();
                        students.get(studentIdx).addGrade(grade);
                        System.out.println(x:"Nota adicionada");
                    } else {
                        System.out.println(s:"indice de aluno invalido");
                    }
                    break;

                case 3:
                    if (students.isEmpty()) {
                        System.out.println(s:"Nenhum aluno cadastrado");
                        continue;
                    }
                    for (Student s : students) {
                    double averageGrade = s.getAverageGrade();
                    String status = averageGrade >= 60 ? "Aprovado" : "Reprovado";
                    System.out.println(s.name + "-media" + averageGrade + "Status" + status);
                    }
                    break;

                case 4:
                    System.out.println(s:"Saindo...");
                    System.out.println(s:"obrigado por usar nosso sistema");
                    System.out.println(s:"Volte sempre!");
                    scanner.close();
                    return;
                default:
                    System.out.println(s:"Opção inválida, tente novamente");
                    break;


        }
    }
}

