# Multi-Provider Support for Evaluation System

This evaluation system now supports multiple LLM providers:

## Supported Providers

### 1. Anthropic (Default)
Uses Claude 3 Sonnet for evaluation.

**Requirements:**
- API key in environment variable `ANTHROPIC_API_KEY` or via `--api-key` parameter

**Usage:**
```bash
# Using environment variable
export ANTHROPIC_API_KEY=sk-ant-...
python evaluador.py documento.md ./resultados

# Using command line parameter
python evaluador.py documento.md ./resultados --api-key sk-ant-...
```

### 2. Ollama (Local)
Uses locally hosted models via Ollama.

**Requirements:**
- Ollama installed and running (default: http://localhost:11434)
- Model downloaded (e.g., `ollama pull llama2`)

**Usage:**
```bash
# Use with llama2
python evaluador.py documento.md ./resultados --ollama llama2

# Use with mistral
python evaluador.py documento.md ./resultados --ollama mistral:latest

# Use with any other model
python evaluador.py documento.md ./resultados --ollama codellama:13b
```

**Available models:** Run `ollama list` to see installed models.

### 3. OpenAI
Uses OpenAI's GPT models for evaluation.

**Requirements:**
- API key in environment variable `OPENAI_API_KEY` or via `--api-key` parameter
- `openai` package installed: `pip install openai`

**Usage:**
```bash
# Using environment variable with GPT-4 Turbo
export OPENAI_API_KEY=sk-...
python evaluador.py documento.md ./resultados --openai gpt-4-turbo-preview

# Using GPT-3.5 Turbo (cheaper option)
python evaluador.py documento.md ./resultados --openai gpt-3.5-turbo

# With explicit API key
python evaluador.py documento.md ./resultados --openai gpt-4 --api-key sk-...
```

## Cost Comparison

| Provider | Model | Cost per 1k tokens (Input/Output) | Notes |
|----------|-------|-----------------------------------|-------|
| Anthropic | claude-3-sonnet | $0.003 / $0.015 | High quality, default |
| OpenAI | gpt-4-turbo-preview | $0.01 / $0.03 | Very high quality |
| OpenAI | gpt-3.5-turbo | $0.0005 / $0.0015 | Good quality, cheaper |
| Ollama | Any | Free | Local execution, quality varies |

## Testing Providers

Run the test script to verify provider configuration:

```bash
python test_providers.py
```

## Examples

```bash
# Evaluate with Claude (default)
python evaluador.py trabajo_final.md ./evaluacion

# Evaluate with local Ollama model
python evaluador.py trabajo_final.md ./evaluacion --ollama mistral

# Evaluate with GPT-4
python evaluador.py trabajo_final.md ./evaluacion --openai gpt-4-turbo-preview

# Debug mode with Ollama
python evaluador.py trabajo_final.md ./evaluacion --ollama llama2 --debug
```

## Recommendations

- **For best quality:** Use Anthropic (Claude) or OpenAI (GPT-4)
- **For cost efficiency:** Use OpenAI (GPT-3.5-Turbo) or Ollama
- **For privacy/offline:** Use Ollama with local models
- **For testing:** Start with Ollama to avoid costs

## Troubleshooting

### Ollama Connection Error
```
Error: No se puede conectar con Ollama en http://localhost:11434
```
**Solution:** Ensure Ollama is running: `ollama serve`

### Model Not Found (Ollama)
```
Error validando conexión con Ollama
```
**Solution:** Pull the model first: `ollama pull <model-name>`

### OpenAI Import Error
```
ImportError: OpenAI library not installed
```
**Solution:** Install OpenAI library: `pip install openai`

### API Key Errors
- Anthropic: Ensure key starts with `sk-ant-`
- OpenAI: Ensure key starts with `sk-`
- Check environment variables are set correctly

## 📄 License

Multi-Provider Support for Evaluation System - Support for multiple LLM providers including Anthropic, Ollama, and OpenAI.

Copyright (C) 2025 Marc Alier, Francisco Garcia-Peñalvo, Alicia Garcia-Holgado, Andrea Vázquez Ingelmo, Maria José Casañ, Juanan Pereira

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.

## © Copyright

**Authors:**
- Marc Alier
- Francisco Garcia-Peñalvo
- Alicia Garcia-Holgado
- Andrea Vázquez Ingelmo
- Maria José Casañ
- Juanan Pereira

**Universities:**
- Universitat Politècnica de Catalunya (UPC)
- Universidad de Salamanca (USAL)
- Universitat Politècnica de València (UPV) 