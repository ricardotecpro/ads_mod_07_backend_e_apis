#include <iostream>
#include <string>

using namespace std;

class Aluno {
private:
    string nome;
    int idade;
    int matricula;
    float mediaNotas;

public:
    // Construtor padr�o
    Aluno() {
        nome = "";
        idade = 0;
        matricula = 0;
        mediaNotas = 0.0;
    }

    // M�todo para cadastrar os dados do aluno
    void cadastrarDados() {
        cout << "Digite o nome do aluno: ";
        getline(cin, nome);
        cout << "Digite a idade do aluno: ";
        cin >> idade;
        cout << "Digite o n�mero de matr�cula do aluno: ";
        cin >> matricula;
        cin.ignore(); // limpar o buffer ap�s cin
    }

    // M�todo para cadastrar a m�dia de notas
    void cadastrarMediaNotas() {
        cout << "Digite a m�dia de notas do aluno: ";
        cin >> mediaNotas;
        cin.ignore();
    }

    // M�todo para exibir as informa��es do aluno
    void exibirInformacoes() {
        cout << "\n--- Informa��es do Aluno ---\n";
        cout << "Nome: " << nome << endl;
        cout << "Idade: " << idade << endl;
        cout << "Matr�cula: " << matricula << endl;
        cout << "M�dia de Notas: " << mediaNotas << endl;
    }
};

// Fun��o principal
int main() {
    Aluno aluno1;

    aluno1.cadastrarDados();
    aluno1.cadastrarMediaNotas();
    aluno1.exibirInformacoes();

    return 0;
}
