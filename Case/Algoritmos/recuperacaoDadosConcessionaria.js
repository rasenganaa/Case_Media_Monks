const fs = require('fs');

/**
 * Função para ler os arquivos JSON.
 *
 * @param {string} nomeArquivo - O nome do arquivo JSON a ser lido.
 * @returns {Array|Object|null} - Os dados lidos do arquivo JSON ou null em caso de erro.
 * @throws {Error} - Lança um erro se houver problemas ao ler o arquivo ou analisar o JSON.
 * @author Ana Caroline Brandão Costa
 */
function lerArquivo(nomeArquivo) {
    try {
        // Lê o conteúdo do arquivo especificado como JSON
        const dados = fs.readFileSync(nomeArquivo, 'utf8');
        return JSON.parse(dados);
    } catch (erro) {
        console.error(`Erro ao ler o arquivo ${nomeArquivo}: ${erro}`);
        return null;
    }
}

/**
 * Função para corrigir nomes de marca e veículo.
 *
 * @param {Object} registro - O registro a ser corrigido.
 * @returns {Object} - O registro com os nomes corrigidos.
 */
function corrigirNomesVeiculo(registro) {
    const { nome } = registro;

    // Substitui caracteres especiais nos nomes de veículos
    const nomeCorrigido = nome.replace(/æ/g, 'a').replace(/ø/g, 'o');
    return { ...registro, nome: nomeCorrigido };
}

/**
 * Função para corrigir vendas.
 *
 * @param {Object} registro - O registro a ser corrigido.
 * @returns {Object} - O registro com as vendas corrigidas.
 */
function corrigirVendas(registro) {
    // Converte a string de vendas para um número inteiro
    const vendasCorrigidas = parseInt(registro.vendas, 10);
    return { ...registro, vendas: vendasCorrigidas };
}

/**
 * Função para corrigir nomes de marca.
 *
 * @param {Object} registro - O registro a ser corrigido.
 * @returns {Object} - O registro com o nome da marca corrigido.
 */
function corrigirNomesMarca(registro) {
    const { marca } = registro;

    // Substitui caracteres especiais nos nomes de marca
    const marcaCorrigida = marca.replace(/æ/g, 'a').replace(/ø/g, 'o');
    return { ...registro, marca: marcaCorrigida };
}

/**
 * Função para exportar um arquivo JSON com o banco corrigido.
 *
 * @param {string} nomeArquivoDestino - O nome do arquivo JSON a ser exportado.
 * @param {Array} dadosCorrigidos - Os dados corrigidos a serem exportados.
 * @throws {Error} - Lança um erro se houver problemas ao exportar o arquivo.
 */
function exportarArquivo(nomeArquivoDestino, dadosCorrigidos) {
    try {
        // Converte os dados corrigidos para uma string JSON e escreve no arquivo
        const dadosJSON = JSON.stringify(dadosCorrigidos, null, 2);
        fs.writeFileSync(nomeArquivoDestino, dadosJSON);
        console.log(`Banco de dados corrigido exportado para ${nomeArquivoDestino}`);
    } catch (erro) {
        console.error(`Erro ao exportar o banco de dados corrigido: ${erro}`);
        throw erro; // Lança o erro novamente para tratamento em níveis superiores, se necessário
    }
}

/**
 * Função principal para recuperar os dados originais.
 * - Lê os arquivos JSON originais.
 * - Realiza correções nos nomes de veículo, nas vendas e nos nomes de marca.
 * - Exporta os arquivos corrigidos em formato JSON.
 * - Exibe mensagens de erro se houver problemas ao ler ou exportar os arquivos.
 */
function recuperarDadosOriginais() {
    // Ler os arquivos JSON originais
    const bancoOriginal1 = lerArquivo('broken_database_1.json');
    const bancoOriginal2 = lerArquivo('broken_database_2.json');

    if (!bancoOriginal1 || !bancoOriginal2) {
        console.error('Falha ao ler os arquivos JSON. Certifique-se de que os arquivos existem e têm formato válido.');
        return;
    }

    // Corrigir nomes de marca e veículo no primeiro banco
    const bancoCorrigidoNomesVeiculo = bancoOriginal1.map(corrigirNomesVeiculo);

    // Corrigir vendas no primeiro banco
    const bancoFinal = bancoCorrigidoNomesVeiculo.map(corrigirVendas);

    // Corrigir nomes de marca no segundo banco
    const bancoCorrigidoNomesMarca = bancoOriginal2.map(corrigirNomesMarca);

    // Exportar os arquivos corrigidos
    exportarArquivo('banco_corrigido_1.json', bancoFinal);
    exportarArquivo('banco_corrigido_2.json', bancoCorrigidoNomesMarca);
}

// Executar a função principal
recuperarDadosOriginais();
