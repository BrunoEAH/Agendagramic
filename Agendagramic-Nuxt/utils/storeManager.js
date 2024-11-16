// utils/storageManager.js

import { setItem, getItem } from './localStorage';
import { STORAGE_KEYS } from './storageKeys';

// Atualizar usuários no localStorage
export const updateUsers = (users) => {
  setItem(STORAGE_KEYS.USERS, users);
};

// Atualizar grupos no localStorage
export const updateGroups = (groups) => {
  setItem(STORAGE_KEYS.GROUPS, groups);
};

// Recuperar todos os dados do localStorage
export const getAllData = () => ({
  users: getItem(STORAGE_KEYS.USERS),
  groups: getItem(STORAGE_KEYS.GROUPS),
  userTelegram: getItem(STORAGE_KEYS.USER_TELEGRAM),
});
