import { useField } from 'formik'
import TextField from '@mui/material/TextField'

import type { FC } from 'react'
import type { TTextFieldProps } from '@features/flatForm/adapters'


// Компонент-адаптер для текстового поля формы, интегрированный с Formik
export const TextFieldField: FC<TTextFieldProps> = ({ name, ...props }) => {
    const [field, meta] = useField(name);
    const isError = Boolean(meta.touched && meta.error);
    return (
        <TextField
            {...field}
            {...props}
            error={isError}
            helperText={isError ? meta.error : props.helperText}
        />
    );
};
