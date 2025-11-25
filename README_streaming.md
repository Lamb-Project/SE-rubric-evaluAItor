# Sistema de Evaluación Automatizada - Versión Streaming

Esta versión del evaluador implementa **streaming** para todos los modelos de IA soportados, con **timeouts extendidos** para manejar respuestas más largas.

## 🚀 Características

- ✅ **Streaming activado** para Anthropic Claude, Ollama y OpenAI
- ⏱️ **Timeouts extendidos**: 15 minutos para streaming (antes 5 minutos)
- 🔄 **Reintentos aumentados**: Hasta 5 reintentos (antes 3)
- 📊 **Mejor feedback** durante la evaluación
- 🛡️ **Fallback automático** si el streaming falla

## 📋 Requisitos

```bash
pip install anthropic openai requests
```

## 🏃 Uso

### Con Ollama (Streaming activado)
```bash
python evaluador_streaming.py documento.md ./resultados --ollama llama2
```

### Con Anthropic Claude (Streaming activado)
```bash
python evaluador_streaming.py documento.md ./resultados --api-key sk-ant-...
```

### Con OpenAI (Streaming activado)
```bash
python evaluador_streaming.py documento.md ./resultados --openai gpt-4-turbo-preview
```

## 🔧 Diferencias con la versión anterior

| Característica | Anterior | Nueva Versión Streaming |
|---------------|----------|------------------------|
| Streaming Ollama | ❌ Desactivado | ✅ **Activado** |
| Streaming Anthropic | ❌ No disponible | ✅ **Activado** |
| Streaming OpenAI | ❌ No disponible | ✅ **Activado** |
| Timeout | 5 minutos | **15 minutos** |
| Reintentos | 3 | **5** |
| Rate limiting | 20K tokens/min | **15K tokens/min** |

## 🌊 Cómo funciona el streaming

1. **Ollama**: Procesa la respuesta JSON línea por línea
2. **Anthropic**: Usa el método `stream()` nativo del SDK
3. **OpenAI**: Usa `stream=True` en la API de completions

Cada fragmento de texto se procesa inmediatamente, permitiendo:
- Mejor experiencia de usuario
- Menor uso de memoria
- Respuestas más rápidas en apariencia
- Mejor manejo de respuestas largas

## 🐛 Solución de problemas

### Si el streaming falla
El sistema automáticamente hace fallback a modo no-streaming.

### Timeouts largos
Los timeouts de 15 minutos permiten procesar documentos muy grandes.

### Memoria
El streaming reduce significativamente el uso de memoria para respuestas largas.

## 📁 Archivos

- `evaluador_streaming.py` - Programa principal con streaming
- `utils/api_client_streaming.py` - Cliente API con soporte completo de streaming
- `README_streaming.md` - Esta documentación

## 🔄 Compatibilidad

Esta versión es **100% compatible** con la versión anterior. Los mismos comandos funcionan, pero ahora con streaming activado automáticamente.

## 📄 Licencia

Sistema de Evaluación Automatizada - Versión Streaming - Versión con soporte completo de streaming para todos los proveedores de IA.

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

**Autores:**
- Marc Alier
- Francisco Garcia-Peñalvo
- Alicia Garcia-Holgado
- Andrea Vázquez Ingelmo
- Maria José Casañ
- Juanan Pereira

**Universidades:**
- Universitat Politècnica de Catalunya (UPC)
- Universidad de Salamanca (USAL)
- Universitat Politècnica de València (UPV)
