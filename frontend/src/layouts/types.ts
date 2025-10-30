import type { ReactNode } from 'react'

// Интерфейс пропсов для макета основной страницы
export interface IMainPageLayoutProps {
    children:  ReactNode;
    title?:    string;
}