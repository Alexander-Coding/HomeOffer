import { useField } from 'formik'

import Checkbox from '@mui/material/Checkbox'

import FormControl from '@mui/material/FormControl'
import FormHelperText from '@mui/material/FormHelperText'
import FormControlLabel from '@mui/material/FormControlLabel'

import type { FC } from 'react'
import type { TCheckboxFieldProps } from '@features/flatForm/adapters'


// Компонент-адаптер для чекбокс поля формы, интегрированный с Formik
export const CheckboxField: FC<TCheckboxFieldProps> = ({ name, label, disabled }) => {
    const [field, meta, helpers] = useField({ name, type: 'checkbox' });
    const isError = Boolean(meta.touched && meta.error);
    return (
        <FormControl error={isError} disabled={disabled}>
            <FormControlLabel
                control={
                    <Checkbox
                        checked={Boolean(field.value)}
                        onChange={(e) => helpers.setValue(e.target.checked)}
                        onBlur={field.onBlur}
                        name={name}
                    />
                }
                label={label}
            />
            {isError && <FormHelperText>{meta.error}</FormHelperText>}
        </FormControl>
    );
};
