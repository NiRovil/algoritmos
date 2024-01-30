// Aqui está minha visão do mesmo algoritmo aplicado na linguagem java

import java.util.ArrayList;

public class pesquisaBinaria{
    public static void main(String[] args) {

        Integer item = 7;
        ArrayList<Integer> minhaLista = new ArrayList<>();

        minhaLista.add(1);
        minhaLista.add(3);
        minhaLista.add(5);
        minhaLista.add(7);
        minhaLista.add(9);

        System.out.println(pesquisa(minhaLista, item));

    }

    public static Integer pesquisa(ArrayList<Integer> lista, Integer item){
        
        Integer inicio = 0;
        Integer fim = lista.size();

        while (inicio <= fim) {
            Integer meio = (inicio + fim) / 2;
            Integer chute = lista.get(meio);

            if (chute == item) {
                return meio;
            }

            if (chute > item) {
                fim = meio - 1;
            } else {
                inicio = meio + 1;
            }
        }

        return null;
    }
}