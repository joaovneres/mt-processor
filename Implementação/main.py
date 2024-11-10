import argparse

class TuringMachine:
    def __init__(self):
        self.num_states = 0
        self.states = []
        self.tape_alphabet = []
        self.extended_alphabet = []
        self.accept_state = ''
        self.transitions = {}
        self.input_strings = []
        self.blank_symbol = 'B'

    def read_input(self, input_file):
        """Lê o arquivo de entrada e inicializa a Máquina de Turing."""
        with open(input_file, 'r') as file:
            lines = file.readlines()

        index = 0

        # Leitura do número de estados
        self.num_states = int(lines[index].strip())
        self._validate_max_number(self.num_states, 10, "O número de estados")
        self.states = [f'q{i}' for i in range(self.num_states)]
        index += 1

        # Leitura do alfabeto de fita (Σ)
        input_data = lines[index].strip().split()
        num_terminals = int(input_data[0])
        self._validate_max_number(num_terminals, 10, "O número de símbolos terminais")
        self.tape_alphabet = input_data[1:num_terminals + 1]
        index += 1

        # Leitura do alfabeto estendido de fita (Σ') não presente em Σ
        input_data = lines[index].strip().split()
        num_extended = int(input_data[0])
        self.extended_alphabet = input_data[1:num_extended + 1]
        index += 1

        # Combina o alfabeto de fita com o alfabeto estendido
        self.full_alphabet = self.tape_alphabet + self.extended_alphabet

        # Leitura do estado de aceitação (qa)
        accept_state_index = int(lines[index].strip())
        self._validate_state_index(accept_state_index)
        self.accept_state = f'q{accept_state_index}'
        index += 1

        # Leitura do número de transições
        num_transitions = int(lines[index].strip())
        self._validate_max_number(num_transitions, 50, "O número de transições")
        index += 1

        # Inicializa o dicionário de transições
        for state in self.states:
            self.transitions[state] = {}

        # Leitura das transições
        for i in range(num_transitions):
            transition = lines[index + i].strip().split()
            if len(transition) != 5:
                raise ValueError("Erro: Transição malformada.")
            q = f'q{transition[0]}'
            symbol_read = transition[1]
            q_next = f'q{transition[2]}'
            symbol_write = transition[3]
            direction = transition[4]

            self._validate_state(q)
            self._validate_state(q_next)
            self._validate_symbol(symbol_read)
            self._validate_symbol(symbol_write)
            self._validate_direction(direction)

            if symbol_read not in self.transitions[q]:
                self.transitions[q][symbol_read] = (q_next, symbol_write, direction)
            else:
                raise ValueError(f"Erro: Transição duplicada para o estado '{q}' e símbolo '{symbol_read}'.")
        index += num_transitions

        # Leitura do número de cadeias de entrada
        num_input_strings = int(lines[index].strip())
        self._validate_max_number(num_input_strings, 10, "O número de cadeias de entrada")
        index += 1

        # Leitura das cadeias de entrada
        for i in range(num_input_strings):
            line = lines[index + i].strip()
            self._validate_max_number(len(line), 20, "O comprimento da cadeia de entrada")
            self.input_strings.append(line if line != '-' else '')
    
    def _validate_max_number(self, number, max_number, message):
        """Verifica se o número é menor ou igual ao máximo permitido."""
        if number > max_number:
            raise ValueError(f"Erro: {message} não pode ser maior que {max_number}.")

    def _validate_state_index(self, index):
        """Valida se o índice do estado está dentro do range."""
        if index < 0 or index >= self.num_states:
            raise ValueError(f"Erro: Índice de estado '{index}' fora do intervalo de estados definidos.")

    def _validate_state(self, state):
        """Verifica se o estado está definido no conjunto de estados."""
        if state not in self.states:
            raise ValueError(f"Erro: Estado '{state}' não definido no conjunto de estados.")

    def _validate_symbol(self, symbol):
        """Verifica se o símbolo está no alfabeto completo."""
        if symbol not in self.full_alphabet:
            raise ValueError(f"Erro: Símbolo '{symbol}' não definido no alfabeto de fita estendido.")

    def _validate_direction(self, direction):
        """Verifica se a direção é válida."""
        if direction not in {'R', 'L', 'S'}:
            raise ValueError(f"Erro: Direção inválida '{direction}'. Use 'R', 'L' ou 'S'.")

    def simulate(self, input_string):
        """Simula a Máquina de Turing para uma cadeia de entrada."""
        current_state = 'q0'
        tape = list(input_string) if input_string else [self.blank_symbol]
        head_position = 0

        # Usa um conjunto para manter o histórico de configurações para evitar loops infinitos
        configurations = set()

        while True:
            # Captura a configuração atual
            config = (current_state, head_position, ''.join(tape))
            if config in configurations:
                # Loop detectado, máquina não está em uma linguagem recursiva
                return "rejeita"
            configurations.add(config)

            # Verifica se o estado atual é o estado de aceitação
            if current_state == self.accept_state:
                return "aceita"

            # Lê o símbolo atual na fita
            if head_position < 0:
                tape.insert(0, self.blank_symbol)
                head_position = 0
            elif head_position >= len(tape):
                tape.append(self.blank_symbol)

            symbol = tape[head_position]

            # Obtém a transição
            if symbol in self.transitions[current_state]:
                next_state, write_symbol, direction = self.transitions[current_state][symbol]
                # Executa a transição
                tape[head_position] = write_symbol
                current_state = next_state

                if direction == 'R':
                    head_position += 1
                elif direction == 'L':
                    head_position -= 1
                elif direction == 'S':
                    pass  # Não move a cabeça
            else:
                # Sem transição válida, rejeita a cadeia
                return "rejeita"

    def evaluate_strings(self):
        """Avalia todas as cadeias de entrada e retorna se são aceitas ou rejeitadas."""
        results = []
        for input_string in self.input_strings:
            result = self.simulate(input_string)
            results.append(result)
        return results

    def write_output(self, output_file, results):
        """Escreve os resultados no arquivo de saída."""
        with open(output_file, 'w') as file:
            for result in results:
                file.write(f"{result}\n")

def main():
    parser = argparse.ArgumentParser(description="Simulador Universal de Máquinas de Turing.")
    parser.add_argument("input_file", nargs="?", help="Arquivo de entrada contendo a especificação da MT", default="entrada.txt")
    parser.add_argument("output_file", nargs="?", help="Arquivo de saída para escrever os resultados", default="saida.txt")

    args = parser.parse_args()

    try:
        tm = TuringMachine()
        tm.read_input(args.input_file)
        results = tm.evaluate_strings()
        tm.write_output(args.output_file, results)
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()
