// utils/localStorage.js

// Salvar no localStorage
export const setItem = (key, value) => {
    localStorage.setItem(key, JSON.stringify(value));
  };
  
  // Recuperar do localStorage
  export const getItem = (key) => {
    const value = localStorage.getItem(key);
    return value ? JSON.parse(value) : null;
  };
  
  // Remover item específico do localStorage
  export const removeItem = (key) => {
    localStorage.removeItem(key);
  };
  
  // Limpar todo o localStorage
  export const clearStorage = () => {
    localStorage.clear();
  };
  