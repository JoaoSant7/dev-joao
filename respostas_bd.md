
# Respostas da Atividade – Banco de Dados

## 1.  
**Resposta:** c. Identificar unicamente cada linha de uma tabela.

---

## 2.  
**Resposta:** b. Permite compreender o que o banco precisa representar e as regras do negócio.

---

## 3.  
**Resposta:** d. Decidir sozinho o modelo conceitual do banco.

---

## 4.  
**Resposta:** b. O sistema apresentaria erro, pois a chave primária deve ser única.

---

## 5. Entidades e atributos  
- **Funcionário:** id_func, nome, cargo, salário  
- **Departamento:** id_depto, nome  
- **Projeto:** id_proj, nome, descrição  

Relacionamentos:  
- Funcionário → Departamento (1:N)  
- Funcionário ↔ Projeto (N:N)

---

## 6. Chaves primárias  
- **Cliente:** id_cliente (PK)  
- **Pedido:** id_pedido (PK)

Relação:  
`Pedido.id_cliente` é chave estrangeira que referencia `Cliente.id_cliente`.

---

## 7. Requisitos do sistema de reservas de hotel  

### Requisitos funcionais (8)
1. Registrar reservas  
2. Cancelar reservas  
3. Consultar disponibilidade  
4. Registrar clientes  
5. Registrar quartos  
6. Fazer check-in  
7. Fazer check-out  
8. Emitir relatórios  

### Requisitos não funcionais (5)
1. Sistema deve ser seguro  
2. Interface intuitiva  
3. Alta disponibilidade  
4. Resposta rápida  
5. Backup automático

---

## 8.  
**Resposta:** a. Nenhum produto poderá ter o mesmo código.

---

## 9.  
**Resposta:** b. O modelo conceitual descreve a realidade do negócio; o lógico traduz isso para tabelas.

---

## 10.  
**Resposta:** c. Modelagem conceitual

---

## 11.  
**Resposta:** c. Garante maior integridade, segurança e consistência das informações.

---

## 12. Entidades e atributos  
- **Cliente:** id_cliente, nome, telefone  
- **Produto:** id_produto, nome, preco  
- **Venda:** id_venda, data, id_cliente  
- **ItemVenda:** id_venda, id_produto, quantidade

---

## 13. Modelo Relacional  

**PACIENTE**(id_paciente **PK**, nome, telefone)  
**MÉDICO**(id_medico **PK**, nome, especialidade)  
**CONSULTA**(id_consulta **PK**, data, id_paciente **FK**, id_medico **FK**)

---

## 14.

### a) Requisitos funcionais  
1. Publicar postagens  
2. Adicionar amigos / seguir usuários  

### b) Requisitos não funcionais  
1. Alta performance  
2. Segurança de dados  

### c) Entidade e atributos  
**Usuário:** id_usuario, nome, email, senha

---

## 15.

### a)  
Uma boa modelagem evita redundância, organiza melhor os dados e facilita manutenção e expansão.

### b)  
Um SGBD aplica regras, validações, transações e integridade, reduzindo erros humanos.

---

## 16.  
**Resposta:** a. A chave primária é uma combinação única de valores que identifica cada registro.

---

## 17.  
**Resposta:** b. “Produto” é uma entidade e os demais são atributos.

---

## 18.  
**Resposta:** b. Levantar e entender o que o sistema deve armazenar e como deve funcionar.

---

## 19.

### 1. Entidades  
- Cliente  
- Produto  
- Venda  
- ItemVenda (necessário para relação muitos-para-muitos)

### 2. Atributos  

**Cliente**(id_cliente **PK**, nome, telefone, endereço)  
**Produto**(id_produto **PK**, nome, preco)  
**Venda**(id_venda **PK**, data, id_cliente **FK**)  
**ItemVenda**(id_venda **FK**, id_produto **FK**, quantidade)

### 3. Representação relacional  

CLIENTE(id_cliente **PK**, nome, telefone, endereco)  
PRODUTO(id_produto **PK**, nome, preco)  
VENDA(id_venda **PK**, data, id_cliente **FK**)  
ITEM_VENDA(id_venda **FK**, id_produto **FK**, quantidade)  
