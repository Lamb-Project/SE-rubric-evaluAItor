#!/usr/bin/env python3
"""
Script de prueba para verificar los diferentes proveedores de LLM
"""

import sys
from utils.config_manager import EvaluacionConfig
from utils.api_client import crear_cliente_api

def test_provider(provider, model=None, api_key=None):
    """Prueba un proveedor específico"""
    print(f"\n{'='*50}")
    print(f"Probando {provider.upper()}")
    print(f"{'='*50}")
    
    try:
        # Crear cliente
        client = crear_cliente_api(provider=provider, api_key=api_key, model=model)
        
        # Obtener información del modelo
        info = client.obtener_info_modelo()
        print(f"✓ Cliente creado exitosamente")
        print(f"  Modelo: {info['model']}")
        if 'provider' in info:
            print(f"  Provider: {info['provider']}")
        
        # Validar conexión
        print(f"\nValidando conexión...")
        if client.validar_conexion():
            print(f"✓ Conexión validada")
        else:
            print(f"✗ No se pudo validar la conexión")
        
        # Calcular costo estimado
        costo = client.calcular_costo_estimado(10)
        print(f"\nCosto estimado para 10 llamadas:")
        print(f"  Total: ${costo['costo_total_usd']:.4f} USD")
        if 'nota' in costo:
            print(f"  Nota: {costo['nota']}")
            
    except Exception as e:
        print(f"✗ Error: {e}")
        return False
    
    return True

def main():
    print("PRUEBA DE PROVEEDORES DE LLM")
    print("="*50)
    
    # Probar Anthropic (requiere API key)
    print("\n1. Anthropic (Claude)")
    if input("¿Probar Anthropic? (s/n): ").lower() == 's':
        test_provider("anthropic")
    
    # Probar Ollama (local)
    print("\n2. Ollama (Local)")
    if input("¿Probar Ollama? (s/n): ").lower() == 's':
        model = input("Modelo de Ollama (ej: llama2, mistral): ") or "llama2"
        test_provider("ollama", model=model)
    
    # Probar OpenAI (requiere API key)
    print("\n3. OpenAI")
    if input("¿Probar OpenAI? (s/n): ").lower() == 's':
        model = input("Modelo de OpenAI (ej: gpt-4-turbo-preview, gpt-3.5-turbo): ") or "gpt-4-turbo-preview"
        test_provider("openai", model=model)
    
    print("\n" + "="*50)
    print("Prueba completada")

if __name__ == "__main__":
    main() 