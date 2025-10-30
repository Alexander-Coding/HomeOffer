import type { TextFieldProps } from '@mui/material/TextField'


// Тип пропсов для текстового поля формы
// Исключаем 'name', 'value', 'onChange', 'onBlur' из TextFieldProps и добавляем обязательное 'name'
export type TTextFieldProps = Omit<TextFieldProps, 'name' | 'value' | 'onChange' | 'onBlur'> & { name: string; };


// Тип пропсов для чекбокс поля формы
export type TCheckboxFieldProps = { name: string; label: string; disabled?: boolean };


// Тип пропсов для radio группы формы
type _TRadioOption = { label: string; value: string }
export type TRadioGroupFieldProps = {
    name:      string;           // Имя поля формы
    label?:    string;           // Метка группы радио кнопок
    options:   _TRadioOption[];  // Данные радио кнопок в группе
    row?:      boolean;          // Расположить радио кнопки в ряд
    disabled?: boolean           // Отключено ли поле
};
