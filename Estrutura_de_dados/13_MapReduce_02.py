#Para rodar: python 13_MapReduce_02.py empresas.csv

from mrjob.job import MRJob

class MRTotalFaturamento(MRJob):

    def mapper(self, _, line):
        # Ignorando a linha de cabeçalho
        if line.startswith("Ano"):
            return

        # Dividindo a linha em colunas
        columns = line.split(',')
        nome_empresa = columns[1]
        faturamento = float(columns[3])

        # Emitindo o nome da empresa e o faturamento
        yield (nome_empresa, faturamento)

    def reducer(self, nome_empresa, faturamentos):
        # Somando os faturamentos por empresa
        yield (nome_empresa, sum(faturamentos))

if __name__ == '__main__':
    MRTotalFaturamento.run()
