import mysql.connector

class Database:
    def __init__(self):
        try:        

            self.conexao = mysql.connector.connect(
                host="host.docker.internal",
                user="root",
                password="",
                database="licitasp"
            )
            self.cursor = self.conexao.cursor(dictionary=True)  # Retorna os resultados como dicionário
        except mysql.connector.Error as e:
            print(f"Erro ao conectar ao banco de dados: {e}")
            raise

    def executar_query(self, query, valores=None, fetch=False):
        try:
            if valores:
                self.cursor.execute(query, valores)
            else:
                self.cursor.execute(query)

            if fetch:
                return self.cursor.fetchall()  # Retorna os resultados se necessário

            self.conexao.commit()
            return True  # Indica sucesso
        except mysql.connector.Error as e:
            print(f"Erro ao executar query: {e}")
            self.conexao.rollback()
            return None

    def executar_many(self, query, valores_list):        
        try:
            self.cursor.executemany(query, valores_list)
            self.conexao.commit()
            return True
        except mysql.connector.Error as e:
            print(f"Erro ao executar query em lote: {e}")
            self.conexao.rollback()
            return None

    ## Função Genérica para criar uma tabela no banco de dados
    def criar_tabela(self, nome_tabela, estrutura_colunas):
        # Cria a tabela caso ela não exista
        query = f"""
        CREATE TABLE IF NOT EXISTS {nome_tabela} (
            {estrutura_colunas}
        );
        """
        if self.executar_query(query):
            print(f"Tabela '{nome_tabela}' criada ou já existe.")
        else:
            print(f"Erro ao criar a tabela '{nome_tabela}'.")

    def fechar_conexao(self):
        if self.cursor:
            self.cursor.close()
        if self.conexao:
            self.conexao.close()
