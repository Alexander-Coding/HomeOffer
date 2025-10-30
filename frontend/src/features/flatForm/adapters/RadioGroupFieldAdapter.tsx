import { useField } from 'formik'

import Radio from '@mui/material/Radio'
import RadioGroup from '@mui/material/RadioGroup'

import FormLabel from '@mui/material/FormLabel'
import FormControl from '@mui/material/FormControl'
import FormHelperText from '@mui/material/FormHelperText'
import FormControlLabel from '@mui/material/FormControlLabel'

import type { FC } from 'react'
import type { TRadioGroupFieldProps } from '@features/flatForm/adapters'


// Компонент-адаптер для радио группы формы, интегрированный с Formik
export const RadioGroupField: FC<TRadioGroupFieldProps> = (
    {
        name,
        label,
        options,
        row,
        disabled,
    }
) => {
    const [field, meta, helpers] = useField<string>(name);
    const isError = Boolean(meta.touched && meta.error);

    return (
        <FormControl error={isError} disabled={disabled}>
            {label && <FormLabel>{label}</FormLabel>}
            <RadioGroup
                row={row}
                name={name}
                value={field.value ?? ''}
                onChange={(e) => helpers.setValue(e.target.value)}
                onBlur={field.onBlur}
            >
                {options.map((opt) => (
                    <FormControlLabel key={opt.value} value={opt.value} control={<Radio />} label={opt.label} />
                ))}
            </RadioGroup>
            {isError && <FormHelperText>{meta.error}</FormHelperText>}
        </FormControl>
    );
};
