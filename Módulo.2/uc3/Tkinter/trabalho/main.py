import tkinter as tk
from tkinter import ttk, messagebox


class OrdemServico:
    def __init__(self, numero, cliente, telefone, equipamento, marca_modelo, descricao, valor, situacao="Pendente"):
        self.numero = numero
        self.cliente = cliente
        self.telefone = telefone
        self.equipamento = equipamento
        self.marca_modelo = marca_modelo
        self.descricao = descricao
        self.valor = valor
        self.situacao = situacao

    def alterar_situacao(self, situacao):
        self.situacao = situacao

    def exibir_informacoes(self):
        return (self.numero, self.cliente, self.telefone, self.equipamento,
                self.marca_modelo, self.descricao, self.valor, self.situacao)


class SistemaOS:
    def __init__(self, janela):
        self.janela = janela
        self.janela.title("EcoSpending - Gerenciamento de Ordens de Serviço")
        self.janela.geometry("1200x780")
        self.janela.minsize(1000, 700)
        self.janela.configure(bg="#eef3f0")

        self.ordens = []
        self.proximo_numero = 1

        self.criar_interface()
        self.atualizar_lista()
        self.atualizar_indicadores()

    def criar_interface(self):
        topo = tk.Frame(self.janela, bg="#123c2a", height=90)
        topo.pack(fill="x")
        topo.pack_propagate(False)

        tk.Label(topo, text="ECOSPENDING", font=("Arial", 18, "bold"),
                 fg="white", bg="#123c2a").pack(anchor="w", padx=25, pady=(12, 0))
        tk.Label(topo, text="Gerenciamento de Ordens de Serviço",
                 font=("Arial", 12), fg="#d5e9dd", bg="#123c2a").pack(anchor="w", padx=25)

        corpo = tk.Frame(self.janela, bg="#eef3f0")
        corpo.pack(fill="both", expand=True, padx=20, pady=15)

        cadastro = tk.LabelFrame(corpo, text="Nova Ordem de Serviço", font=("Arial", 11, "bold"),
                                bg="#eef3f0", padx=12, pady=10)
        cadastro.pack(fill="x", pady=(0, 12))

        self.campos = {}
        campos = [
            ("Cliente", "cliente"),
            ("Telefone", "telefone"),
            ("Equipamento", "equipamento"),
            ("Marca/modelo", "marca_modelo"),
            ("Valor (R$)", "valor"),
        ]

        for i, (texto, chave) in enumerate(campos):
            linha = i // 3
            coluna = (i % 3) * 2
            tk.Label(cadastro, text=texto, bg="#eef3f0", font=("Arial", 10)).grid(
                row=linha, column=coluna, sticky="w", padx=(5, 8), pady=6)
            entrada = tk.Entry(cadastro, width=30, font=("Arial", 10))
            entrada.grid(row=linha, column=coluna + 1, sticky="ew", padx=(0, 12), pady=6)
            self.campos[chave] = entrada

        tk.Label(cadastro, text="Descrição do problema", bg="#eef3f0",
                 font=("Arial", 10)).grid(row=2, column=0, sticky="nw", padx=5, pady=6)
        self.descricao = tk.Text(cadastro, height=3, width=80, font=("Arial", 10))
        self.descricao.grid(row=2, column=1, columnspan=5, sticky="ew", padx=(0, 12), pady=6)

        botoes_cadastro = tk.Frame(cadastro, bg="#eef3f0")
        botoes_cadastro.grid(row=3, column=0, columnspan=6, pady=8)
        tk.Button(botoes_cadastro, text="Cadastrar OS", command=self.cadastrar,
                  bg="#1f8a57", fg="white", font=("Arial", 10, "bold"),
                  padx=15, pady=5).pack(side="left", padx=5)
        tk.Button(botoes_cadastro, text="Limpar campos", command=self.limpar,
                  bg="#66736c", fg="white", font=("Arial", 10),
                  padx=15, pady=5).pack(side="left", padx=5)

        consulta = tk.LabelFrame(corpo, text="Consulta e listagem", font=("Arial", 11, "bold"),
                                bg="#eef3f0", padx=12, pady=10)
        consulta.pack(fill="both", expand=True)

        busca_frame = tk.Frame(consulta, bg="#eef3f0")
        busca_frame.pack(fill="x", pady=(0, 10))
        tk.Label(busca_frame, text="Nome ou número da OS:", bg="#eef3f0").pack(side="left")
        self.busca = tk.Entry(busca_frame, width=30)
        self.busca.pack(side="left", padx=8)
        tk.Button(busca_frame, text="Buscar", command=self.buscar,
                  bg="#286c50", fg="white").pack(side="left", padx=3)
        tk.Button(busca_frame, text="Listar todas", command=self.atualizar_lista,
                  bg="#66736c", fg="white").pack(side="left", padx=3)

        tabela_frame = tk.Frame(consulta)
        tabela_frame.pack(fill="both", expand=True)

        colunas = ("numero", "cliente", "telefone", "equipamento", "modelo", "situacao", "valor")
        self.tabela = ttk.Treeview(tabela_frame, columns=colunas, show="headings", height=12)
        nomes = ("OS", "Cliente", "Telefone", "Equipamento", "Marca/modelo", "Situação", "Valor")
        larguras = (65, 170, 130, 130, 160, 130, 100)
        for coluna, nome, largura in zip(colunas, nomes, larguras):
            self.tabela.heading(coluna, text=nome)
            self.tabela.column(coluna, width=largura, anchor="center")
        scrollbar = ttk.Scrollbar(tabela_frame, orient="vertical", command=self.tabela.yview)
        self.tabela.configure(yscrollcommand=scrollbar.set)
        self.tabela.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        operacoes = tk.Frame(consulta, bg="#eef3f0")
        operacoes.pack(fill="x", pady=10)
        tk.Label(operacoes, text="Número da OS:", bg="#eef3f0").pack(side="left")
        self.numero_operacao = tk.Entry(operacoes, width=8)
        self.numero_operacao.pack(side="left", padx=6)

        tk.Label(operacoes, text="Nova situação:", bg="#eef3f0").pack(side="left", padx=(12, 0))
        self.situacao = ttk.Combobox(operacoes, values=("Pendente", "Em andamento", "Concluído", "Entregue"),
                                     state="readonly", width=16)
        self.situacao.pack(side="left", padx=6)
        tk.Button(operacoes, text="Alterar situação", command=self.alterar,
                  bg="#286c50", fg="white").pack(side="left", padx=5)
        tk.Button(operacoes, text="Remover OS", command=self.remover,
                  bg="#b34242", fg="white").pack(side="left", padx=5)

        indicadores = tk.LabelFrame(corpo, text="Indicadores e controle financeiro",
                                   font=("Arial", 11, "bold"), bg="#eef3f0", padx=10, pady=8)
        indicadores.pack(fill="x", pady=(12, 0))
        self.indicadores_label = tk.Label(indicadores, text="", bg="#eef3f0",
                                          font=("Arial", 10), justify="left")
        self.indicadores_label.pack(anchor="w")

        self.mensagem = tk.Label(self.janela, text="Sistema pronto.", bg="#dce8e1",
                                fg="#123c2a", anchor="w", padx=12, pady=7)
        self.mensagem.pack(fill="x", side="bottom")

    def cadastrar(self):
        dados = {chave: entrada.get().strip() for chave, entrada in self.campos.items()}
        descricao = self.descricao.get("1.0", "end").strip()

        if any(not valor for valor in dados.values()) or not descricao:
            self.mostrar_mensagem("Preencha todos os campos.", erro=True)
            return

        try:
            valor = float(dados["valor"].replace(",", "."))
            if valor < 0:
                raise ValueError
        except ValueError:
            self.mostrar_mensagem("Informe um valor numérico válido e não negativo.", erro=True)
            return

        ordem = OrdemServico(
            self.proximo_numero, dados["cliente"], dados["telefone"],
            dados["equipamento"], dados["marca_modelo"], descricao, valor
        )
        self.ordens.append(ordem)
        self.proximo_numero += 1
        self.limpar()
        self.atualizar_lista()
        self.atualizar_indicadores()
        self.mostrar_mensagem(f"OS {ordem.numero:03d} cadastrada com sucesso!")

    def limpar(self):
        for entrada in self.campos.values():
            entrada.delete(0, "end")
        self.descricao.delete("1.0", "end")
        self.mostrar_mensagem("Formulário limpo.")

    def atualizar_lista(self, ordens=None):
        if ordens is None:
            ordens = self.ordens
        for item in self.tabela.get_children():
            self.tabela.delete(item)
        for ordem in ordens:
            self.tabela.insert("", "end", values=(
                f"{ordem.numero:03d}", ordem.cliente, ordem.telefone,
                ordem.equipamento, ordem.marca_modelo, ordem.situacao,
                f"R$ {ordem.valor:.2f}".replace(".", ",")
            ))

    def buscar(self):
        termo = self.busca.get().strip().lower()
        if not termo:
            self.atualizar_lista()
            return
        resultados = [
            ordem for ordem in self.ordens
            if termo in ordem.cliente.lower() or termo == str(ordem.numero)
            or termo == f"{ordem.numero:03d}"
        ]
        self.atualizar_lista(resultados)
        if resultados:
            self.mostrar_mensagem(f"{len(resultados)} resultado(s) encontrado(s).")
        else:
            self.mostrar_mensagem("Nenhuma ordem de serviço encontrada.", erro=True)

    def encontrar_ordem(self):
        numero_texto = self.numero_operacao.get().strip()
        if not numero_texto:
            self.mostrar_mensagem("Informe o número da OS.", erro=True)
            return None
        try:
            numero = int(numero_texto)
        except ValueError:
            self.mostrar_mensagem("O número da OS deve ser inteiro.", erro=True)
            return None
        ordem = next((o for o in self.ordens if o.numero == numero), None)
        if ordem is None:
            self.mostrar_mensagem("OS não encontrada.", erro=True)
        return ordem

    def alterar(self):
        ordem = self.encontrar_ordem()
        if ordem is None:
            return
        nova = self.situacao.get()
        if not nova:
            self.mostrar_mensagem("Selecione uma situação.", erro=True)
            return
        ordem.alterar_situacao(nova)
        self.atualizar_lista()
        self.atualizar_indicadores()
        self.mostrar_mensagem(f"Situação da OS {ordem.numero:03d} atualizada.")

    def remover(self):
        ordem = self.encontrar_ordem()
        if ordem is None:
            return
        if not messagebox.askyesno("Confirmar", f"Deseja remover a OS {ordem.numero:03d}?"):
            return
        self.ordens.remove(ordem)
        self.atualizar_lista()
        self.atualizar_indicadores()
        self.mostrar_mensagem(f"OS {ordem.numero:03d} removida.")

    def atualizar_indicadores(self):
        total = len(self.ordens)
        pendentes = sum(o.situacao == "Pendente" for o in self.ordens)
        andamento = sum(o.situacao == "Em andamento" for o in self.ordens)
        concluidos = sum(o.situacao == "Concluído" for o in self.ordens)
        entregues = sum(o.situacao == "Entregue" for o in self.ordens)
        valor_total = sum(o.valor for o in self.ordens)
        valor_finalizados = sum(o.valor for o in self.ordens if o.situacao in ("Concluído", "Entregue"))

        texto = (
            f"Total de OS: {total}   |   Pendentes: {pendentes}   |   Em andamento: {andamento}   |   "
            f"Concluídos: {concluidos}   |   Entregues: {entregues}\n"
            f"Valor total dos serviços: R$ {valor_total:.2f}   |   "
            f"Concluídos e entregues: R$ {valor_finalizados:.2f}"
        ).replace(".", ",")
        self.indicadores_label.config(text=texto)

    def mostrar_mensagem(self, texto, erro=False):
        self.mensagem.config(text=texto, fg="#a12b2b" if erro else "#123c2a")


if __name__ == "__main__":
    janela = tk.Tk()
    app = SistemaOS(janela)
    janela.mainloop()
