# PDF Signer Tool

## 📌 Sobre
Script Python que adiciona automaticamente uma imagem de assinatura em todas as páginas de um PDF, posicionando-a no canto inferior direito.

## 🛠️ Funcionalidades
- Insere imagem (JPG/PNG) como assinatura digital
- Processa todas as páginas do documento
- Configuração simplificada com caminhos pré-definidos
- Gera novo arquivo com prefixo `assinado_`

## ⚙️ Tecnologias
- Python 3
- Bibliotecas:
  - PyPDF2 (manipulação de PDF)
  - ReportLab (inserção de imagens)
  - Pillow (processamento de imagens)

## 🚀 Como Usar
1. Coloque os arquivos nas pastas:
   - PDFs originais: `/pdf`
   - Assinaturas: `/img`
2. Execute `python assinador.py`
3. Informe apenas os nomes dos arquivos
4. Resultado salvo em `/feito`

## 🔮 Futuras Atualizações
- **Versão Web com Django** (em desenvolvimento):
  - Upload via navegador
  - Interface amigável
  - Download direto do PDF assinado
  - Gerenciamento de usuários
- Opção para ajustar posição via interface
- Suporte a múltiplas assinaturas
- Sistema de templates de documentos


